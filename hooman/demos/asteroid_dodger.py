import random
import pygame
from hooman import Hooman

# Initialize pygame
pygame.init()

# Setup game window and game variables
width, height = 600, 600
hapi = Hooman(width, height)
spaceship_x = width // 2
spaceship_speed = 5
asteroids = []
score = 0
game_over = False

# Clock for frame rate
clock = pygame.time.Clock()
fps = 30

# Spaceship dimensions
spaceship_width = 50
spaceship_height = 30

# Function to add asteroids
def add_asteroid():
    asteroid_size = random.randint(20, 50)
    asteroid_x = random.randint(0, width - asteroid_size)
    asteroids.append([asteroid_x, -asteroid_size, asteroid_size])

# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    # Move spaceship
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        spaceship_x -= spaceship_speed
    if keys[pygame.K_RIGHT]:
        spaceship_x += spaceship_speed
    
    # Keep spaceship in window bounds
    spaceship_x = max(0, min(spaceship_x, width - spaceship_width))
    
    # Add and move asteroids
    if random.randint(1, 30) == 1:  # Adjust the probability as needed
        add_asteroid()
    for asteroid in asteroids:
        asteroid[1] += 3  # Adjust speed as needed
        
    # Collision detection
    for asteroid in asteroids:
        if (asteroid[1] + asteroid[2] > height - spaceship_height and
            asteroid[0] < spaceship_x + spaceship_width and
            asteroid[0] + asteroid[2] > spaceship_x):
            game_over = True
    
    # Remove off-screen asteroids
    asteroids = [ast for ast in asteroids if ast[1] <= height]
    
    # Draw everything
    hapi.background(0)
    hapi.fill(hapi.color['white'])
    for asteroid in asteroids:
        hapi.ellipse(asteroid[0], asteroid[1], asteroid[2], asteroid[2])
    hapi.fill(hapi.color['blue'])
    hapi.rect(spaceship_x, height - spaceship_height, spaceship_width, spaceship_height)
    
    # Update the display
    hapi.flip_display()
    score += 1  # Increase score
    hapi.text(f"Score: {score}", 10, 10)
    
    # Limit the frame rate
    clock.tick(fps)

# Quit the game
pygame.quit()
