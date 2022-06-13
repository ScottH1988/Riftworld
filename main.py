import pygame
pygame.init()

# Main Variables
WIN = pygame.display.set_mode() # creates the intial surface for the game
WIDTH,HEIGHT = WIN.get_size() # how to get the screen size of a user to use as the surface dimensions

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                run = False
                pygame.quit()






main()




 