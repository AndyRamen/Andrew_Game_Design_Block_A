#Andrew Cai
#10/15/21
#Today we are going to learn  display, opening windows, 
# changing size window, basic game loop

import pygame, random
pygame.init()

invalidInput = True
height= " "
width= " "
colors= {'red': (255,0,0), 'green':(0,255,0), 'blue':(0,0,255), 'purple':(150,0,150), 'black': (0,0,0)} #black is like a key and its associated to a value
Thecolors = ['red', 'green', 'blue', 'purple', 'black']

def rectMove():
    window.fill('black') #Clear entire display window
    pygame.display.flip()
    #If rect is out of bounds, flip it to the other side of the display
    if rect.y > height:
        rect.y = 0
    elif rect.y < 0:
        rect.y = height - hbox
    elif rect.x > width:
        rect.x = 0
    elif rect.x < 0:
        rect.x = width - wbox
    pygame.draw.rect(window, colors.get('blue'), rect) #Redraw rectangle
    pygame.draw.circle(window, 'red', (xc,yc), radius) #Redraw circle
    pygame.display.flip()

def rectDelete(currentRect, newRadius):
    window.fill('black')
    pygame.display.flip()
    pygame.draw.rect(window, colors.get('blue'), currentRect, -1) #Undraw original rectangle
    pygame.draw.circle(window, 'red', (xc,yc), newRadius) #Redraw the circle where it is with the specified new radius
    xRect2 = random.randint(0, width - wbox)
    yRect2 = random.randint(0, height - hbox)
    newRect = pygame.Rect(xRect2, yRect2, wbox, hbox)
    pygame.draw.rect(window, colors.get('blue'), newRect) #Draw a new rectangle at a random position
    pygame.display.flip()
    return newRect

def circleCheck(currentRadius):
    #Pass current radius in and return new increased radius, but if it decides radius cannot be increased then return 0
    newRadius = currentRadius + 10
    if newRadius >= width/2 or newRadius >= height/2:
        newRadius = 0
    return newRadius


width = 500
height = 500
Mycolor = random.choice(Thecolors)
run = True
    
#while invalidInput:
    # height=input("Height of the window: (100 - 1000): ")
    # width = input("Width of the window: (100 - 1000): ")

 #   try:
        # height = int(height)
        # width = int(width)
        # if height<1001 and height>99 and width<1001 and width>99:
        #     #Round to nearest teen
        #     height = height/10 + 0.5
        #     height = int(height) * 10
        #     width = width/10 + 0.5
        #     width = int(width) * 10
        #     invalidInput = False
    #     else:
    #         print("Invalid width or height!\n")
    #         invalidInput = True
    #         run = False
    # except ValueError:
    #     print("Invalid width or height!\n")
    #     invalidInput = True
    #     run = False

color=colors.get(str(Mycolor))
window = pygame.display.set_mode((height,width))
window.fill(('black')) #RGB- colors in comp sci are either Red, Green or Blue, or a combination of them. red=255, FF green=255,FF blue=255, FF, 
#refresh window with new color
pygame.display.set_caption("My game Window")
pygame.display.flip()
hbox=50 
wbox=50
speed=5
rect = pygame.Rect(width/2, height/2, wbox, hbox)
xc = random.randint(25, 100)
yc = random.randint(25, 100)
radius = wbox/2
pygame.draw.rect(window, colors.get(str('blue')), rect)
circleRect = pygame.draw.circle(window, 'red', (xc,yc), radius)
pygame.display.flip()
run = True

#Main loop for the game:
while run:
    pygame.time.delay(20)
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            run= False


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
    elif keyPressed[pygame.K_w] and (yc-speed-radius)>=0:
        yc -= speed
        rectMove()
    elif keyPressed[pygame.K_a] and (xc-speed-radius)>=0:
        xc -= speed
        rectMove()
    elif keyPressed[pygame.K_s] and (yc+speed+radius)<=height:
        yc +=speed
        rectMove()
    elif keyPressed[pygame.K_d] and (xc+speed+radius)<=width:
        xc += speed
        rectMove()
    else:
        continue

    shapesTouched = False
    if xc >= rect.x and xc <= (rect.right):
        if (rect.y-yc) > 0 and (rect.y-yc) <= radius:
            print("Touched on top edge")
            shapesTouched = True
        elif (yc - rect.bottom) > 0 and (yc - rect.bottom) <= radius:
            print("Touched on bottom edge")
            shapesTouched = True
    elif yc >= rect.y and yc <= (rect.bottom):
        if (rect.x - xc) > 0 and (rect.x - xc) <= radius:
            print("Touched on left edge")
            shapesTouched = True
        elif (xc - rect.right) > 0 and (xc - rect.right) <= radius:
            print("Touched on right edge")
            shapesTouched = True
    elif (rect.x - xc) > 0 and (rect.x - xc) < radius:
        if (rect.y - yc) > 0 and (rect.y - yc) < radius:
            print("Touched on top left corner")
            shapesTouched = True
        elif (yc - rect.bottom) > 0 and (yc - rect.bottom) < radius:
            print("Touched on bottom left corner")
            shapesTouched = True
    elif (xc - rect.right) > 0 and (xc - rect.right) < radius:
        if (rect.y - yc) > 0 and (rect.y - yc) < radius:
            print("Touched on top right corner")
            shapesTouched = True
        elif (yc - rect.bottom) > 0 and (yc - rect.bottom) < radius:
            print("Touched on bottom right corner")
            shapesTouched = True
    else:
        continue
    
    if shapesTouched:
        radius = circleCheck(radius)
        if radius > 0:
            rect = rectDelete(rect, radius)
        else:
            print("Circle too large to fit! Ending game.")
            run = False
    else:
        continue

pygame.display.quit()
