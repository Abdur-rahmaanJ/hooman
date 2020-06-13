from hooman import Hooman

import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

red_blue = hapi.gradient(300, 30, hapi.color['blue'], hapi.color['red']).convert()

<<<<<<< Updated upstream


slider_options = {
    'value_range': [0, 255]
}

r_slider = hapi.slider(50, 300, 400, 10, slider_options)
g_slider = hapi.slider(50, 330, 400, 10, slider_options)
b_slider = hapi.slider(50, 360, 400, 10, slider_options)

while hapi.is_running:
    bg_col = (r_slider.value(), g_slider.value(), b_slider.value())
    hapi.background(bg_col)
    
    hapi.fill(hapi.color['blue'])
    color_text = 'r:{} g:{} b:{}'.format(r_slider.value(), g_slider.value(), b_slider.value())
    hapi.text(color_text, 20, 20)
    r_slider.update()
    g_slider.update()
    b_slider.update()
=======
green_blue = hapi.gradient(300, 30, hapi.color['green'], hapi.color['blue']).convert()

yellow_black = hapi.gradient(300, 30, hapi.color['yellow'], hapi.color['black']).convert()

black_white = hapi.gradient(300, 30, hapi.color['black'], hapi.color['white']).convert()

slider = hapi.slider(100, 300, 300, 30,
                     {'image': red_blue,
                      'slider_height': 60,
                      'value_range': [0, 255]}
                     )

color_slider = hapi.slider(150, 400, 200, 20,
                           {'slider_height': 40,
                            'value_range': [0, 3],
                            'step': 1,
                            'starting_value': 0}
                           )

slider = hapi.slider_with_text(slider, 
                               {'pivot': 'top',
                                'padding_y': 12}
                               )

def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False


hapi.handle_events = handle_events

clock = pygame.time.Clock()

while hapi.is_running:
    if color_slider.value() == 0:
        hapi.background((slider.value(), 0, 255 - slider.value()))
        slider.image = red_blue
    elif color_slider.value() == 1:
        hapi.background((0,255 - slider.value(), slider.value()))
        slider.image = green_blue
    elif color_slider.value() == 2:
        hapi.background((255 - slider.value(), 255 - slider.value(), 0))
        slider.image = yellow_black
    elif color_slider.value() == 3:
        hapi.background(slider.value())
        slider.image = black_white

    slider.update()
    color_slider.update()

    hapi.event_loop()

>>>>>>> Stashed changes
    hapi.flip_display()

    clock.tick(60)

pygame.quit()
