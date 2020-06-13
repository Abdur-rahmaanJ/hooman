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

size = 50
while hapi.is_running:
    hapi.background((255, 255, 255))

    hapi.no_stroke()
    hapi.fill((0, 255, 0))
    hapi.rect(10, 10, size, size)
    hapi.fill((255, 255, 0))
    hapi.rect(100, 100, size, size)
    hapi.fill((255, 0, 0))
    hapi.rect(100, 10, size, size)
    hapi.fill((0, 0, 255))
    hapi.rect(10, 100, size, size)

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()
