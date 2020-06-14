from hooman import Hooman
from collections import OrderedDict
import pygame
import random

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)



while hapi.is_running:
    hapi.background(bg_col)

    hapi.piechart(100, 100, 50, [
        ['a', 20, hapi.color['red']],
        ['b', 30, hapi.color['blue']],
        ['c', 40, hapi.color['yellow']],
        ['d', 60, hapi.color['green']],
        ['e', 30, hapi.color['black']]
    ], start_rad=20)

    hapi.barchart(
        190, 30, 200, 200, {
        "data": {"a": 10, "b": 20, "c": 90}, 
        "mouse_line": True
        }
    )

    hapi.linechart(
        30,
        270,
        200,
        100,
        {
            "data": [[0, 0], [100, 100], [200, 20], [300, 200]],
            "mouse_line": True,
            "range_y": [0, 200],
            "range_x": [0, 300],
        },
    )

    hapi.event_loop()
    hapi.flip_display()

pygame.quit()
