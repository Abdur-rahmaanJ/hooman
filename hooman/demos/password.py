from hooman import Hooman
from hooman.formula import distance

import pygame

pen = Hooman(500, 500)

coords = []
bids = []
buttons = []


class B:
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
        global coords, bids, just_ended

        if pen.pygame.mouse.get_pressed()[0]:

            if distance(self.coords(), (pen.mouseX(), pen.mouseY())) <= 20:
                if self.coords() not in coords:
                    if just_ended:
                        just_ended = False
                    else:
                        bids.append(self.num)
                        coords.append(self.coords())

    def run(self):
        self.update()
        self.draw()


bid = 1
for x in range(5):
    for y in range(5):

        buttons.append(B(x * 50 + 10, y * 50 + 10, pen, num=bid))
        bid += 1

display_win = False
just_ended = False

while pen.is_running:
    pen.background(255)

    pen.fill(0)

    for i, c in enumerate(coords):
        try:
            pen.stroke_size(5)
            pen.stroke(pen.color["green"])
            pen.line(c[0] + 10, c[1] + 10, coords[i + 1][0] + 10, coords[i + 1][1] + 10)
        except Exception as e:
            pass
            # print(coords, e)

    try:
        pen.line(coords[-1][0] + 10, coords[-1][1] + 10, pen.mouseX(), pen.mouseY())
    except:
        pass

    for b in buttons:
        b.run()

    if len(coords) >= 7:
        try:
            pen.stroke(pen.color["red"])
            pen.line(coords[-1][0] + 10, coords[-1][1] + 10, pen.mouseX(), pen.mouseY())
        except:
            pass

        if bids == [1, 2, 3, 4, 5, 6, 7]:
            display_win = True
            just_ended = True
        coords = []
        bids = []

    if display_win:

        pen.fill((200, 200, 50))
        pen.font_size(30)
        pen.text("Right password!", 300, 10)

    pen.flip_display()
    pen.event_loop()
