from hooman import Hooman
import numpy
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


def fake_slider(pos, x, y, width):
    size = 10
    hapi.fill(hapi.color['grey'])
    hapi.rect(x, y, width, size)
    hapi.fill((200, 200, 200))
    hapi.rect(pos, y, size, size)

while hapi.is_running:
    hapi.background(bg_col)
    
    fake_slider(hapi.mouseX(), 0, 450, hapi.WIDTH)

    reflected_val = hapi.constrain(hapi.mouseX(), 0, 500, 0, 255)
    reflected_col = (reflected_val, reflected_val, reflected_val)
    hapi.fill(reflected_col)
    hapi.rect(10, 10, 100, 100)

    reflected_val2 = hapi.constrain(hapi.mouseX(), 0, 500, 100, 200)
    fake_slider(reflected_val2, 100, 200, 100)

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()