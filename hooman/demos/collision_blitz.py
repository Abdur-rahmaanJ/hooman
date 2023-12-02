import pygame
from hooman import Hooman
import random
import math

pygame.init()

window_width, window_height = 800, 600
hapi = Hooman(window_width, window_height)

screen = pygame.display.set_mode((window_width, window_height))

bg_color = (200, 200, 200) 

ball_radius = 20
ball_speed_x, ball_speed_y = 5, 5
ball_color = hapi.color['blue']

main_ball = {
    'x': window_width // 2,
    'y': window_height // 2,
    'speed_x': random.choice([-5, 5]),
    'speed_y': random.choice([-5, 5]),
    'radius': ball_radius
}

sec_ball = {
    'x': random.randint(0, window_width),
    'y': random.randint(0, window_height),
    'speed_x': random.choice([-3, 3]),
    'speed_y': random.choice([-3, 3]),
    'radius': ball_radius
}

score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    hapi.event_loop()

    main_ball['x'] += main_ball['speed_x']
    main_ball['y'] += main_ball['speed_y']

    sec_ball['x'] += sec_ball['speed_x']
    sec_ball['y'] += sec_ball['speed_y']

    if main_ball['x'] - main_ball['radius'] <= 0 or main_ball['x'] + main_ball['radius'] >= window_width:
        main_ball['speed_x'] = -main_ball['speed_x']
    if main_ball['y'] - main_ball['radius'] <= 0 or main_ball['y'] + main_ball['radius'] >= window_height:
        main_ball['speed_y'] = -main_ball['speed_y']

    if sec_ball['x'] - sec_ball['radius'] <= 0 or sec_ball['x'] + sec_ball['radius'] >= window_width:
        sec_ball['speed_x'] = -sec_ball['speed_x']
    if sec_ball['y'] - sec_ball['radius'] <= 0 or sec_ball['y'] + sec_ball['radius'] >= window_height:
        sec_ball['speed_y'] = -sec_ball['speed_y']

    distance = math.sqrt((main_ball['x'] - sec_ball['x']) ** 2 + (main_ball['y'] - sec_ball['y']) ** 2)
    if distance <= main_ball['radius'] + sec_ball['radius']:
        sec_ball = {
            'x': random.randint(0, window_width),
            'y': random.randint(0, window_height),
            'speed_x': random.choice([-3, 3]),
            'speed_y': random.choice([-3, 3]),
            'radius': ball_radius
        }
        score += 1

    hapi.background(bg_color)

    hapi.fill(ball_color)
    hapi.circle(main_ball['x'], main_ball['y'], main_ball['radius'])

    hapi.fill(hapi.color['red'])
    hapi.circle(sec_ball['x'], sec_ball['y'], sec_ball['radius'])

    score_text = font.render(f"Score: {score}", True, hapi.color['black'])
    hapi.screen.blit(score_text, (10, 10))

    hapi.flip_display()

    clock.tick(60)  


