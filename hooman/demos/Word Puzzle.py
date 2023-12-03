from hooman import Hooman
import pygame  
import random

# Constants
WIDTH, HEIGHT = 800, 600

# Initialize Hooman
hm = Hooman(WIDTH, HEIGHT)

# List of words for the game
words = ['PYTHON', 'PYGAME', 'HOOMAN', 'DEMOS']

# Select a random word
selected_word = random.choice(words)
guessed_letters = ['_' for _ in selected_word]  # Initially, all letters are hidden

# Set up the display
hm.set_caption('Simple Word Puzzle Game')

# Handle events
def handle_events(event):
    print(event)
    if event.type == pygame.KEYDOWN:
        if event.key >= pygame.K_a and event.key <= pygame.K_z:
            letter = chr(event.key).upper()  # Convert key press to uppercase letter
            if letter in selected_word:
                # Replace '_' with correctly guessed letter
                for i in range(len(selected_word)):
                    if selected_word[i] == letter:
                        guessed_letters[i] = letter

hm.handle_events = handle_events

# Main game loop
while hm.is_running:
    hm.background(hm.color['white'])

    # Display guessed letters
    hm.fill(hm.color['black'])
    hm.font_size(36)
    hm.text(' '.join(guessed_letters), WIDTH / 2, HEIGHT / 2)

    hm.event_loop()
    hm.flip_display()
