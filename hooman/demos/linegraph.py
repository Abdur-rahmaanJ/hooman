from hooman import Hooman


window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)


while hapi.is_running:
    bg_col = (255, 255, 255)
    hapi.background(bg_col)

    hapi.linechart(
        40,
        30,
        300,
        200,
        {
            "data": [[0, 0], [10, 10], [20, 20], [30, 30], [90, 20]],
            "mouse_line": True,
            "range_y": [0, 200],
            "range_x": [0, 300],
        },
    )
    hapi.fill(hapi.color["blue"])

    hapi.flip_display()
    hapi.event_loop()
