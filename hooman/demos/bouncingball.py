# demo_bouncing_ball.py
from hooman import Hooman
import pygame

# Initialize Hooman
window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)


bg_col = (255, 255, 255)

# Ball
ball_x, ball_y = window_width // 2, window_height // 2
ball_radius = 20
ball_speed_x, ball_speed_y = 2, 1
ball_color = hapi.color["blue"]  

# Effects
size_change_rate = 0.1  
speed_change_rate = 0.01  

def handle_events(event):
    if event.type == pygame.QUIT:
        hapi.is_running = False  
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            hapi.is_running = False


hapi.handle_events = handle_events


while hapi.is_running:
    
    hapi.background(bg_col)

    
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= window_width:
        ball_speed_x = -ball_speed_x
        ball_color = hapi.color["red"]  

    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= window_height:
        ball_speed_y = -ball_speed_y
        ball_color = hapi.color["green"]  

    
    ball_radius += size_change_rate
    if ball_radius <= 5 or ball_radius >= 30:
        size_change_rate = -size_change_rate  

    
    ball_speed_x += speed_change_rate
    ball_speed_y += speed_change_rate
    if abs(ball_speed_x) >= 8 or abs(ball_speed_y) >= 8:
        speed_change_rate = -speed_change_rate  

   
    hapi.fill(ball_color)
    hapi.circle(ball_x, ball_y, int(ball_radius))

    
    hapi.flip_display()
    hapi.event_loop()

pygame.quit()
