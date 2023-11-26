from hooman import Hooman
import random
import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

paddle_width, paddle_height = 100, 10
paddle_x = (window_width - paddle_width) // 2
paddle_y = window_height - 20

ball_radius = 15
ball_x = random.randint(ball_radius, window_width - ball_radius)
ball_y = 0
ball_speed = 0.3  # Adjust the ball speed

score = 0
missed_balls = 0
max_missed_balls = 5  # Maximum allowed missed balls

paddle_speed = 2  # Adjust paddle movement speed

while hapi.is_running and missed_balls < max_missed_balls:
    hapi.background((255, 255, 255))

    # Draw paddle
    hapi.fill(hapi.color["blue"])
    hapi.rect(paddle_x, paddle_y, paddle_width, paddle_height)

    # Draw ball
    hapi.fill(hapi.color["red"])
    hapi.circle(ball_x, ball_y, ball_radius)

    # Move the ball
    ball_y += ball_speed

    # Check collision with paddle
    if (
        paddle_x - ball_radius < ball_x < paddle_x + paddle_width + ball_radius
        and paddle_y - ball_radius < ball_y < paddle_y + paddle_height + ball_radius
    ):
        ball_y = 0
        ball_x = random.randint(ball_radius, window_width - ball_radius)
        score += 1

    # Check if the ball missed the paddle
    if ball_y > window_height:
        ball_y = 0
        ball_x = random.randint(ball_radius, window_width - ball_radius)
        score -= 1
        missed_balls += 1

    # Draw score
    hapi.fill(hapi.color["black"])
    hapi.text(f"Score: {score}", 20, 20)

    # Move the paddle with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x + paddle_width < window_width:
        paddle_x += paddle_speed

    hapi.flip_display()
    hapi.event_loop()

# End the game
pygame.quit()
