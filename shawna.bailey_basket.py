""" basket.py
    illustrates basic motion
    image loading
    move laundry basket
"""


#Initialize
import pygame

def main():
    pygame.init()

    #Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("basket!")

    #Entities
    #green background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill("green")

    #load an image
    basket = pygame.image.load("basket.png")
    basket = basket.convert_alpha()
    basekt = pygame.transform.scale(basket, (100, 100))

    # set up some basket variables
    basket_x = 0
    basket_y = 200

    #ACTION

        #Assign
    clock = pygame.time.Clock()
    keepGoing = True

        #Loop
    while keepGoing:

        #Time
        clock.tick(30)

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        #modify basket value
        basket_x += 5
        #check boundaries
        if basket_x > screen.get_width():
            basket_x = 0

        #Refresh screen
        screen.blit(background, (0, 0))
        screen.blit(basket, (basket_x, basket_y))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()