ripple graph

![](https://github.com/Abdur-rahmaanJ/hooman/raw/master/assets/ripple_graph.gif)

```python
"""
Author: Abdur-Rahmaan Janhangeer
Github: https://github.com/Abdur-RahmaanJ
hooman: 0.9.3
"""

from hooman import Hooman

hapi = Hooman(500, 500)



data = {"x": 10, "y": 20, "z": 30, "a": 40, "b": 50, "c": 60, "d": 70, "e": 80}
ripple_graph = hapi.ripple_graph(80, 10, 300, data, 100) # x y size range
sliders = []

# --- initialise sliders corresponding to graph values ---
for i, d in enumerate(ripple_graph.data):
    s = hapi.slider(
        10,
        300 + (i * 25),
        100,
        5,
        {"curve": 1, "background_color": ripple_graph.cols[i], "range": [0, ripple_graph.val_range]},
    )
    s.set_value(ripple_graph.data[d])
    sliders.append([s, d])


def sketch_pad():
    global ripple_graph, sliders
    hapi.background((255, 255, 255))

    hapi.fill(hapi.color["black"])
    hapi.font_size(40)

    ripple_graph.draw()

    for i, s in enumerate(sliders):
        slider = s[0]
        data_key = s[1]

        slider.update()
        ripple_graph.data[data_key] = slider.value() # modify value

        text = f"{data_key} {slider.value()} / {round(ripple_graph.val_range, 2)}"
        hapi.font_size(15)

        hapi.text(text, slider.x + slider.w, slider.y + 10)

    hapi.flip_display()
    hapi.event_loop()


if __name__ == "__main__":
    while hapi.is_running:
        sketch_pad()
else:
    print(__name__)
```