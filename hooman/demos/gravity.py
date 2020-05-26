from hooman import Hooman

import pygame

window_width, window_height = 800, 800
hapi = Hooman(window_width, window_height)

rect_x, rect_y = 100, 100
rect_w, rect_h = 100, 100
dy = 0
gravity_acceleration = 1
jump_strength = 20

def handle_events(event):
    global dy
    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False
        if event.key == pygame.K_SPACE:
            dy = -jump_strength

hapi.handle_events = handle_events

clock = pygame.time.Clock()

while hapi.is_running:
    hapi.background((255, 255, 255))

    hapi.event_loop()
    dy += gravity_acceleration
    rect_y += dy
    if rect_y + rect_h >= window_height:
        dy = 0
        rect_y = window_height - rect_h

    hapi.fill((0, 0, 0))
    hapi.rect(rect_x, rect_y, rect_w, rect_h)

    hapi.flip_display()

    clock.tick(60) # slows down gravity acceleration

pygame.quit()
