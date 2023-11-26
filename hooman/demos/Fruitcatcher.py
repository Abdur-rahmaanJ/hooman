from hooman import Hooman
import pygame
import random

# Initialize Hooman
window_width, window_height = 800, 600
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)

# Basket
basket_width, basket_height = 100, 20
basket_x = window_width // 2 - basket_width // 2
basket_y = window_height - 2 * basket_height
basket_color = (0, 128, 255)

# Fruits
num_fruits = 5
fruits = []

for _ in range(num_fruits):
    fruit_x = random.randint(50, window_width - 50)
    fruit_y = random.randint(50, 200)
    fruit_radius = 20
    fruit_color = (255, 0, 0)
    fruits.append((fruit_x, fruit_y, fruit_radius, fruit_color))

# Game variables
score = 0
speed = 5

def handle_events(event):
    global basket_x

    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            basket_x -= 20
        elif event.key == pygame.K_RIGHT:
            basket_x += 20

    # Ensure the basket stays within the window
    basket_x = max(0, min(basket_x, window_width - basket_width))

hapi.handle_events = handle_events

# Set initial font size
hapi.font_size = 20

while hapi.is_running:
    hapi.background(bg_col)

    # Draw basket
    hapi.fill(basket_color)
    hapi.rect(basket_x, basket_y, basket_width, basket_height)

    # Draw fruits
    for i, fruit in enumerate(fruits):
        fruit_x, fruit_y, fruit_radius, fruit_color = fruit
        hapi.fill(fruit_color)
        hapi.circle(int(fruit_x), int(fruit_y), int(fruit_radius))

        # Check if fruit is caught
        if (
            basket_x < fruit_x < basket_x + basket_width
            and basket_y < fruit_y < basket_y + basket_height
        ):
            score += 1
            # Respawn the fruit at the top
            fruit_x = random.randint(50, window_width - 50)
            fruit_y = random.randint(50, 200)
            fruits[i] = (fruit_x, fruit_y, fruit_radius, fruit_color)

        # Move the fruit down
        fruit_y += speed
        fruits[i] = (fruit_x, fruit_y, fruit_radius, fruit_color)

        # Check if fruit reaches the bottom
        if fruit_y > window_height:
            # Respawn the fruit at the top
            fruit_x = random.randint(50, window_width - 50)
            fruit_y = random.randint(50, 200)
            fruits[i] = (fruit_x, fruit_y, fruit_radius, fruit_color)

    # Display the score
    hapi.fill((0, 0, 0))
    hapi.text(f"Score: {score}", 20, 20)

    # Update display and handle events
    hapi.flip_display()
    hapi.event_loop()

hapi.quit()
