from hooman import Hooman

import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)

text_box_options = {"background_color": hapi.color["light_grey"], "max_lines": 3}

text_box = hapi.text_box(100, 100, 300, 40, text_box_options)


def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        text_box.key_down(event)
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False


hapi.handle_events = handle_events

while hapi.is_running:
    hapi.background(bg_col)

    text_box.update()

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()
