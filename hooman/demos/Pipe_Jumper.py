import pygame
from hooman import Hooman
import random

pygame.init()
hapi = Hooman(400, 600)


player_size = 50
player_color = hapi.color["blue"]
player_x = 50
player_y = hapi.HEIGHT // 2 - player_size // 2
player_speed = 3 
jump_height = 10
gravity = 1

pipe_width = 50
pipe_color = hapi.color["green"]
pipe_speed = 0.2 
pipe_interval = 2000
pipes = []

score = 0
game_over = False

max_pipe_height = 300  

# Function to spawn a new pipe
def spawn_pipe():
    pipe_height = random.randint(100, max_pipe_height)
    pipes.append([hapi.WIDTH, hapi.HEIGHT - pipe_height, pipe_width, pipe_height])

while hapi.is_running and not game_over:
    hapi.background(hapi.color["white"])

    hapi.fill(player_color)
    hapi.rect(player_x, player_y, player_size, player_size)

    # Draw and move pipes
    for pipe in pipes[:]:
        hapi.fill(pipe_color)
        hapi.rect(pipe[0], pipe[1], pipe[2], pipe[3])
        pipe[0] -= pipe_speed

        if (
            player_x < pipe[0] + pipe[2]
            and player_x + player_size > pipe[0]
            and player_y < pipe[1] + pipe[3]
            and player_y + player_size > pipe[1]
        ):
            game_over = True

        # Check if the pipe has passed the player
        if pipe[0] + pipe[2] < 0:
            pipes.remove(pipe)
            score += 1

    # Display score
    hapi.text("Score: " + str(score), x=10, y=10)

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and player_y > 0:
        player_y -= jump_height
    else:
        player_y += gravity

    # Spawn new pipes periodically
    if hapi._frame_count % pipe_interval == 0:
        spawn_pipe()

    # Check if the player is out of bounds
    if player_y > hapi.HEIGHT - player_size:
        player_y = hapi.HEIGHT - player_size

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()
