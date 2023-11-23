import pygame
import random

# Initialize Pygame
pygame.init()

# Initialize the window
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Collect Stars Game")

# Colors
bg_col = (0, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

# Player character
player_x, player_y = window_width // 2, window_height // 2
player_speed = 5

# Stars
num_stars = 20
stars = []

for _ in range(num_stars):
    star_x = random.randint(0, window_width)
    star_y = random.randint(0, window_height)
    stars.append((star_x, star_y))

score = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed

    # Draw the background
    window.fill(bg_col)

    # Draw and check collision with stars
    for i, (x, y) in enumerate(stars):
        pygame.draw.circle(window, yellow, (int(x), int(y)), 10)

        # Check for collision with player
        distance = ((player_x - x) ** 2 + (player_y - y) ** 2) ** 0.5
        if distance < 15:
            stars[i] = (random.randint(0, window_width), random.randint(0, window_height))
            score += 1

    # Draw player character
    pygame.draw.circle(window, blue, (player_x, player_y), 20)

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, white)
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
