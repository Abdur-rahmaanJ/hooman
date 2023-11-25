from hooman import Hooman
import pygame
import random

# Initialize Hooman
window_width, window_height = 800, 600
hapi = Hooman(window_width, window_height)

bg_col = (0, 0, 0)

# Spaceship
spaceship_size = 50
spaceship_x = window_width // 2 - spaceship_size // 2
spaceship_y = window_height - 2 * spaceship_size
spaceship_speed = 5

# Bullets
bullet_size = 5
bullet_speed = 7
bullets = []

# Asteroids
asteroid_size = 30
asteroid_speed = 3
asteroids = []

fps = 60

def handle_events(event):
    global spaceship_x

    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False
        if event.key == pygame.K_SPACE:
            # Shoot a bullet
            bullets.append((spaceship_x + spaceship_size // 2, spaceship_y))

    # Move spaceship with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship_x > 0:
        spaceship_x -= spaceship_speed
    if keys[pygame.K_RIGHT] and spaceship_x < window_width - spaceship_size:
        spaceship_x += spaceship_speed

hapi.handle_events = handle_events

while hapi.is_running:

    hapi.background(bg_col)

    # Draw spaceship
    hapi.fill(255, 0, 0)  # Red spaceship
    hapi.rect(spaceship_x, spaceship_y, spaceship_size, spaceship_size)

    # Draw bullets
    for i, (bullet_x, bullet_y) in enumerate(bullets):
        hapi.fill(0, 255, 0)  # Green bullets
        hapi.rect(bullet_x, bullet_y, bullet_size, bullet_size)

        # Move bullets up the screen
        bullets[i] = (bullet_x, bullet_y - bullet_speed)

        # Remove bullets that go off-screen
        if bullet_y < 0:
            bullets.pop(i)

    # Draw asteroids
    for i, (asteroid_x, asteroid_y) in enumerate(asteroids):
        hapi.fill(255, 255, 255)  # White asteroids
        hapi.rect(asteroid_x, asteroid_y, asteroid_size, asteroid_size)

        # Move asteroids down the screen
        asteroids[i] = (asteroid_x, asteroid_y + asteroid_speed)

        # Remove asteroids that go off-screen
        if asteroid_y > window_height:
            asteroids.pop(i)

    # Add new asteroids randomly
    if random.random() < 0.02:
        asteroids.append((random.randint(0, window_width - asteroid_size), -asteroid_size))

    # Check for collisions with asteroids
    for (asteroid_x, asteroid_y) in asteroids:
        for (bullet_x, bullet_y) in bullets:
            if (
                bullet_x < asteroid_x + asteroid_size
                and bullet_x + bullet_size > asteroid_x
                and bullet_y < asteroid_y + asteroid_size
                and bullet_y + bullet_size > asteroid_y
            ):
                # Remove the bullet and asteroid on collision
                bullets.remove((bullet_x, bullet_y))
                asteroids.remove((asteroid_x, asteroid_y))

    # Update display and handle events
    hapi.flip_display()
    hapi.event_loop()

    # FPS limiter
    hapi.clock.tick(fps)

pygame.quit()

