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

clock = pygame.time.Clock()

while hapi.is_running:
    hapi.background(bg_col)
    
    hapi.fill(hapi.color['red'])
    n1 = (hapi.mouseX()/hapi.WIDTH) * 1
    smooth_star = {
        'n1':n1,
        'n2':1.7,
        'n3':1.7,
        'm': 5,
        'a':1,
        'b':1,
        'phi':2
    }
    hapi.text(n1, 10+hapi.mouseX(), 10+hapi.mouseY())
    hapi.supershape(200, 200, 200, 200, smooth_star)

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()