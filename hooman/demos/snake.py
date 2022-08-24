import hooman
import random
import pygame

WIDTH, HEIGHT = 600, 600

hapi = hooman.Hooman(WIDTH, HEIGHT)

btn_style = {
    "outline": True,
    "background_color": (255, 0, 0),
    "curve": 0.7,
    "hover_outline_thickness": 3,
}

slider_style = {
    "background_color": (200, 200, 200),
    "slider_height": 60,
    "slider_color": (240, 240, 240),
}


class Game:
    def __init__(self):
        self.current_screen = self.Main_menu
        hapi.handle_events = self.Events

        self.menu_btn_start = hapi.button(200, 200, 200, 50, "Start", btn_style)
        self.menu_btn_quit = hapi.button(200, 400, 200, 50, "Quit", btn_style)
        self.settings_btn = hapi.button(200, 300, 200, 50, "Settings", btn_style)

        slider_style.update({"range": [5, 30], "step": 1, "starting_value": 20})
        self.rows_slider = hapi.slider(300, 200, 200, 30, slider_style)
        self.rows_slider = hapi.slider_with_text(self.rows_slider)

        slider_style.update(
            {"range": [0.01, 1], "step": 0, "starting_value": 0.1}
        )
        self.speed_slider = hapi.slider(300, 300, 200, 30, slider_style)
        self.speed_slider = hapi.slider_with_text(self.speed_slider, {"accuracy": 2})
        self.slider_names = ["num of rows", "speed"]
        self.back_btn = hapi.button(200, 400, 200, 50, "Back", btn_style)

        self.size = WIDTH // self.rows_slider.value()

        self.start_pos = 5, 5
        self.head = [x * self.size for x in self.start_pos]
        self.body = []
        self.food_pos = [
            random.randint(0, WIDTH) // self.size * self.size for x in range(2)
        ]
        self.direction = [0, 0]
        self.move = hapi.timer(seconds=self.speed_slider.value())

    def Start(self):
        while hapi.is_running:
            self.current_screen()

            hapi.flip_display()
            hapi.event_loop()

    def Main(self):
        hapi.background(hapi.color["black"])
        hapi.fill(hapi.color["yellow"])
        hapi.rect(self.head[0] + 1, self.head[1] + 1, self.size - 2, self.size - 2)
        for x, y in self.body:
            hapi.rect(x + 1, y + 1, self.size - 2, self.size - 2)
        if self.move:
            for i in range(len(self.body) - 1, 0, -1):
                self.body[i] = self.body[i - 1]
            if len(self.body) > 0:
                self.body[0] = self.head
            self.head = [self.head[i] + self.direction[i] for i in range(2)]
            self.move = hapi.timer(seconds=self.speed_slider.value())
            if self.head in self.body:
                self.Died()
            elif (
                self.head[0] >= WIDTH
                or self.head[0] < 0
                or self.head[1] < 0
                or self.head[1] >= HEIGHT
            ):
                self.Died()
            if self.head == self.food_pos:
                self.body.append(self.head[:])
                self.food_pos = [
                    random.randint(0, WIDTH) // self.size * self.size for x in range(2)
                ]
        hapi.fill(hapi.color["green"])
        hapi.rect(self.food_pos[0], self.food_pos[1], self.size - 1, self.size - 1)

    def Died(self):
        self.head = [x * self.size for x in self.start_pos]
        self.body = []
        self.food_pos = [
            random.randint(0, WIDTH) // self.size * self.size for x in range(2)
        ]
        self.direction = [0, 0]
        self.current_screen = self.Main_menu

    def Settings(self):
        hapi.background(hapi.color["white"])
        self.speed_slider.update()
        self.rows_slider.update()
        hapi.fill(hapi.color["black"])
        hapi.font_size(30)
        hapi.text(self.slider_names[0], 100, 200)
        hapi.text(self.slider_names[1], 100, 300)
        if self.back_btn.update():
            self.current_screen = self.Main_menu

    def Main_menu(self):
        hapi.background(hapi.color["white"])
        hapi.fill(hapi.color["black"])
        hapi.font_size(50)
        hapi.text("Snake", 220, 30)
        if self.menu_btn_quit.update():
            hapi.is_running = False
        if self.menu_btn_start.update():
            self.current_screen = self.Main
        if self.settings_btn.update():
            self.current_screen = self.Settings

    def Events(self, event):
        if event.type == pygame.QUIT:
            hapi.is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "a" or event.key == 276:
                self.direction = [-self.size, 0]
            elif event.unicode == "d" or event.key == 275:
                self.direction = [self.size, 0]
            elif event.unicode == "w" or event.key == 273:
                self.direction = [0, -self.size]
            elif event.unicode == "s" or event.key == 274:
                self.direction = [0, self.size]


if __name__ == "__main__":
    game = Game()
    game.Start()
