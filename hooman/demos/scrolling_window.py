from hooman import Hooman
from collections import OrderedDict
import pygame
import random

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)

scroll = hapi.scroll({'range_y': 400})

slider = hapi.slider(100, 850, 300, 30, {'curve': 0.8})

while hapi.is_running:
    hapi.background(bg_col)

    hapi.fill(hapi.color['red'])
    dy = scroll[1]
    hapi.rect(100, 600 + dy, 100, 100)
    hapi.rect(200, 400 + dy, 100, 200)

    scroll.update()
    slider.update()
    slider.Move(y=850 + dy)

    hapi.event_loop()
    hapi.flip_display()

pygame.quit()
