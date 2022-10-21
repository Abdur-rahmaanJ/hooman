"""
Author: Abdur-Rahmaan Janhangeer
Github: https://github.com/Abdur-rahmaanJ
"""

from hooman import Hooman

import pygame

hapi = Hooman(500, 500)


def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False


hapi.handle_events = handle_events


def sketch_pad():
    # hapi.background((255, 255, 255))

    # hapi.font_size(15)
    # hapi.text(f'{hapi.mouseX()}, {hapi.pmouseX()}', 10, 10)

    hapi.fill(100)

    hapi.stroke_size(5)
    hapi.stroke(100)
    hapi.line(hapi.pmouseX(), hapi.pmouseY(), hapi.mouseX(), hapi.mouseY())

    hapi.flip_display()
    hapi.event_loop()

while hapi.is_running:
    sketch_pad()

pygame.quit()
