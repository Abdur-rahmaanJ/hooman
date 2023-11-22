# demo_starfield.py
from hooman import Hooman
import pygame
import random

# Initialize Hooman
window_width, window_height = 800, 600
hapi = Hooman(window_width, window_height)

bg_col = (0, 0, 0)

# Starfield
num_stars = 100
stars = []

for _ in range(num_stars):
    star_x = random.randint(0, window_width)
    star_y = random.randint(0, window_height)
    star_speed = random.uniform(1, 5)
    stars.append((star_x, star_y, star_speed))

def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False

hapi.handle_events = handle_events

while hapi.is_running:
    
    hapi.background(bg_col)

    # Update and draw stars
    for i, (x, y, speed) in enumerate(stars):
        hapi.fill(255)  # White stars
        hapi.circle(int(x), int(y), 2)

        # Move stars diagonally
        stars[i] = (x + speed, y + speed, speed)

        # Reset stars that go off-screen
        if x > window_width or y > window_height:
            stars[i] = (0, 0, speed)

    # Update display and handle events
    hapi.flip_display()
    hapi.event_loop()

pygame.quit()