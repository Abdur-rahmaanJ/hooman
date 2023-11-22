from hooman import Hooman
import pygame
import math

# Initialize Hooman
window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)

# Square
square_size = 50
square_x, square_y = window_width // 2, window_height // 2
rotation_angle = 0
rotation_speed = 2
square_color = (128, 0, 128)

# Trail
trail_length = 10
trail_positions = []

# Set the desired frames per second (fps)
fps = 60
clock = pygame.time.Clock()

def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False

hapi.handle_events = handle_events

while hapi.is_running:
    hapi.background(bg_col)

    # Update square position and rotation
    rotation_angle += rotation_speed
    if rotation_angle >= 360:
        rotation_angle = 0

    # Add current position to trail
    trail_positions.append((square_x, square_y))
    if len(trail_positions) > trail_length:
        trail_positions.pop(0)

    # Draw trail
    for i, (x, y) in enumerate(trail_positions):
        alpha = int(255 * (1 - i / trail_length))
        hapi.fill(square_color[0], square_color[1], square_color[2])
        hapi.set_alpha(alpha)
        hapi.rect(x - square_size // 2, y - square_size // 2, square_size, square_size)
        hapi.set_alpha(255)

    # Draw rotating square
    hapi.rotate(rotation_angle)
    hapi.fill(square_color)
    hapi.rect(square_x - square_size // 2, square_y - square_size // 2, square_size, square_size)
    hapi.rotate(-rotation_angle)

    # Update display and handle events
    hapi.flip_display()
    hapi.event_loop()

    # Control frame rate
    clock.tick(fps)

pygame.quit()
