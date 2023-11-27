from hooman import Hooman
import pygame
import random

# Initialize window and Hooman
window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

# Slider options
slider_options = {
    "background_color": hapi.color["grey"],
    "slider_color": (220, 220, 220),
}

# Create sliders for R, G, B values
red_slider = hapi.slider(50, 400, 400, 30, slider_options)
green_slider = hapi.slider(50, 350, 400, 30, slider_options)
blue_slider = hapi.slider(50, 300, 400, 30, slider_options)

# Function to generate a random color
def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

# Target color and color change count
target_color = random_color()
color_match_timer = 300  # Time in frames to match the color
color_change_count = 0
max_color_changes = 5  # Quit after 5 color changes

# Scoring
score = 0

# Event handling
def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False

hapi.handle_events = handle_events

# Set frame rate
frame_rate = 60
clock = pygame.time.Clock()

def calculate_score(player_color, target_color):
    # Simple color difference calculation
    return max(0, 100 - sum(abs(pc - tc) for pc, tc in zip(player_color, target_color)) // 10)

# Game loop
while hapi.is_running:
    hapi.background((255, 255, 255))

    # Update sliders
    red_slider.update()
    green_slider.update()
    blue_slider.update()

    # Player's color
    player_color = (int(red_slider.value() * 255), int(green_slider.value() * 255), int(blue_slider.value() * 255))

    # Draw color boxes
    hapi.fill(target_color)
    hapi.rect(50, 50, 150, 150)
    hapi.fill(player_color)
    hapi.rect(300, 50, 150, 150)

    # Timer for color match
    if color_match_timer > 0:
        color_match_timer -= 1
    else:
        # Add to score if colors match
        score += calculate_score(player_color, target_color)
        # Change target color
        target_color = random_color()
        color_match_timer = 300  # Reset timer
        color_change_count += 1

    # Display the timer and score
    remaining_time = color_match_timer // frame_rate
    hapi.text(f"Time: {remaining_time}s", 220, 450)
    hapi.text(f"Score: {score}", 50, 450)

    # Check if max color changes reached
    if color_change_count >= max_color_changes:
        break

    hapi.flip_display()
    hapi.event_loop()

    # Control the frame rate
    clock.tick(frame_rate)

# Output Game Over message and score to terminal
print("Game Over")
print(f"Final Score: {score}")

pygame.quit()
