"""
Author: Vinícius Romano
Github: https://github.com/romavini
"""

from hooman import Hooman
import pygame

hapi = Hooman(500, 500)

bg_col = (255, 255, 255)

grey_button = {
    "background_color": (200, 200, 200),
    "hover_background_color": (220, 220, 220),
    "curve": 0.1,
    "padding_x": 5,
    "padding_y": 5,
    "font_size": 15,
}


def check_click():
    if (
        (button.x + button.w > hapi.mouseX() > button.x)
        and (button.y + button.h > hapi.mouseY() > button.y)
        and pygame.mouse.get_pressed()[0] == True
    ):
        return True
    else:
        return False


def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False
    elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
        hapi.is_running = False


hapi.handle_events = handle_events

button = hapi.button(150, 150, 180, 100, "Click me and hold!", grey_button)

while hapi.is_running:
    hapi.background(bg_col)

    mouse_coord = (hapi.mouseX(), hapi.mouseY())

    button.update()
    if check_click():
        bg_col = (255, 0, 0)
    else:
        bg_col = (255, 255, 255)

    hapi.set_background(bg_col)
    hapi.flip_display()
    hapi.event_loop()

pygame.quit()
