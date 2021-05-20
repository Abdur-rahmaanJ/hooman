from hooman import Hooman
from math import pow
from math import sqrt
import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)


def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False


hapi.handle_events = handle_events

while hapi.is_running:
    hapi.background(bg_col)

    hapi.stroke(hapi.color["red"])
    hapi.stroke_size(2)

    mouse_coord = (hapi.mouseX(), hapi.mouseY())
    hapi.cross_hair(mouse_coord)

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()
