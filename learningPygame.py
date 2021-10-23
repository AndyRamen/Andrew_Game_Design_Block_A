#Andrew Cai
#10/15/21
#Today we are going to learn  display, opening windows, 
# changing size window, basic game loop

import pygame, random
#first thing to do is initialize pygame
pygame.init()

check=True
height= " "
width= " "
colors= {'red': (255,0,0), 'green':(0,255,0), 'blue':(0,0,255), 'purple':(150,0,150), 'black': (0,0,0)} #black is like a key and its associated to a value
Thecolors = ['red', 'green', 'blue', 'purple', 'black']

def rectMove():
    window.fill('black')
    pygame.display.flip()
    pygame.draw.rect(window, colors.get('blue'), rect)
    pygame.display.flip()
    
while check:
    height=input("Height of the window: (100 - 1000): ")
    width = input("Width of the window: (100 - 1000): ")
    Mycolor = random.choice(Thecolors)

    try:
        height = int(height)
        width = int(width)
        height = height/10 + 0.5
        height = int(height) * 10
        width = width/10 + 0.5
        width = int(width) * 10
        check=False
    except ValueError:
        print("waga")
        check=True

color=colors.get(str(Mycolor))
if height<1001 and height>99 and width<1001 and width>99:
    window = pygame.display.set_mode((height,width))
    window.fill(('black')) #RGB- colors in comp sci are either Red, Green or Blue, or a combination of them. red=255, FF green=255,FF blue=255, FF, 
    # combination could be 100,120,255(EF)
    pygame.display.flip() # refresh windo wiht new color
    pygame.display.set_caption("My game Window")
    pygame.display.flip()
    hbox=50 
    wbox=50
    speed=5
    rect=pygame.Rect(width/2,height/2, wbox, hbox)
    #Circle needs (x,y,radius) Radius is wbox/2
    # xc = wbox/2
    # yc = hbox/2
    # r = hbox/2
    # ball = pygame.circle(xc, yc, r)
    # pygame.draw.circle(window, colors.get(str('blue')), ball)
    pygame.draw.rect(window, colors.get(str('blue')), rect)
    pointer= pygame.draw.rect(window, colors.get(str('blue')), rect)
    pygame.display.flip()
    run=True

else: 
    print()
    print("Wrong")
    run=False
    

    #main loop for the game:
while run:
    pygame.time.delay(20)
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            run= False
    #How to get the position of the mouse
    #x,y=pygame.mouse.get_pos()
    #print("("+ str(x)+ " , "+str(y)+" )")
    keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_UP] and rect.y-speed>=0:
        rect.y -= speed
        rectMove()
    elif keyPressed[pygame.K_DOWN] and (rect.y+hbox+speed)<=height:
        rect.y += speed
        rectMove()
    elif keyPressed[pygame.K_RIGHT] and (rect.x+wbox+speed)<=width:
        rect.x += speed
        rectMove()
    elif keyPressed[pygame.K_LEFT] and rect.x-speed>=0:
        rect.x -=speed
        rectMove()




pygame.quit()
#y+hbox is equal to height, you're at the border
#when y=0 you're at the border
#x=0
#x+wbox=width
#Make them stop once they hit the border. Do nothing once it reaches there
#If x+wbox=width do nothing.