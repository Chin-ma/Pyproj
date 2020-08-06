import pygame, sys

def run_my_game():
    pygame.init()
    screen = pygame.display.set_mode((1100, 700))#sets the display size
    pygame.display.set_caption('Kill the aliens')# sets title
    while True:
        for event in pygame.event.get():#tracks user actions
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()#updates screen according to latest input

run_my_game()