from hooman import Hooman

import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)



while hapi.is_running:
    hapi.background(bg_col)

    hapi.fill(hapi.color["red"])
    hapi.fill_arc(hapi.center_x, hapi.center_y, 100, 0, 90, start_rad=30)
    hapi.fill(hapi.color["blue"])
    hapi.fill_arc(hapi.center_x, hapi.center_y, 100, 90, 180, start_rad=30)
    hapi.fill(hapi.color["green"])
    hapi.fill_arc(hapi.center_x, hapi.center_y, 100, 180, 270, start_rad=30)
    hapi.fill(hapi.color["black"])
    hapi.fill_arc(hapi.center_x, hapi.center_y, 100, 270, 0, start_rad=30)

    hapi.event_loop()
    hapi.flip_display()

pygame.quit()
