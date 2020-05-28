'''
Author: Abdur-Rahmaan Janhangeer
Github: https://github.com/Abdur-rahmaanJ
'''

from hooman import Hooman

import pygame

hapi = Hooman(500, 500)

def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False

hapi.handle_events = handle_events

while hapi.is_running:
    hapi.background((255, 255, 255))

    start = (hapi.mouseY() / hapi.HEIGHT) * hapi.PI
    end = (hapi.mouseX() / hapi.WIDTH) * hapi.PI
    hapi.fill(hapi.color['blue'])
    hapi.stroke_size(4)
    hapi.arc(10, 10, 200, 200, start, end)

    hapi.begin_shape()
    hapi.vertex((0, 0))
    hapi.vertex((100, 0))
    hapi.vertex((hapi.mouseX(), hapi.mouseY()))
    hapi.end_shape()

    hapi.polygon([(10, 10), (100, 100), (10, 200)])

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()
