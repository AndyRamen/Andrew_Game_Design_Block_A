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
bg = py.image.load("GameImages\\800x800space image.jpg")
screen.blit(bg, (0,0))
#screen.fill(myColor)
py.display.set_caption("Moving Square")
py.display.flip()

#parameters to define our square
x=width/2
y=height/2
wbox=50
hbox=50

walkRight = [py.image.load("GameImages\\Pygame-Tutorials-master\\Game\\R1.png"), py.image.load('R2.png'), py.image.load('R3.png'), py.image.load('R4.png'), py.image.load('R5.png'), py.image.load('R6.png'), py.image.load('R7.png'), py.image.load('R8.png'), py.image.load('R9.png')]
walkLeft = [py.image.load('L1.png'), py.image.load('L2.png'), py.image.load('L3.png'), py.image.load('L4.png'), py.image.load('L5.png'), py.image.load('L6.png'), py.image.load('L7.png'), py.image.load('L8.png'), py.image.load('L9.png')]
bg = py.image.load('bg.jpg')
char = py.image.load('standing.png')
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
clock = py.time.clock

def redrawGameWindow():
    global walkCount
    bg = py.image.load("GameImages\\800x800space image.jpg")
    screen.blit(bg, (0,0))
    py.draw.rect(screen, objColor, square)
    py.draw.rect(screen, boulderColor, boulder)
    py.display.flip()

    if walkCount +1 >= 27:
        walkCount = 0
    if left:
        screen.blit(walkLeft(walkCount//3))
        walkCount += 1
    elif right:
        screen.blit(walkRight(walkCount//3))
        walkCount += 1
    else: 
        screen.blit(char, (x,y))
    py.display.update()
#Just put character sprite into each movement thing and just replace square.x with fig.x and stuff
jumpCount=10
move = True
left = False
right = False
walkCount = 0
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
    clock.tick(27)
    for anyThing in py.event.get():
        if anyThing.type == py.QUIT:
            run =False
    keyPressed= py.key.get_pressed()
    if square.y <= (height-boulder.height-hbox): #If the red box is entirely above the boulder
        if keyPressed[py.K_RIGHT] and square.x <width-wbox-speed:
            square.x += speed
            right = True
            left = False
        elif keyPressed[py.K_LEFT] and square.x>speed-5:
            square.x -= speed
            right = False
            left = True
    elif square.x <= (boulder.x-wbox): #If bottom of red box is below top of boulder and to its left
        if keyPressed[py.K_RIGHT] and (square.x+wbox+speed)<=boulder.x:
            square.x += speed
            right = True
            left = False
        elif keyPressed[py.K_LEFT] and square.x>speed-5:
            square.x -= speed
            right = False
            left = True
    elif square.x >= boulder.x: #If bottom of red box is below top of boulder and to its right
        if keyPressed[py.K_RIGHT] and square.x <width-wbox-speed:
            square.x += speed
            right = True
            left = False
        elif keyPressed[py.K_LEFT] and (square.x-speed)>=(boulder.x+boulder.width):
            square.x -= speed
            right = False
            left = True
    
    if not(Jumping):
        if keyPressed[py.K_DOWN] and square.y < height-hbox-speed:
            if not(boulder.collidepoint(square.x, square.y+hbox+speed-1)) and not(boulder.collidepoint(square.x+wbox-1, square.y+hbox+speed-1)):
                #Go down only if the bottom of red square won't go past the top of boulder
                square.y += speed
                right = False
                left = False
        elif keyPressed[py.K_UP] and square.y>speed-5:
            square.y -= speed
            right = False
            left = False
        elif keyPressed[py.K_SPACE]:
            Jumping = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            newYCoord = square.y - jumpCount* abs(jumpCount)*0.5
            square.y = newYCoord
            jumpCount -= 1
            square.y+= 2
        else:
            jumpCount = 10
            Jumping = False
    redrawGameWindow()
    # if square.x <= 500 and square.x >= 400 and square.y ==500:
    #     Jumping = False    
#(400, 500) and (500,500)
    # if(py.Rect.collidepoint(boulder, (square.x+wbox/2. square.y))):
    #     move = False
    #     square.x = square.x-wbox
    #     move = True
    # if square.y >= width >= 300:
    #screen.fill(myColor)
    bg = py.image.load("GameImages\\800x800space image.jpg")
    screen.blit(bg, (0,0))
    py.draw.rect(screen, objColor, square)
    py.draw.rect(screen, boulderColor, boulder)
    py.display.flip()

py.quit()