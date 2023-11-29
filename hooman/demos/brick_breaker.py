from hooman import Hooman
import random
import pygame

window_width, window_height = 600, 400
hapi = Hooman(window_width, window_height)


pygame.init()

brick_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]  


ball_radius = 10
ball_x = window_width // 2
ball_y = window_height // 2
ball_speed_x = random.choice([-0.5, 0.5])
ball_speed_y = -0.5
ball_color = (0, 0, 0) 


paddle_width, paddle_height = 100, 10
paddle_x = window_width // 2 - paddle_width // 2
paddle_y = window_height - 50
paddle_speed = 5
paddle_color = (100, 100, 100)  


brick_width, brick_height = 50, 20
num_bricks = 8
bricks = []
for i in range(num_bricks):
    bricks.append([i * brick_width, 50, random.choice(brick_colors)])

def draw_ball():
    hapi.fill(ball_color)
    hapi.circle(ball_x, ball_y, ball_radius)

def draw_paddle():
    hapi.fill(paddle_color)
    hapi.rect(paddle_x, paddle_y, paddle_width, paddle_height)

def draw_bricks():
    for brick in bricks:
        hapi.fill(brick[2])
        hapi.rect(brick[0], brick[1], brick_width, brick_height)

while hapi.is_running:
    hapi.background(255)

    draw_ball()
    draw_paddle()
    draw_bricks()

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with walls
    if ball_x <= 0 or ball_x >= window_width:
        ball_speed_x *= -1
    if ball_y <= 0:
        ball_speed_y *= -1

    # Ball collision with paddle
    if (
        ball_y + ball_radius >= paddle_y
        and ball_x >= paddle_x
        and ball_x <= paddle_x + paddle_width
    ):
        ball_speed_y *= -1

    # Ball collision with bricks
    for brick in bricks:
        if (
            ball_y - ball_radius <= brick[1] + brick_height
            and ball_x >= brick[0]
            and ball_x <= brick[0] + brick_width
        ):
            ball_speed_y *= -1
            bricks.remove(brick)
            break

    # Check if all bricks are broken
    if not bricks:
        print("Game Over - All bricks are broken!")
        break

   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT]:
        paddle_x += paddle_speed

    
    paddle_x = max(0, min(paddle_x, window_width - paddle_width))

    hapi.flip_display()
    hapi.event_loop()

pygame.quit()  



