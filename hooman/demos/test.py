from hooman import Hooman

import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)


def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False


hapi.handle_events = handle_events

clock = pygame.time.Clock()

hapi.set_background(hapi.color["white"])

while hapi.is_running:

    hapi.fill(100)
    hapi.stroke(0)
    hapi.stroke_size(4)
    hapi.regular_polygon(100, 200, 50, 50, hapi.mouseX() // 50)
    hapi.rotate(hapi.mouseY() // 2)

    hapi.event_loop()

    hapi.flip_display()

    clock.tick(60)

pygame.quit()
