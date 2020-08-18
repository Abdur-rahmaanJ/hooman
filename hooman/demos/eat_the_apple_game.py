"""
Author: Maxime Coene
Github: https://github.com/macoene
"""

from hooman import Hooman

import pygame
import random

hapi = Hooman(500, 500)


def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False


hapi.handle_events = handle_events

apple = (random.randint(10, (hapi.WIDTH - 10)), random.randint(10, (hapi.HEIGHT - 10)))
score = 0

while hapi.is_running:
    hapi.background((50, 50, 50))

    hapi.no_stroke()
    mx = (hapi.mouseX() / hapi.WIDTH) * 255

    if hapi.mouseX() < (apple[0] - 24):
        hapi.fill(hapi.color["green"])
        hapi.ellipse((hapi.mouseX() - 15), (hapi.mouseY() - 25), 50, 50)

    if hapi.mouseX() > (apple[0] + 24):
        hapi.fill(hapi.color["green"])
        hapi.ellipse((hapi.mouseX() - 35), (hapi.mouseY() - 25), 50, 50)

    if hapi.mouseY() < (apple[1] - 24):
        hapi.fill(hapi.color["green"])
        hapi.ellipse((hapi.mouseX() - 25), (hapi.mouseY() - 15), 50, 50)

    if hapi.mouseY() > (apple[1] + 24):
        hapi.fill(hapi.color["green"])
        hapi.ellipse((hapi.mouseX() - 25), (hapi.mouseY() - 35), 50, 50)
    
    hapi.fill((255, 255, 255))
    hapi.ellipse((hapi.mouseX() - 25), (hapi.mouseY() - 25), 50, 50)

    hapi.fill(hapi.color["red"])
    hapi.text(score, 5, 5)

    if (hapi.mouseX() < (apple[0] + 24)) and (hapi.mouseX() > (apple[0] - 24)) and (hapi.mouseY() < (apple[1] + 24)) and (hapi.mouseY() > (apple[1] - 24)):
        hapi.fill(hapi.color["red"])
        hapi.ellipse((apple[0] - 5), (apple[1] - 5), 10, 10)

    if (hapi.mouseX() < (apple[0] + 9)) and (hapi.mouseX() > (apple[0] - 9)) and (hapi.mouseY() < (apple[1] + 9)) and (hapi.mouseY() > (apple[1] - 9)):
        apple = (random.randint(10, (hapi.WIDTH - 10)), random.randint(10, (hapi.HEIGHT - 10)))
        score += 1

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()