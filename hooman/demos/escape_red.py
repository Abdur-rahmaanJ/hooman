import random
import pygame
from hooman import Hooman

WIDTH, HEIGHT = 800, 600
hapi = Hooman(WIDTH, HEIGHT)

player_x, player_y = WIDTH // 2, HEIGHT - 50
player_size = 50
player_color = hapi.color['blue']
objects = []
object_size = 30
object_speed = 1
spawn_rate = 15
score = 0
lives = 10
frame_count = 0

def spawn_object():
    x = random.randint(object_size, WIDTH - object_size)
    y = -object_size
    is_bomb = random.choice([True, False])
    color = hapi.color['red'] if is_bomb else hapi.color['green']
    objects.append([x, y, is_bomb, color])

def check_collision(player_x, player_y, player_size, object_x, object_y, object_size):
    return (
        abs(player_x - object_x) < (player_size + object_size) // 2
        and abs(player_y - object_y) < (player_size + object_size) // 2
    )

game_over = False
while hapi.is_running and not game_over:
    hapi.background(hapi.color['white'])

    hapi.fill(player_color)
    hapi.rect(player_x - player_size // 2, player_y - player_size // 2, player_size, player_size)

    # Handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= 10
            elif event.key == pygame.K_RIGHT:
                player_x += 10

    if frame_count % spawn_rate == 0:
        spawn_object()

    for obj in objects[:]:
        hapi.fill(obj[3])  # Object color
        hapi.ellipse(obj[0], obj[1], object_size, object_size)

        obj[1] += object_speed

        if check_collision(player_x, player_y, player_size, obj[0], obj[1], object_size):
            if obj[2]:  # If it's a bomb, reduce lives
                lives -= 1
                objects.remove(obj)
                if lives <= 0:
                    game_over = True
            else:  # If it's a regular object, increase score and remove it
                score += 1
                objects.remove(obj)

    hapi.fill(hapi.color['black'])
    hapi.text(f"Score: {score}", 10, 10)
    hapi.text(f"Lives: {lives}", 10, 40)

    hapi.flip_display()

    frame_count += 1

print("Game Over")
pygame.quit()
