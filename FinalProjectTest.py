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
    pygame.display.set_caption("Space Invaders")
    pygame.display.flip()