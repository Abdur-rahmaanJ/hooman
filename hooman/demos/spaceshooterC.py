import random
import pygame
from hooman import Hooman

# Game window dimensions
WIDTH, HEIGHT = 600, 800

# Initialize Hooman
hapi = Hooman(WIDTH, HEIGHT)

# Spaceship class
class Spaceship:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 60
        self.speed = 5
        self.color = (255, 255, 255)

    def move(self, direction):
        if direction == "LEFT" and self.x > 0:
            self.x -= self.speed
        elif direction == "RIGHT" and self.x < WIDTH - 50:
            self.x += self.speed

    def draw(self):
        hapi.fill(self.color)
        hapi.rect(self.x, self.y, 50, 30)
        hapi.fill(255, 255, 255)

    def change_speed(self, increase):
        if increase:
            self.speed = 10  # Increased speed
        else:
            self.speed = 5  # Default speed

    def change_color(self, color):
        self.color = color

# Asteroid class
class Asteroid:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 30)
        self.y = 0
        self.speed = random.uniform(2.0, 4.0)

    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = 0
            self.x = random.randint(0, WIDTH - 30)

    def draw(self):
        hapi.rect(self.x, self.y, 30, 30)

    def is_hit_by(self, projectile):
        return (self.x < projectile.x < self.x + 30 and
                self.y < projectile.y < self.y + 30)

# Projectile class
class Projectile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10

    def update(self):
        self.y -= self.speed

    def draw(self):
        hapi.rect(self.x, self.y, 5, 10)

    def off_screen(self):
        return self.y < 0

# Initialize spaceship, asteroids, projectiles, and score
spaceship = Spaceship()
asteroids = [Asteroid() for _ in range(5)]
projectiles = []
score = 0

# Define the event handler function
def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False

# Attach the event handler to the Hooman instance
hapi.handle_event = handle_events


# Game loop
while hapi.is_running:
    # Handle events and spaceship movement
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hapi.is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spaceship.move("LEFT")
                spaceship.change_color((255, 0, 0))
                spaceship.change_speed(increase=True)
            elif event.key == pygame.K_RIGHT:
                spaceship.move("RIGHT")
                spaceship.change_color((255, 0, 0))
                spaceship.change_speed(increase=True)
            elif event.key == pygame.K_SPACE:
                projectiles.append(Projectile(spaceship.x + 22, spaceship.y))
            elif event.key == pygame.K_UP:  # Example key to increase speed
                spaceship.change_speed(True)
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                spaceship.change_color((255, 255, 255))  # Change color back to original
                spaceship.change_speed(increase=False)
            if event.key == pygame.K_UP:  # Example key to reset speed
                spaceship.change_speed(False)
    # hapi.event_loop()
    
    # Update and draw asteroids
    hapi.background(0, 0, 0)
    for asteroid in asteroids:
        asteroid.update()
        asteroid.draw()

    # Update and draw projectiles
    for projectile in projectiles[:]:
        projectile.update()
        if projectile.off_screen():
            projectiles.remove(projectile)
        else:
            projectile.draw()

    # Check for collisions and update score
    for projectile in projectiles[:]:
        for asteroid in asteroids[:]:
            if asteroid.is_hit_by(projectile):
                projectiles.remove(projectile)
                asteroids.remove(asteroid)
                asteroids.append(Asteroid())  # Add a new asteroid
                score += 1  # Increase score
                break

    # Draw the spaceship
    spaceship.draw()

    # Draw the score
    hapi.fill(255, 255, 255)  # White color for the text
    hapi.text(f"Score: {score}", 10, 10)

    # Refresh the screen
    hapi.flip_display()

# pygame.quit()
