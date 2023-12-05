import random
import pygame
from hooman import Hooman

# Initialize Pygame and Hooman
pygame.init()
window_width, window_height = 800, 600
hapi = Hooman(window_width, window_height)

# Colors and Constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SPACESHIP_SPEED = 5
ASTEROID_SPEED = 3
BULLET_SPEED = 7
FPS = 30

# Spaceship Class


class Spaceship:
    def __init__(self):
        self.x = window_width // 2
        self.y = window_height - 50
        self.width = 40
        self.height = 40

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= SPACESHIP_SPEED
        if keys[pygame.K_RIGHT]:
            self.x += SPACESHIP_SPEED

        # Limit movement to screen width
        self.x = max(0, min(self.x, window_width - self.width))

    def draw(self):
        hapi.fill(RED)
        hapi.rect(self.x, self.y, self.width, self.height)

    def shoot(self):
        bullets.append(Bullet(self.x + self.width // 2 - 2, self.y))

# Asteroid Class


class Asteroid:
    def __init__(self):
        self.x = random.randint(0, window_width - 20)
        self.y = -20
        self.width = 20
        self.height = 20

    def update(self):
        self.y += ASTEROID_SPEED

    def draw(self):
        hapi.fill((128, 128, 128))  # Gray color
        hapi.rect(self.x, self.y, self.width, self.height)

# Bullet Class


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 10

    def update(self):
        self.y -= BULLET_SPEED

    def draw(self):
        hapi.fill(RED)
        hapi.rect(self.x, self.y, self.width, self.height)


# Initialize game elements
spaceship = Spaceship()
asteroids = []
bullets = []
score = 0
lives = 3

# Game Loop
while hapi.is_running:
    hapi.background(BLUE)

    # Update spaceship
    spaceship.move()
    spaceship.draw()

    # Generate and update asteroids
    if random.randint(0, 60) == 0:  # Random chance to create an asteroid
        asteroids.append(Asteroid())
    for asteroid in asteroids[:]:
        asteroid.update()
        asteroid.draw()

        # Check for bullet collision
        for bullet in bullets[:]:
            if bullet.x in range(asteroid.x, asteroid.x + asteroid.width) and bullet.y in range(asteroid.y, asteroid.y + asteroid.height):
                bullets.remove(bullet)
                asteroids.remove(asteroid)
                score += 1
                break  # Break to avoid modifying the list during iteration

        # Check for spaceship collision
        if spaceship.x in range(asteroid.x, asteroid.x + asteroid.width) and spaceship.y in range(asteroid.y, asteroid.y + asteroid.height):
            lives -= 1
            asteroids.remove(asteroid)
            if lives == 0:
                hapi.is_running = False  # Game over

        if asteroid.y > window_height:
            asteroids.remove(asteroid)

    # Update bullets
    for bullet in bullets[:]:
        bullet.update()
        bullet.draw()
        if bullet.y < 0:
            bullets.remove(bullet)

    # Handle shooting
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spaceship.shoot()

    # Display score and lives
    score_surface = pygame.font.Font(None, 30).render(
        f"Score: {score}", True, WHITE)
    lives_surface = pygame.font.Font(None, 30).render(
        f"Lives: {lives}", True, WHITE)
    hapi.screen.blit(score_surface, (10, 10))
    hapi.screen.blit(lives_surface, (window_width - 100, 10))

    # Update Display
    hapi.flip_display()
    hapi.event_loop()
    pygame.time.Clock().tick(FPS)

pygame.quit()
