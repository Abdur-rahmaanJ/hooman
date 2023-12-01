import random
import pygame
from hooman import Hooman

# Initializing Pygame and Hooman
pygame.init()
window_width, window_height = 800, 600
hapi = Hooman(window_width, window_height)

# Constants
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BRICK_WIDTH, BRICK_HEIGHT = 80, 30
BALL_SPEED = 2
PADDLE_SPEED = 10
FPS = 30
SCORE_FONT_SIZE = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Score
score = 0

score_font = pygame.font.Font(None, SCORE_FONT_SIZE)


# Ball class
class Ball:
    def __init__(self):
        self.x = window_width // 2 + random.randint(100, 200)
        self.y = window_height // 2 + random.randint(100, 200)
        self.speed_x = BALL_SPEED
        self.speed_y = -BALL_SPEED

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off walls
        if self.x - BALL_RADIUS < 0 or self.x + BALL_RADIUS > window_width:
            self.speed_x *= -1
        if self.y - BALL_RADIUS < 0:
            self.speed_y *= -1

        # Ball missed paddle
        if self.y - BALL_RADIUS > window_height:
            return True  # Ball is out of bounds
        return False

    def draw(self):
        hapi.fill(BLACK)
        hapi.circle(self.x, self.y, BALL_RADIUS)

    def get_rect(self):
        return pygame.Rect(self.x - BALL_RADIUS, self.y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)

# Paddle class
class Paddle:
    def __init__(self):
        self.x = window_width // 2 - PADDLE_WIDTH // 2
        self.y = window_height - 40

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT]:
            self.x += PADDLE_SPEED

        # Limiting paddle movement
        self.x = max(0, min(self.x, window_width - PADDLE_WIDTH))

    def draw(self):
        hapi.fill((0, 0, 255))
        hapi.rect(self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT)

# Brick class
class Brick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self):
        hapi.fill(self.color)
        hapi.rect(self.x, self.y, BRICK_WIDTH, BRICK_HEIGHT)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, BRICK_WIDTH, BRICK_HEIGHT)


# Initializing game elements
ball = Ball()
paddle = Paddle()
bricks = [Brick(col * (BRICK_WIDTH + 2), row * (BRICK_HEIGHT + 2)) for row in range(5) for col in range(10)]

#game main loop
running = True
game_over = False
while running and hapi.is_running:
    hapi.background(WHITE)

    # Updating game elements
    if not game_over:
        ball_out = ball.update()
        paddle.update()

        # Ball and paddle collision
        if ball.get_rect().colliderect(paddle.get_rect()):
            ball.speed_y *= -1

        # Ball and bricks collision
        for brick in bricks[:]:
            if ball.get_rect().colliderect(brick.get_rect()):
                ball.speed_y *= -1
                bricks.remove(brick)
                score += 1  # Increment score

    # Draw game elements
    for brick in bricks:
        brick.draw()
    if not game_over:
        ball.draw()
    paddle.draw()

    # Render and display the score
    score_surface = score_font.render(f"Score: {score}", True, BLACK)
    hapi.screen.blit(score_surface, (10, 10))

    # Check if the game is over
    if ball_out and not game_over:
        game_over = True
        game_over_surface = score_font.render("Game Over - Press any key to exit", True, BLACK)
        hapi.screen.blit(game_over_surface, (window_width // 2 - 150, window_height // 2 - 20))

    hapi.flip_display()
    hapi.event_loop()

    # End game if ball is out
    if ball_out:
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    running = False
                elif event.type == pygame.KEYDOWN:
                    game_over = False
                    running = False

# Quit the game
pygame.quit()
