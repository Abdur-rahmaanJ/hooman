from hooman import Hooman
import numpy
from math import pow
from math import sqrt
import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)




slider_options = {
    'value_range': [0, 255]
}

r_slider = hapi.slider(50, 300, 400, 10, slider_options)
g_slider = hapi.slider(50, 330, 400, 10, slider_options)
b_slider = hapi.slider(50, 360, 400, 10, slider_options)

while hapi.is_running:
    bg_col = (r_slider.value(), g_slider.value(), b_slider.value())
    hapi.background(bg_col)
    
    hapi.fill(hapi.color['blue'])
    color_text = 'r:{} g:{} b:{}'.format(r_slider.value(), g_slider.value(), b_slider.value())
    hapi.text(color_text, 20, 20)
    r_slider.update()
    g_slider.update()
    b_slider.update()
    hapi.flip_display()
    hapi.event_loop()

pygame.quit()