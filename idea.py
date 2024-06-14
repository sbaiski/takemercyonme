""" idea.py
    simplest possible pygame display
    demonstrates IDEA / ALTER model
    Andy Harris, 5/06
    Modded for CS 120, 2023
    NOTE: Will only run with Pygame installed
    """

def main():
    #I - Import and initialize
    import pygame
    pygame.init()

    #D - Display configuration
    screen = pygame.display.set_mode((480, 480))
    pygame.display.set_caption("Lets Play!")

    #E - Entities (just background for now)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((20, 5, 255))

    #A - Action (broken into ALTER steps)

        #A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True

        #L - Set up main loop
    while keepGoing:

        #T - Timer to set frame rate
        clock.tick(45)

        #E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        #R - Refresh display
        screen.blit(background, (2, 2))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()