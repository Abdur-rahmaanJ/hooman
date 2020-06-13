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

while hapi.is_running:
    hapi.background((255, 255, 255))

    hapi.no_stroke()
    mx = (hapi.mouseX() / hapi.WIDTH) * 255

    hapi.fill((0, mx, 0))
    for i in range(50, 200, 60):
        hapi.rect(i, 50, 30, 30)

    hapi.fill((255, 0, 0))
    hapi.ellipse(hapi.mouseX(), hapi.mouseY(), 10, 10)

    hapi.stroke_size(1)
    hapi.stroke((255, 10, 10))
    hapi.line(0, hapi.mouseY(), hapi.mouseX() - 10, hapi.mouseY())

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()
