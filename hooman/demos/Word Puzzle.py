#!/usr/bin/env python
# coding: utf-8

# In[1]:


from hooman import Hooman
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

# List of words for the game
words = ['PYTHON', 'PYGAME', 'HOOMAN', 'DEMOS']

# Select a random word
selected_word = random.choice(words)
guessed_letters = ['_' for _ in selected_word]  # Initially, all letters are hidden

# Set up the display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simple Word Puzzle Game')

# Main game loop
running = True
while running:
    win.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key >= pygame.K_a and event.key <= pygame.K_z:
                letter = chr(event.key).upper()  # Convert key press to uppercase letter
                if letter in selected_word:
                    # Replace '_' with correctly guessed letter
                    for i in range(len(selected_word)):
                        if selected_word[i] == letter:
                            guessed_letters[i] = letter

    # Display guessed letters
    text = FONT.render(' '.join(guessed_letters), True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    win.blit(text, text_rect)

    pygame.display.flip()

# Quit Pygame
pygame.quit()

