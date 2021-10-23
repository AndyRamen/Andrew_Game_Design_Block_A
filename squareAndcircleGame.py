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
    pygame.draw.circle(window, 'red', (xc,yc), radius)
    pygame.display.flip()

def rectDelete():
    window.fill('black')
    pygame.display.flip()
    pygame.draw.rect(window, colors.get('blue'), rect2)
    pygame.draw.circle(window, 'red', (xc,yc), radius)
    pygame.display.flip()

    
while check:
    # height=input("Height of the window: (100 - 1000): ")
    # width = input("Width of the window: (100 - 1000): ")
    width = 500
    height = 500
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
    width2 =random.randint(5, 495)
    height2 =random.randint(5, 495)
    rect=pygame.Rect(width/2,height/2, wbox, hbox)
    rect2 = pygame.Rect(width2/2, height2/2, wbox, hbox)
    #Circle needs (x,y,radius) Radius is wbox/2
    xc = random.randint(25, 100)
    yc = random.randint(25, 100)
    radius = wbox/2
    xsr = rect.x+wbox
    ysb = rect.y - hbox
    xsl = rect.x - hbox
    yst = rect.y
    #ball = pygame.surface.circle(xc, yc, r)
    #pygame.draw.circle(window, colors.get(str('blue')), ball)
    pygame.draw.rect(window, colors.get(str('blue')), rect)
    pygame.display.flip()
    pygame.draw.circle(window, 'red', (xc,yc), radius)
    circle = pygame.draw.circle(window, 'red', (xc,yc), radius)
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
    rectPos = (rect.x, rect.y)
    circlePos = (xc, yc)
    #How to get the position of the mouse
    #x,y=pygame.mouse.get_pos()
    #print("("+ str(x)+ " , "+str(y)+" )")
    keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_UP]: #and rect.y-speed>=0:
        rect.y -= speed
        rectMove()
    elif keyPressed[pygame.K_DOWN]: #and (rect.y+hbox+speed)<=height
        rect.y += speed
        rectMove()
    elif keyPressed[pygame.K_RIGHT]: #and (rect.x+wbox+speed)<=width
        rect.x += speed
        rectMove()
    elif keyPressed[pygame.K_LEFT]: #and rect.x-speed>=0:
        rect.x -=speed
        rectMove()
    print(rect.x, rect.y)
    if keyPressed[pygame.K_w] and yc>=30:
        yc -= speed
        rectMove()
    elif keyPressed[pygame.K_a] and xc-speed>=20:
        xc -= speed
        rectMove()
    elif keyPressed[pygame.K_s] and yc<=475:
        yc +=speed
        rectMove()
    elif keyPressed[pygame.K_d] and xc<=475:
        xc += speed
        rectMove()

    if rect.y>500:
        rect.y = 0
    elif rect.y<0:
        rect.y = 450
    elif rect.x>500:
        rect.x=0
    elif rect.x<0:
        rect.x = 450

    if xc >= rect.x and xc <= xsr:
        if (abs(yc - yst) <= radius) or (abs(yc - ysb) <= radius):
            #Touched on top or bottom edge
            rectDelete()
    elif yc >= rect.y and yc <= ysb:
        if (abs(xc - xsl)<= radius) or (abs(xc - xsr)<= radius):
            #Touched on right or left edge
            rectDelete()
    elif (xsl - xc) < radius:
        if (yst - yc) < radius:
            #Touched on top left corner
            window.fill('black')
            rectDelete()
        elif (yc - ysb) < radius:
            #Touched on bottom left corner
            rectDelete()
    elif (xc - xsr) < radius:
        if (yst - yc) < radius:
            #Touched on bottom left corner
            rectDelete()
        elif (yc - ysb) < radius:
            #Touched on bottom right corner
            rectDelete()
#POssible ideas:
#If pos is the same, no longer draw circle and create a new circle in a random place

pygame.quit()
#y+hbox is equal to height, you're at the border
#when y=0 you're at the border
#x=0
#x+wbox=width
#Make them stop once they hit the border. Do nothing once it reaches there
#If x+wbox=width do nothing.