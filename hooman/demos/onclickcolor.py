from hooman import Hooman
import pygame  
import random
import math  

# Initialize Hooman
window_width, window_height = 800, 600
hapi = Hooman(window_width, window_height)

bg_col = (0, 0, 0)

# Circles
num_circles = 10
circles = []

for _ in range(num_circles):
    circle_x = random.randint(50, window_width - 50)
    circle_y = random.randint(50, window_height - 50)
    circle_radius = 30
    circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    circles.append((circle_x, circle_y, circle_radius, circle_color))

def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = hapi.mouseX(), hapi.mouseY()  
        for i, circle in enumerate(circles):
            circle_x, circle_y, circle_radius, circle_color = circle
            distance = math.sqrt((mouse_x - circle_x)**2 + (mouse_y - circle_y)**2)  
            if distance < circle_radius:
                new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                circles[i] = (circle_x, circle_y, circle_radius, new_color)

hapi.handle_events = handle_events

while hapi.is_running:
    hapi.background(bg_col)

    # Draw circles
    for circle in circles:
        circle_x, circle_y, circle_radius, circle_color = circle
        hapi.fill(circle_color)
        hapi.circle(int(circle_x), int(circle_y), int(circle_radius))

    # Update display and handle events
    hapi.flip_display()
    hapi.event_loop()

hapi.quit()
