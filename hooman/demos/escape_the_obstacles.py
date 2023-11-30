import random
import pygame
from hooman import Hooman

# Initialize pygame and hooman
pygame.init()

# Setup game window and variables
width, height = 600, 400
hapi = Hooman(width, height)
spaceship_x, spaceship_y = width // 2, height - 50
spaceship_speed = 5
asteroids = []
score = 0
game_over = False

# Clock for frame rate
clock = pygame.time.Clock()
fps = 30

# Spaceship dimensions
spaceship_width = 40
spaceship_height = 20

# Colors
dark_green = (0, 100, 0)  # Dark green background
light_blue = (173, 216, 230)  # Light blue color for the spaceship
gray_color = (169, 169, 169)  # Gray color for the asteroids

# Function to add asteroids
def add_asteroid():
    asteroid_x = random.randint(0, width)
    asteroid_y = 0  # Start at the top of the screen
    asteroid_size = random.randint(20, 40)
    asteroids.append([asteroid_x, asteroid_y, asteroid_size])

# Main game loop
while not game_over:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Spaceship movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        spaceship_x -= spaceship_speed
    if keys[pygame.K_RIGHT]:
        spaceship_x += spaceship_speed

    # Keep spaceship within the screen bounds
    spaceship_x = max(0, min(spaceship_x, width - spaceship_width))

    # Add asteroids
    if random.randint(1, 100) <= 5:  # Low probability to spawn asteroids
        add_asteroid()

    # Move asteroids down
    for asteroid in asteroids:
        asteroid[1] += 5  # Fixed speed for asteroids

    # Check for spaceship collision with asteroids
    for asteroid in asteroids[:]:
        if spaceship_x < asteroid[0] + asteroid[2] and spaceship_x + spaceship_width > asteroid[0] and \
                spaceship_y < asteroid[1] + asteroid[2] and spaceship_y + spaceship_height > asteroid[1]:
            game_over = True

    # Remove off-screen asteroids
    asteroids = [ast for ast in asteroids if ast[1] < height]

    # Drawing
    hapi.background(dark_green)
    # Draw spaceship
    hapi.fill(light_blue)
    hapi.rect(spaceship_x, spaceship_y, spaceship_width, spaceship_height)
    # Draw asteroids
    hapi.fill(gray_color)
    for asteroid in asteroids:
        hapi.ellipse(asteroid[0], asteroid[1], asteroid[2], asteroid[2])

    # Update the display
    hapi.flip_display()
    score += 1  # Increase score
    hapi.text(f"Score: {score}", 10, 10)

    # Limit the frame rate
    clock.tick(fps)

# Quit the game
pygame.quit()
