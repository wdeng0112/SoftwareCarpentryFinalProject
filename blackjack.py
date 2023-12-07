# This is the main file for final project
import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

# Variable to determine if the game is running
running = True

# Main game loop for when the game is running
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

    pygame.display.flip()
pygame.quit()
