import pygame
import random
from hooman import Hooman

def check_collision(player_x, player_y, player_size, circle_x, circle_y, circle_size):
    player_rect = pygame.Rect(player_x - player_size // 2, player_y - player_size // 2, player_size, player_size)
    circle_rect = pygame.Rect(circle_x - circle_size // 2, circle_y - circle_size // 2, circle_size, circle_size)
    return player_rect.colliderect(circle_rect)

pygame.init()
window_width, window_height = 800, 600
hapi = Hooman(window_width, window_height)


player_x, player_y = window_width // 2, window_height // 2
player_size = 50
player_color = hapi.color['red']
circles = []
circle_size = 20
circle_speed = 0.1
spawn_rate = 600  
score = 0
lives = 10
difficulty_increase_rate = 100


def spawn_circle():
    safe_distance = 100
    while True:
        x = random.randint(circle_size, window_width - circle_size)
        y = random.randint(circle_size, window_height - circle_size)
        if abs(x - player_x) > safe_distance and abs(y - player_y) > safe_distance:
            break
    color = random.choice([hapi.color['red'],hapi.color['red'],hapi.color['green'], hapi.color['blue']])
    circles.append([x, y, color])


def handle_events(event):
    global player_x, player_y, player_color
    if event.type == pygame.QUIT:
        hapi.is_running = False  
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False
        elif event.key == pygame.K_r:
            player_color = hapi.color["red"]
        elif event.key == pygame.K_g:
            player_color = hapi.color["green"]
        elif event.key == pygame.K_b:
            player_color = hapi.color["blue"]
        elif event.key == pygame.K_LEFT:
            player_x -= 10
        elif event.key == pygame.K_RIGHT:
            player_x += 10
        elif event.key == pygame.K_UP:
            player_y -= 10
        elif event.key == pygame.K_DOWN:
            player_y += 10

    player_x = max(player_size // 2, min(window_width - player_size // 2, player_x))
    player_y = max(player_size // 2, min(window_height - player_size // 2, player_y))

hapi.handle_events = handle_events


frame_count = 0
game_over = False
while hapi.is_running and not game_over:
    hapi.background(hapi.color['white'])

    for event in pygame.event.get():
        handle_events(event)

   
    frame_count += 1
    if frame_count >= spawn_rate:
        spawn_circle()
        frame_count = 0


    for circle in circles[:]:
        hapi.fill(circle[2])
        hapi.ellipse(circle[0], circle[1], circle_size, circle_size)
        
        move_direction = random.choice(["towards_player", "random"])
        if move_direction == "towards_player":
            if circle[0] > player_x:
                circle[0] -= circle_speed
            elif circle[0] < player_x:
                circle[0] += circle_speed
            if circle[1] > player_y:
                circle[1] -= circle_speed
            elif circle[1] < player_y:
                circle[1] += circle_speed
        else:
            circle[0] += random.randint(-int(circle_speed), int(circle_speed))
            circle[1] += random.randint(-int(circle_speed), int(circle_speed))

        circle[0] = max(circle_size, min(window_width - circle_size, circle[0]))
        circle[1] = max(circle_size, min(window_height - circle_size, circle[1]))

      
        if check_collision(player_x, player_y, player_size, circle[0], circle[1], circle_size):
            if circle[2] == player_color:
                score += 1
                circles.remove(circle)
                if score % difficulty_increase_rate == 0:
                    # circle_speed += 1
                    spawn_rate = max(30, spawn_rate - 5)
            else:
                lives -= 1
                circles.remove(circle)
                if lives <= 0:
                    game_over = True

   
    hapi.fill(player_color)
    hapi.rect(player_x - player_size // 2, player_y - player_size // 2, player_size, player_size)

    hapi.fill(hapi.color['black'])
    hapi.text(f"Score: {score}", 10, 10)
    hapi.text(f"Lives: {lives}", 10, 40)

    hapi.flip_display()
    hapi.event_loop()

print("Game Over")
pygame.quit()
