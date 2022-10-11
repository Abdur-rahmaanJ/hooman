from hooman import Hooman
from hooman.formula import distance
from hooman.ui import Button

import pygame

pen = Hooman(500, 500)

attempt_button_coords = [] # coords for lock buttons in user pattern
attempt_button_ids = [] # ids of lock buttons in user pattern
buttons = [] # list of buttons to display
display_win = False
pattern = [1, 2, 3, 4, 5, 6, 7] # ids of password


# --- reset button ---
def reset_clicked(this):
    global attempt_button_coords, attempt_button_ids, display_win
    attempt_button_coords = []
    attempt_button_ids = []
    display_win = False


reset_button_styles = {
    "hover_background_color": (200, 200, 200),
    "font_size": 10,
    "background_color": (210, 210, 210),
    "on_click": reset_clicked,
    "curve": 1,
}
reset_button = Button(250, 10, 150, 20, "Reset", reset_button_styles)


class LockButton:
    def __init__(self, x, y, pen, num=0):
        self.x = x
        self.y = y
        self.pen = pen
        self.num = num

    def coords(self):
        return (self.x, self.y)

    def draw(self):
        pen = self.pen

        pen.fill(0)
        pen.ellipse(self.x, self.y, 20, 20)

    def update(self):
        pen = self.pen
        global attempt_button_coords, attempt_button_ids

        if pen.pygame.mouse.get_pressed()[0]:

            mouse_coords = (pen.mouseX(), pen.mouseY())
            if distance(self.coords(), mouse_coords) <= 20:
                if self.coords() not in attempt_button_coords:
                    attempt_button_ids.append(self.num)
                    attempt_button_coords.append(self.coords())

    def run(self):
        self.update()
        self.draw()


# --- initialise buttons ---
button_id = 1
for x in range(5):
    for y in range(5):

        buttons.append(LockButton(x * 50 + 10, y * 50 + 10, pen, num=button_id))
        button_id += 1


while pen.is_running:
    pen.background(255)

    # --- draw lock pattern ---
    pen.fill(0)
    for i, c in enumerate(attempt_button_coords):
        try:
            pen.stroke_size(5)
            pen.stroke(pen.color["green"])
            pen.line(
                c[0] + 10,
                c[1] + 10,
                attempt_button_coords[i + 1][0] + 10,
                attempt_button_coords[i + 1][1] + 10,
            )
        except Exception as e:
            pass

    # --- draw last part of pattern ---
    try:
        pen.line(
            attempt_button_coords[-1][0] + 10,
            attempt_button_coords[-1][1] + 10,
            pen.mouseX(),
            pen.mouseY(),
        )
    except:
        pass

    # --- display lock buttons ---
    for b in buttons:
        b.run()


    # --- if max pattern length ---
    if len(attempt_button_coords) >= 7:

        if attempt_button_ids == pattern:
            display_win = True

        attempt_button_coords = []
        attempt_button_ids = []

    # --- right password found ---
    if display_win:
        pen.fill((200, 200, 50))
        pen.font_size(30)
        pen.text("Right password!", 300, 50)

    reset_button.update()

    pen.flip_display()
    pen.event_loop()
