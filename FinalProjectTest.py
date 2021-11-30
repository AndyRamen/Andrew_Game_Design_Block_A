import pygame
pygame.init()

height= 600
width = 600
run = True
while run:
    screen=pygame.display.set_mode((width, height))
    bg1 = pygame.image.load('GameImages\purple space.jpg')
    screen.blit(bg1, (0,0))
    #screen.fill(myColor)
    ship1 = pygame.image.load('GameImages\enemy ship 1Resized.png')
    screen.blit(ship1, (20,20))
    ship2 = pygame.image.load('GameImages\enemy ship 1Resized.png')
    screen.blit(ship2,  (70,20))
    ship3 = pygame.image.load('GameImages\enemy ship 4Resized.png')
    screen.blit(ship3, (120,20))
    pygame.display.set_caption("Space Invaders")
    pygame.display.flip()

pygame.display.quit()