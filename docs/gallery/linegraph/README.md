line graph

![](https://github.com/Abdur-rahmaanJ/hooman/raw/master/assets/linegraph.gif)

```python
from hooman import Hooman

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)


mouse_x = {
    "label": "mouse x",
    "color": (0, 255, 0),
    "data": [[1, 1]],
    "values_window": 200,
}


mouse_y = {
    "label": "mouse y",
    "color": (255, 0, 0),
    "data": [[1, 1]],
    "values_window": 200,
}

time_unit = 0


def max_data(data, index):
    a = []
    for d in data:
        a.append(d[index])

    return max(a)


while hapi.is_running:
    bg_col = (255, 255, 255)
    hapi.background(255)

    max_range_y = max([max_data(mouse_y["data"], 1), max_data(mouse_x["data"], 1)])

    hapi.linechart(
        40,
        30,
        300,
        400,
        {
            "lines": [mouse_x, mouse_y],
            "mouse_line": False,
            "range_y": [0, max_range_y],
            "range_x": [0, max_data(mouse_x["data"], 0)],
            "show_axes": False,
            "tick_size": 10,
            "show_ticks_x": False,
            "show_ticks_y": False,
            "x_axis_label": "mouse position",
            "y_axis_label": "unit time",
        },
    )
    hapi.fill(hapi.color["blue"])

    mouse_x["data"].append([time_unit, hapi.mouseX()])
    mouse_y["data"].append([time_unit, hapi.mouseY()])


    time_unit += 1

    hapi.flip_display()
    hapi.event_loop()

```