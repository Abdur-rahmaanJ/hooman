from hooman import Hooman
import time



window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)


time.sleep(10)

mouse_x = {
                "label": "mouse x",
                "color": (0, 255, 0),
                "data": [[1,1]]
            }


mouse_y = {
                "label": "mouse y",
                "color": (255, 0, 0),
                "data": [[1,1]]
            }

time_unit = 0


def max_data(data, index):
    a = []
    for d in data:
        a.append(d[index])

    return max(a)


while hapi.is_running:
    bg_col = (255, 255, 255)
    hapi.background(bg_col)

    max_range_y = max([max_data(mouse_y['data'], 1), max_data(mouse_x['data'], 1)])

    hapi.linechart(
        40,
        30,
        300,
        200,
        {
            "lines":[
            mouse_x,
            mouse_y],
            "mouse_line": False,
            "range_y": [0, max_range_y],
            "range_x": [0, max_data(mouse_x['data'], 0)],
        },
    )
    hapi.fill(hapi.color["blue"])

    mouse_x['data'].append([time_unit, hapi.mouseX()])
    mouse_y['data'].append([time_unit, hapi.mouseY()])

    time_unit += 1
    hapi.flip_display()
    hapi.event_loop()
