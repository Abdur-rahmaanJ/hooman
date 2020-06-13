from hooman import Hooman


window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)


while hapi.is_running:
    bg_col = (255, 255, 255)
    hapi.background(bg_col)

    hapi.barchart(
        30, 30, 200, 200, {"data": {"a": 10, "b": 20, "c": 90}, "mouse_line": True}
    )
    # hapi.text(hapi.mouseX(), 200, 200)
    hapi.flip_display()
    hapi.event_loop()
