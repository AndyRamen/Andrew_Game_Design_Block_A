#MAria Suarez

#10/20/2021

# Mouse position

# drawing rect

# moving object
# K_UP                  up arrow

# K_DOWN                down arrow

# K_RIGHT               right arrow

# K_LEFT                left arrow

import os
import pygame as py


#first thing

py.init()

#create window

height= 600
width = 600
boulder = py.Rect(width-300, height-200, 100, 200)
colors = {'red':(150,0,0),'green':(0,200,0), 'blue':(0,0,255), 'purple':(150, 0, 150), 'white':(255,255,255), 'black':(0,0,0) }
screen=py.display.set_mode((width, height))
myColor= colors.get('black')
screen.fill(myColor)
py.display.set_caption("Moving Square")
py.display.flip()

#parameters to define our square
x=width/2
y=height/2
wbox=50
hbox=50

#creating object square and the boulder obstacle
square=py.Rect(x,y,wbox, hbox )
objColor=colors.get('red')
boulderColor = colors.get('blue')
py.draw.rect(screen, objColor, square)
py.draw.rect(screen, boulderColor, boulder)
py.display.update()
#create speed to move the object on the screen
speed = 10
run=True #Variable to control the main loop
#boolean to check for jump
Jumping=False

jumpCount=10
move = True
while run:
    # for eve in py.event.get():
    #     if eve.type == py.QUIT:
    #         run = False
    #         py.quit()
        # elif eve.type == py.MOUSEBUTTONDOWN:
        #     mouse_pressed = py.mouse.get_pressed()
        #     if mouse_pressed[0]: #Left mouse button clicked
        #         mouse_pos = py.mouse.get_pos()
    #     #         print(mouse_pos)
    py.time.delay(100)
    for anyThing in py.event.get():
        if anyThing.type == py.QUIT:
            run =False
    keyPressed= py.key.get_pressed()
    if square.y <= (height-boulder.height-hbox): #If the red box is entirely above the boulder
        if keyPressed[py.K_RIGHT] and square.x <width-wbox-speed:
            square.x += speed
        elif keyPressed[py.K_LEFT] and square.x>speed-5:
            square.x -= speed
    elif square.x <= (boulder.x-wbox): #If bottom of red box is below top of boulder and to its left
        if keyPressed[py.K_RIGHT] and (square.x+wbox+speed)<=boulder.x:
            square.x += speed
        elif keyPressed[py.K_LEFT] and square.x>speed-5:
            square.x -= speed
    elif square.x >= boulder.x: #If bottom of red box is below top of boulder and to its right
        if keyPressed[py.K_RIGHT] and square.x <width-wbox-speed:
            square.x += speed
        elif keyPressed[py.K_LEFT] and (square.x-speed)>=(boulder.x+boulder.width):
            square.x -= speed
    
    if not(Jumping):
        if keyPressed[py.K_DOWN] and square.y < height-hbox-speed:
            if not(boulder.collidepoint(square.x, square.y+hbox+speed-1)) and not(boulder.collidepoint(square.x+wbox-1, square.y+hbox+speed-1)):
                #Go down only if the bottom of red square won't go past the top of boulder
                square.y += speed
        elif keyPressed[py.K_UP] and square.y>speed-5:
            square.y -= speed
        elif keyPressed[py.K_SPACE]:
            Jumping = True
    else:
        if jumpCount >= -10:
            newYCoord = square.y - jumpCount* abs(jumpCount)*0.5
            # if (newYCoord+hbox)>boulder.y and square.x>=boulder.x and square.x<(boulder.x+boulder.width):
            #     #If red square is on top of boulder and would land past the top boulder, make it stop right on top of boulder
            #     square.y = boulder.y - hbox
            #     jumpCount = 10
            #     Jumping = False
            # else: 
            square.y = newYCoord
            jumpCount -= 1
        else:
            jumpCount = 10
            Jumping = False
    # if square.x <= 500 and square.x >= 400 and square.y ==500:
    #     Jumping = False    
#(400, 500) and (500,500)
    # if(py.Rect.collidepoint(boulder, (square.x+wbox/2. square.y))):
    #     move = False
    #     square.x = square.x-wbox
    #     move = True
    # if square.y >= width >= 300:
    screen.fill(myColor)
    py.draw.rect(screen, objColor, square)
    py.draw.rect(screen, boulderColor, boulder)
    py.display.flip()

py.quit()