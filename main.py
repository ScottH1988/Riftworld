import pygame
import os
pygame.init()

# Main Variables
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # creates the intial surface for the game
# WIDTH,HEIGHT = WIN.get_size() # how to get the screen size of a user to use as the surface dimensions
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Riftworld", "assets", "background.png")), (WIDTH, HEIGHT))
PUG = pygame.transform.scale2x(pygame.image.load(os.path.join("Riftworld", "assets", "boy.png"))) # doubles the size of the images uing "pygame.transform.scale2x"



# Game window name & icon
pygame.display.set_caption("Welcome to Riftwold!")
icon = pygame.image.load(os.path.join("Riftworld", "assets", "castle.png"))
pygame.display.set_icon(icon)

# Draw window function to diplay background and character images v1.0
def draw_Window():
    WIN.blit(BACKGROUND, (0,0))
    

    WIN.blit(PUG, (10, 420))
    
    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             run = False
             pygame.quit()

draw_Window()    




main()
if __name__ == "__main__":
    main()



 