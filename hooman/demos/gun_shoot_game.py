import pygame
from hooman import Hooman
import random

# Spaceship settings
pygame.init()
window_width, window_height = 600, 600
hapi = Hooman(window_width, window_height)

# Spaceship settings
spaceship_width, spaceship_height = 50, 50
spaceship_x = (window_width - spaceship_width) // 2
spaceship_y = window_height - spaceship_height - 10
spaceship_speed = 2
gun_height = 10  # Height of the 'gun' part at the bottom of the spaceship

# Asteroids settings
asteroids = []
asteroid_spawn_rate = 50
asteroid_speed = 0.5

# Bullet settings
bullets = []
bullet_speed = 5
bullet_width, bullet_height = 10, 20
last_shot_time = 0
shot_cooldown = 500

# Game settings
score = 0
lives = 3

def spawn_asteroid():
    x = random.randint(0, window_width)
    size = random.randint(5, 15)  # Smaller asteroids
    asteroids.append([x, -size, size])

def move_asteroids():
    for asteroid in asteroids:
        asteroid[1] += asteroid_speed

def draw_asteroids():
    for asteroid in asteroids:
        pygame.draw.circle(hapi.screen, (100, 100, 100), (asteroid[0], asteroid[1]), asteroid[2])

def shoot_bullet(current_time):
    global last_shot_time
    if current_time - last_shot_time > shot_cooldown:
        bullets.append([spaceship_x + spaceship_width // 2 - bullet_width // 2, spaceship_y])
        last_shot_time = current_time

def move_bullets():
    for bullet in bullets:
        bullet[1] -= bullet_speed

def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(hapi.screen, (255, 0, 0), (bullet[0], bullet[1], bullet_width, bullet_height))



def check_collisions():
    global score, lives
    for asteroid in asteroids[:]:
        asteroid_rect = pygame.Rect(asteroid[0] - asteroid[2], asteroid[1] - asteroid[2], asteroid[2] * 2, asteroid[2] * 2)
        gun_rect = pygame.Rect(spaceship_x, spaceship_y + spaceship_height - gun_height, spaceship_width, gun_height)
        for bullet in bullets[:]:
            bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height)
            if asteroid_rect.colliderect(bullet_rect):
                asteroids.remove(asteroid)
                bullets.remove(bullet)
                score += 1
                break
        if asteroid_rect.colliderect(gun_rect):
            asteroids.remove(asteroid)
            lives -= 1

while hapi.is_running and lives > 0:
    hapi.background((0, 0, 0))

    # Handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hapi.is_running = False

    # Draw spaceship
    pygame.draw.rect(hapi.screen, (0, 0, 255), (spaceship_x, spaceship_y, spaceship_width, spaceship_height))

    # Move and draw asteroids
    if random.randint(0, asteroid_spawn_rate) == 0:
        spawn_asteroid()
    move_asteroids()
    draw_asteroids()

    # Move and draw bullets
    move_bullets()
    draw_bullets()

    # Check for collisions
    check_collisions()

    # Display score and lives
    hapi.fill(hapi.color['white'])
    hapi.text(f'Score: {score}', 10, 10)
    hapi.text(f'Lives: {lives}', 10, 30)

    # Move spaceship
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship_x > 0:
        spaceship_x -= spaceship_speed
    if keys[pygame.K_RIGHT] and spaceship_x + spaceship_width < window_width:
        spaceship_x += spaceship_speed

    current_time = pygame.time.get_ticks()
    if keys[pygame.K_SPACE]:
        shoot_bullet(current_time)

    hapi.flip_display()
    hapi.event_loop()
