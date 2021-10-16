import pygame
#first thing to do is initialize pygame
pygame.init()

check=True
height= " "
width= " "
colors= {'green':(0,255,0), 'blue':(0,0,255), 'purple':(150,0,150)} #black is like a key and its associated to a value
while check:
    height=input("Height of the window: (100 - 1000): ")
    width = input("Width of the window: (100-1000): ")
    color=input("what color do you prefer? green, blue, or purple?")

    try:
        height=int(height)
        width=int(width)
        check=False
    except ValueError:
        check=True

color=colors.get(str(color))

window=pygame.display.set_mode((height,width))
window.fill((color)) #RGB- colors in comp sci are either Red, Green or Blue, or a combination of them. red=255, FF green=255,FF blue=255, FF, 
# combination could be 100,120,255(EF)
window = pygame.display.flip() # refresh windo wiht new color
run=True

#main loop for the game:
while run:
    pygame.time.delay(1000)
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            run= False


pygame.quit()