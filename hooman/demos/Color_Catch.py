import pygame
import random
from hooman import Hooman

# Initialize Hooman
hapi = Hooman(500, 500)

# Bucket properties
bucket_x, bucket_y = 250, 450
bucket_width, bucket_height = 100, 20
bucket_color = (0, 128, 255)
bucket_speed = 5

# Ball properties
ball_radius = 10
ball_speed = 0.2  # Decreased ball speed for slower movement
balls = []
max_balls = 30
balls_spawned = 0

# Game properties
score = 0
lives = 10  # Increased the number of lives to 10

def spawn_ball():
    x = random.randint(ball_radius, 500 - ball_radius)
    color = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255)])
    balls.append([x, 0, ball_speed, color])

# Variables to control game timing
game_start_time = pygame.time.get_ticks()
game_duration = 60000  # Game duration in milliseconds (e.g., 60 seconds)

while hapi.is_running:
    hapi.background((255, 255, 255))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hapi.is_running = False

    # Handle bucket movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bucket_x -= bucket_speed
    if keys[pygame.K_RIGHT]:
        bucket_x += bucket_speed
    bucket_x = max(0, min(500 - bucket_width, bucket_x))

    # Set color and draw bucket
    hapi.fill(bucket_color)
    hapi.rect(bucket_x, bucket_y, bucket_width, bucket_height)

    # Spawn and move balls
    if balls_spawned < max_balls:
        if random.randint(1, 100) <= 2:
            spawn_ball()
            balls_spawned += 1
    for ball in balls[:]:
        ball[1] += ball[2]
        hapi.fill(ball[3])
        hapi.circle(ball[0], ball[1], ball_radius)
        if bucket_y < ball[1] + ball_radius < bucket_y + bucket_height and \
           bucket_x < ball[0] < bucket_x + bucket_width:
            score += 1
            balls.remove(ball)
        elif ball[1] > 500:
            balls.remove(ball)

    # Display score and lives
    hapi.text(f"Score: {score}", 10, 10)
    hapi.text(f"Lives: {lives}", 10, 30)

    # Check for game over based on time and balls
    current_time = pygame.time.get_ticks()
    if current_time - game_start_time >= game_duration or (len(balls) == 0 and balls_spawned >= max_balls):
        print("Game Over! Your score:", score)
        hapi.is_running = False

    hapi.flip_display()
    hapi.event_loop()
