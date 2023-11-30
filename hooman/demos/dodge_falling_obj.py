from hooman import Hooman
import pygame
import random

# Initialize Hooman
window_width, window_height = 800, 600
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)
player_color = (0, 128, 255)
player_width, player_height = 50, 50
player_x = (window_width - player_width) // 2
player_y = window_height - player_height - 20
player_speed = 8

# Falling objects
num_objects = 3  # Adjust the number of falling objects
objects = []

for _ in range(num_objects):
    object_x = random.randint(0, window_width - 30)
    object_y = random.randint(-300, -50)
    object_width, object_height = 30, 30
    object_color = (255, 0, 0)
    object_speed = random.uniform(1, 2)
    objects.append((object_x, object_y, object_width, object_height, object_color, object_speed))

def handle_events(event):
    global player_x

    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False
        if event.key == pygame.K_LEFT:
            player_x -= player_speed
        if event.key == pygame.K_RIGHT:
            player_x += player_speed

hapi.handle_events = handle_events

def update_objects():
    global objects

    for i, obj in enumerate(objects):
        obj_x, obj_y, obj_width, obj_height, _, obj_speed = obj
        obj_y += obj_speed

        # If the object reaches the bottom, reset its position
        if obj_y > window_height:
            obj_y = random.randint(-300, -50)
            obj_x = random.randint(0, window_width - obj_width)
            obj_speed = random.uniform(1, 2)

        objects[i] = (obj_x, obj_y, obj_width, obj_height, object_color, obj_speed)

while hapi.is_running:
    hapi.background(bg_col)

    # Draw player
    hapi.fill(player_color)
    hapi.rect(player_x, player_y, player_width, player_height)

    # Draw falling objects
    for obj in objects:
        obj_x, obj_y, obj_width, obj_height, obj_color, _ = obj
        hapi.fill(obj_color)
        hapi.rect(obj_x, obj_y, obj_width, obj_height)

    # Update objects and check for collisions
    update_objects()
    for obj in objects:
        obj_x, obj_y, obj_width, obj_height, _, _ = obj
        if (
            player_x < obj_x + obj_width
            and player_x + player_width > obj_x
            and player_y < obj_y + obj_height
            and player_y + player_height > obj_y
        ):
            print("Game Over!")
            hapi.is_running = False

    # Update display and handle events
    hapi.flip_display()
    hapi.event_loop()

pygame.quit()
