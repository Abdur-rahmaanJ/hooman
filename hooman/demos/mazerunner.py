from hooman import Hooman
import pygame  
import random

# Initialize Hooman
window_width, window_height = 800, 600
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)
player_color = (0, 0, 255)
exit_color = (255, 0, 0)
wall_color = (0, 0, 0)

# Maze
maze_size = 10
maze = [[0] * maze_size for _ in range(maze_size)]

# Generate maze (1 represents walls, 0 represents open paths)
for i in range(maze_size):
    for j in range(maze_size):
        if random.random() < 0.3:  # Adjust the probability to control the density of walls
            maze[i][j] = 1

# Place the player at the top-left corner
player_pos = [0, 0]

# Place the exit at the bottom-right corner
exit_pos = [maze_size - 1, maze_size - 1]

def draw_maze():
    cell_width = window_width // maze_size
    cell_height = window_height // maze_size

    for i in range(maze_size):
        for j in range(maze_size):
            if maze[i][j] == 1:
                hapi.fill(wall_color)
            else:
                hapi.fill(bg_col)
            hapi.rect(j * cell_width, i * cell_height, cell_width, cell_height)

    hapi.fill(player_color)
    hapi.rect(player_pos[1] * cell_width, player_pos[0] * cell_height, cell_width, cell_height)

    hapi.fill(exit_color)
    hapi.rect(exit_pos[1] * cell_width, exit_pos[0] * cell_height, cell_width, cell_height)

def handle_events(event):
    global player_pos

    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False
        elif event.key == pygame.K_UP and player_pos[0] > 0 and maze[player_pos[0] - 1][player_pos[1]] == 0:
            player_pos[0] -= 1
        elif event.key == pygame.K_DOWN and player_pos[0] < maze_size - 1 and maze[player_pos[0] + 1][player_pos[1]] == 0:
            player_pos[0] += 1
        elif event.key == pygame.K_LEFT and player_pos[1] > 0 and maze[player_pos[0]][player_pos[1] - 1] == 0:
            player_pos[1] -= 1
        elif event.key == pygame.K_RIGHT and player_pos[1] < maze_size - 1 and maze[player_pos[0]][player_pos[1] + 1] == 0:
            player_pos[1] += 1

hapi.handle_events = handle_events

while hapi.is_running:
    hapi.background(bg_col)

    draw_maze()

    # Update display and handle events
    hapi.flip_display()
    hapi.event_loop()

hapi.quit()
