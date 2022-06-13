from turtle import width
import pygame
import os
pygame.init()

# Main Variables
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # creates the intial surface for the game
# WIDTH,HEIGHT = WIN.get_size() # how to get the screen size of a user to use as the surface dimensions

# Game window name & icon
pygame.display.set_caption("Welcome to Riftwold!")
icon = pygame.image.load(os.path.join("Riftworld", "assets", "castle.png"))
pygame.display.set_icon(icon)


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             run = False
             pygame.quit()

    




main()
if __name__ == "__main__":
    main()



 