import random
import pygame
from hooman import Hooman

# Initialize pygame and hooman
pygame.init()

# Setup game window and variables
width, height = 600, 400
hapi = Hooman(width, height)
submarine_x, submarine_y = width // 2, height // 2
submarine_speed = 5
trash = []
hazards = []
score = 0
level = 1
game_over = False

# Clock for frame rate
clock = pygame.time.Clock()
fps = 30

# Submarine dimensions
submarine_width = 40
submarine_height = 20

# Colors
dark_blue = (11, 57, 84)  # Dark blue background to represent the ocean
light_blue = (167, 199, 231)  # Light blue color for the submarine
green_color = (189, 198, 103)  # Greenish color for the trash
red_color = (255, 107, 107)  # Red color for the hazards

# Function to add trash
def add_trash():
    trash_x = random.randint(0, width)
    trash_y = random.randint(0, height)
    trash_size = 10
    trash.append([trash_x, trash_y, trash_size])

# Function to add hazards
def add_hazard():
    hazard_x = random.randint(0, width)
    hazard_y = 0  # Start at the top of the screen
    hazard_size = random.randint(20, 40)
    hazards.append([hazard_x, hazard_y, hazard_size])

# Main game loop
while not game_over:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Submarine movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        submarine_x -= submarine_speed
    if keys[pygame.K_RIGHT]:
        submarine_x += submarine_speed
    if keys[pygame.K_UP]:
        submarine_y -= submarine_speed
    if keys[pygame.K_DOWN]:
        submarine_y += submarine_speed

    # Keep submarine within the screen bounds
    submarine_x = max(0, min(submarine_x, width - submarine_width))
    submarine_y = max(0, min(submarine_y, height - submarine_height))

    # Add trash and hazards
    if random.randint(1, 100) <= level:  # Increase probability as level increases
        add_trash()
    if random.randint(1, 200) <= level:  # Increase probability as level increases
        add_hazard()

    # Move hazards down
    for hazard in hazards:
        hazard[1] += level  # Move faster as the level increases

    # Check for submarine collision with trash
    for item in trash[:]:
        if submarine_x < item[0] + item[2] and submarine_x + submarine_width > item[0] and \
           submarine_y < item[1] + item[2] and submarine_y + submarine_height > item[1]:
            trash.remove(item)
            score += 10  # Increase score

    # Check for submarine collision with hazards
    for hazard in hazards[:]:
        if submarine_x < hazard[0] + hazard[2] and submarine_x + submarine_width > hazard[0] and \
           submarine_y < hazard[1] + hazard[2] and submarine_y + submarine_height > hazard[1]:
            game_over = True

    # Remove off-screen hazards
    hazards = [hz for hz in hazards if hz[1] < height]

    # Increase level over time
    if score > 0 and score % 100 == 0:
        level += 1

    # Drawing
    hapi.background(dark_blue)
    # Draw submarine
    hapi.fill(light_blue)
    hapi.rect(submarine_x, submarine_y, submarine_width, submarine_height)
    # Draw trash
    hapi.fill(green_color)
    for item in trash:
        hapi.rect(item[0], item[1], item[2], item[2])
    # Draw hazards
    hapi.fill(red_color)
    for hazard in hazards:
        hapi.ellipse(hazard[0], hazard[1], hazard[2], hazard[2])

    # Update the display
    hapi.flip_display()
    score += 1  # Increase score
    hapi.text(f"Score: {score}", 10, 10)

    # Limit the frame rate
    clock.tick(fps)

# Quit the game
pygame.quit()
