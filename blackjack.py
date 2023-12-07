""" 
This module is a Pygame based blackjack game, where
the player is dealt cards and try to beat the dealer
with a hand as close to but not exceeding 21 as possible.
The player can customize game settings at the start of the game.
"""
# This is the main file for final project
import pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
black = (0, 0, 0)
white = (255, 255, 255)
DARK = (100, 100, 100)      # Dark color
LIGHT = (170, 170, 170)     # Light color
red = (255, 0, 0)
font = pygame.font.SysFont('Times New Roman', 35)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack game")

# Variable to determine if the game is running
running = True

# Main game loop for when the game is running
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)

    # Draw buttons for betting options
    pygame.draw.rect(screen, red, [50, 250, 100, 40], 1, 1)
    pygame.draw.rect(screen, red, [50, 150, 100, 40], 1, 1)
    pygame.draw.rect(screen, red, [50, 50, 100, 40], 1, 1)

    # Update portion of the screen
    pygame.display.flip()

# Quit the module
pygame.quit()
