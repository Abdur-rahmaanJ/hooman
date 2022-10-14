"""
Author: Abdur-Rahmaan Janhangeer
Github: https://github.com/Abdur-RahmaanJ
hooman: 0.9.3
"""

from hooman import Hooman
import pygame

hapi = Hooman(500, 500)


class ConcentricCircleGraph:
    def __init__(self, hapi, x, y, size, data: dict, val_range: list):
        self.x = x
        self.y = y
        self.size = size
        self.data = data
        self.val_range = val_range
        self.cols = []

        # --- have fixed colors for circles ---
        for i in self.data:
            col = next(hapi.candy_colors_list)
            self.cols.append(col)

    def draw(self):
        arc_wid_s = self.size
        arc_wid_x = self.x
        arc_wid_y = self.y

        i = -1
        for key in self.data: # {'x':1}
            i += 1
            d = self.data[key]

            hapi.stroke_size(5)

            end_rad = (d / self.val_range) * (hapi.PI * 2)

            a_size = arc_wid_s - (i * 30)
            pad = (arc_wid_s - a_size) // 2

            # --- background arc ---
            hapi.stroke(hapi.colors['candy_gray'])
            hapi.arc(
                arc_wid_x + pad,
                arc_wid_y + pad,
                a_size,
                a_size,
                0 + (1.5 * hapi.PI),
                hapi.PI * 2 + (1.5 * hapi.PI),
            )

            # --- colored arc ---
            hapi.stroke(self.cols[i])
            hapi.arc(
                arc_wid_x + pad,
                arc_wid_y + pad,
                a_size,
                a_size,
                0 + (1.5 * hapi.PI),
                end_rad + (1.5 * hapi.PI),
            )


data = {"x": 10, "y": 20, "z": 30, "a": 40, "b": 50, "c": 60, "d": 70, "e": 80}
cs = ConcentricCircleGraph(hapi, 80, 10, 300, data, 100)
sliders = []

# --- initialise sliders corresponding to graph values ---
for i, d in enumerate(cs.data):
    s = hapi.slider(
        10,
        300 + (i * 25),
        100,
        5,
        {"curve": 1, "background_color": cs.cols[i], "range": [0, cs.val_range]},
    )
    s.set_value(cs.data[d])
    sliders.append([s, d])


def sketch_pad():
    global cs, sliders
    hapi.background((255, 255, 255))

    hapi.fill(hapi.color["black"])
    hapi.font_size(40)

    cs.draw()

    for i, s in enumerate(sliders):
        slider = s[0]
        data_key = s[1]

        slider.update()
        cs.data[data_key] = slider.value() # modify value

        text = f"{data_key} {slider.value()}/ {round(cs.val_range, 2)}"
        hapi.font_size(15)

        hapi.text(text, slider.x + slider.w, slider.y + 10)

    hapi.flip_display()
    hapi.event_loop()


if __name__ == "__main__":
    while hapi.is_running:
        sketch_pad()
else:
    print(__name__)
