from hooman import Hooman

import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)

start_options = {
    "background_color": hapi.color["grey"],
    "slider_color": (200, 200, 200),
    "value_range": [0, 360],
    "starting_value": 0,
}
end_options = {
    "background_color": hapi.color["grey"],
    "slider_color": (200, 200, 200),
    "value_range": [0, 360],
    "starting_value": 90,
}

start_angle = hapi.slider(50, 400, 400, 20, start_options)
end_angle = hapi.slider(50, 430, 400, 20, end_options)

while hapi.is_running:
    hapi.background(bg_col)

    hapi.fill(hapi.color["red"])
    hapi.fill_arc(hapi.center_x, hapi.center_y, 100, start_angle.value(), end_angle.value(), start_rad=30)
    hapi.text('{}-{}'.format(start_angle.value(), end_angle.value()), 50, 450)

    start_angle.update()
    end_angle.update()
    hapi.event_loop()
    hapi.flip_display()

pygame.quit()
