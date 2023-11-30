import random
import pygame
from hooman import Hooman

# Initialize hooman
pygame.init()
window_width, window_height = 800, 600  # Set your desired window dimensions
hapi = Hooman(window_width, window_height)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
letters = []
speed = 1
score = 0
font_size = 30
game_over = False

font_size = 40 
score_font_size = 30

# Setup the font for rendering text
font = pygame.font.SysFont('Arial', font_size)
score_font = pygame.font.SysFont('Arial', score_font_size)

# Function to add a new letter
def add_letter():
    # letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # x = random.randint(0, hapi.WIDTH - font_size)
    # y = 0  # Start at the top
    # letters.append({'letter': letter, 'x': x, 'y': y})
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  # Include numbers
    char = random.choice(chars)
    x = random.randint(0, hapi.WIDTH - font_size)
    y = 0
    letters.append({'letter': char, 'x': x, 'y': y})

# Main game loop
while hapi.is_running and not game_over:
    hapi.background(WHITE)
    hapi.event_loop()
    
    # Add a new letter at random intervals
    if random.randint(1, 30) == 1:  # Adjust the frequency as needed
        add_letter()

    # Draw the letters
    for letter_info in letters:
        letter_info['y'] += speed  # Move the letter down
        # hapi.text(letter_info['letter'], letter_info['x'], letter_info['y'], size=font_size, color=BLACK)
        hapi.fill((255, 0, 0))
        # hapi.text(letter_info['letter'], letter_info['x'], letter_info['y'])
        text_surface = font.render(letter_info['letter'], True, (255, 0, 0))
        hapi.screen.blit(text_surface, (letter_info['x'], letter_info['y'])) 


    # Check for game over
    for letter_info in letters:
        if letter_info['y'] > hapi.HEIGHT:
            game_over = True

    
    # Handle key presses
    keys = pygame.key.get_pressed()
    for i in range(len(pygame.key.get_pressed())):
        if keys[i] == 1:
            char = pygame.key.name(i).upper()
            for letter_info in letters:
                if letter_info['letter'] == char:
                    letters.remove(letter_info)
                    score += 1
                    break  # Break to only remove one letter at a time
    
    # Display the score
    # hapi.text(f"Score: {score}", 10, 10, size=font_size, color=BLACK)
    # hapi.text(f"Score: {score}", 10, 10)
    score_surface = score_font.render(f"Score: {score}", True, (0, 0, 0))  # Black color
    hapi.screen.blit(score_surface, (10, 10))



    # Update the game display and tick
    hapi.flip_display()
    hapi.clock.tick(30)

# End the game
pygame.quit()