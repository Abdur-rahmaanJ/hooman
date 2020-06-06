from hooman import Hooman
import numpy
from math import pow
from math import sqrt
import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)


slider_options = {
    'background_color': hapi.color['grey'],
    'slider_color': (200, 200, 200),
    'value_range': [100, 200]
}

real_slider = hapi.slider(50, 300, 400, 30, slider_options)

while hapi.is_running:
    hapi.background(bg_col)
    
    hapi.fill(hapi.color['blue'])
    hapi.text(real_slider.value(), 10, 10)

    real_slider.update()
    hapi.flip_display()
    hapi.event_loop()

pygame.quit()