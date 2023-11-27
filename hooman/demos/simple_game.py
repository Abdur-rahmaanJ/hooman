import pygame
from hooman import Hooman

# Initialize Pygame and Hooman
pygame.init()
window_width, window_height = 800, 600
hapi = Hooman(window_width, window_height)

# Player variables
player_size = 50
player_x, player_y = window_width // 2, window_height // 2
player_speed = 5

def handle_events(event):
    global player_x, player_y

    if event.type == pygame.QUIT:
        hapi.is_running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False

def game_logic():
    global player_x, player_y

    keys = pygame.key.get_pressed()

    # Move the player based on arrow key inputs
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Ensure the player stays within the window bounds
    player_x = max(0, min(player_x, window_width - player_size))
    player_y = max(0, min(player_y, window_height - player_size))

# Set the event handler and game logic functions
hapi.handle_events = handle_events
hapi.game_logic = game_logic

while hapi.is_running:
    hapi.background(hapi.color["white"])

    # Draw the player character
    hapi.rect(player_x, player_y, player_size, player_size, hapi.color["blue"])

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()
