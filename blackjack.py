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
WIDTH, HEIGHT = 1000, 1000

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack game")
print("yes")

# Variable to determine if the game is running
running = True

# Main game loop for when the game is running
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

# Quit the module
pygame.quit()
