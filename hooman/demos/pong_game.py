import pygame
import random

# Initialize Pygame
pygame.init()

# Game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
paddle_width, paddle_height = 15, 90
ball_size = 20
player_speed = 6
opponent_speed = 6
ball_speed_x, ball_speed_y = 7 * random.choice((1, -1)), 7 * random.choice((1, -1))
player_score, opponent_score = 0, 0

# Paddles and ball
player = pygame.Rect(width - 20, height // 2 - paddle_height // 2, paddle_width, paddle_height)
opponent = pygame.Rect(20, height // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)

# Game clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= player_speed
    if keys[pygame.K_DOWN] and player.bottom < height:
        player.y += player_speed

    # Opponent AI movement
    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision (top or bottom)
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1

    # Ball collision (paddles)
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # Score update
    if ball.left <= 0:
        player_score += 1
        ball.center = (width // 2, height // 2)
        ball_speed_x = 7 * random.choice((1, -1))
        ball_speed_y = 7 * random.choice((1, -1))
    if ball.right >= width:
        opponent_score += 1
        ball.center = (width // 2, height // 2)
        ball_speed_x = 7 * random.choice((1, -1))
        ball_speed_y = 7 * random.choice((1, -1))

    # Drawing the game
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (width // 2, 0), (width // 2, height))

    # Display scores
    font = pygame.font.Font(None, 36)
    player_text = font.render(str(player_score), True, WHITE)
    screen.blit(player_text, (width // 2 + 20, 20))

    opponent_text = font.render(str(opponent_score), True, WHITE)
    screen.blit(opponent_text, (width // 2 - 40, 20))

    # Updating the window
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
