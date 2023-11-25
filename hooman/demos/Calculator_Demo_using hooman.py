from hooman import Hooman
import pygame

class Calculator:
    def _init_(self):
        self.width, self.height = 600, 800
        self.h = pygame.display.set_mode((self.width, self.height))
        pygame.font.init()
        self.font_big = pygame.font.Font(None, 50)
        self.font_small = pygame.font.Font(None, 36)
        self.expression = ""
        self.result = ""
        self.prev_left_button = False

        self.buttons = [
            ("7", 20, 200, 120, 80), ("8", 160, 200, 120, 80), ("9", 300, 200, 120, 80), ("/", 440, 200, 120, 80),
            ("4", 20, 300, 120, 80), ("5", 160, 300, 120, 80), ("6", 300, 300, 120, 80), ("*", 440, 300, 120, 80),
            ("1", 20, 400, 120, 80), ("2", 160, 400, 120, 80), ("3", 300, 400, 120, 80), ("-", 440, 400, 120, 80),
            ("C", 20, 500, 120, 80), ("0", 160, 500, 120, 80), ("=", 300, 500, 120, 80), 
            ("+", 440, 500, 120, 80),
        ]

    def calculate(self):
        try:
            self.result = str(eval(self.expression))
        except:
            self.result = "Error"

    def handle_button_click(self, button_text):
        if button_text == "=":
            self.calculate()
        elif button_text == "C":
            self.expression = ""
            self.result = ""
        else:
            self.expression += button_text

    def draw_button(self, text, x, y, width, height):
        pygame.draw.rect(self.h, pygame.Color(200, 200, 200), (x, y, width, height))
        text_surface = self.font_small.render(text, True, pygame.Color("blue"))
        text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
        self.h.blit(text_surface, text_rect)

    def draw(self):
        self.h.fill(pygame.Color("grey"))

        text_surface = self.font_big.render(self.expression, True, pygame.Color("white"))
        self.h.blit(text_surface, (20, 50))

        text_surface = self.font_big.render(self.result, True, pygame.Color("black"))
        self.h.blit(text_surface, (20, 100))

        for button in self.buttons:
            text, x, y, width, height = button
            self.draw_button(text, x, y, width, height)

        pygame.display.flip()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def run(self):
        self.is_running = True
        while self.is_running:
            self.draw()

            mouse_x, mouse_y = pygame.mouse.get_pos()
            left_button, _, _ = pygame.mouse.get_pressed()

            if left_button and not self.prev_left_button:
                for button in self.buttons:
                    text, x, y, width, height = button
                    if x < mouse_x < x + width and y < mouse_y < y + height:
                        self.handle_button_click(text)

            self.prev_left_button = left_button

            self.event_loop()

if _name_ == "_main_":
    calculator = Calculator()
    calculator.run()
