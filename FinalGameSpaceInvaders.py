#Andrew Cai 10/25/21
#Learning fonts and blit

from typing import Text
import pygame as py, os, random, time

py.init()
menuMessages = ["Instructions", "Level 1", "Level 2", "Scoreboard", "Settings", "Exit"]
messages = ["Background Color", "Object Color", "Sound on/off", "Screen Size"]
backgroundColors = {'Green': (0,128,0), 'Orange': (255,165,0), 'Black': (0,0,0)}
colors= {'red': (255,0,0), 'green':(0,255,0), 'blue':(0,0,255), 'purple':(150,0,150), 'black': (0,0,0)}
bkgColorMessage = ["Green", "Orange", "Black"]
#backMessage = ["wfoi", "Back"]
GREEN = (90,128,0)
BLACK = (0,0,0)
WHITE=(255,255,255)
ORANGE = (255,140,0)
DISPLAY_MAIN_MENU = 0
DISPLAY_INSTRUCTIONS = 1
DISPLAY_LEVEL1 = 2
DISPLAY_SETTINGS = 3
DISPLAY_SETTINGS_BKGCOLOR = 4
DISPLAY_SETTINGS_OBJCOLOR = 5
DISPLAY_SETTINGS_SOUND = 6
DISPLAY_SETTINGS_SCNSIZE = 7
DISPLAY_LEVEL2 = 8
DISPLAY_SCOREBOARD = 9
currentDisplay = DISPLAY_MAIN_MENU
width = 600
height = 600
# Define a list of Rects to store the main menu selection boxes
tempRect = py.Rect(0,0,5,5)
mainMenuRectList = [tempRect]
# Define a list of Rects to store the Settings selection boxes
settingsRectList = [tempRect]
# Define a list of Rects to store the Background Color selection boxes
backgroundColorsRectList = [tempRect]
# Define rect variables for each window's Back button
instructionBackRect = py.Rect(5,5,5,5)
level1BackRect = py.Rect(10,10,5,5)
settingsBackRect = py.Rect(15,15,5,5)
backgroundColorBackRect = py.Rect(20,20,5,5)
objectColorBackRect = py.Rect(25,25,5,5)
level2BackRect = py.Rect(30,30,5,5)
scoreboardBackRect = py.Rect(35,35,5,5)
soundBackRect = py.Rect(40,40,5,5)
screenSizeBackRect = py.Rect(45,45,5,5)

window = py.display.set_mode((width,height))
py.display.set_caption("Menu Window")

# TITLE_FONT = py.font.SysFont(name, size, bold=False, italic=False )
TITLE_FONT = py.font.SysFont('Heveltica', 50)
SUBTITLE_FONT = py.font.SysFont('Heveltica', 40)
TEXT_FONT = py.font.SysFont('Heveltica', 25)
wbox = 25
hbox = 25
square = py.Rect(10,10, wbox, hbox)

def display_TITLE(message, y):
    py.time.delay(100)
    text = TITLE_FONT.render(message, 1, WHITE )
    x = width/2-text.get_width()/2
   # window.blit(text, (width/2-text.get_width()/2, height/2-text.get_height()/2))
    titleRect = window.blit(text, (x, y))
    py.display.update()
    return titleRect

def display_subtitle (message, y):
    py.time.delay(100)
    text = SUBTITLE_FONT.render(message, 1, WHITE)
    x = width/2 - text.get_width()/2
    subtitleRect = window.blit(text, (x,y))
    py.display.update()
    return subtitleRect

def display_text (message, y):
    py.time.delay(100)
    text = TEXT_FONT.render(message, 1, WHITE)
    x = width/2 - text.get_width()/2
    subtitleRect = window.blit(text, (x,y))
    py.display.update()
    return subtitleRect


def display_Menu():
    x = 40
    y = 90
    square.x = x
    square.y = y
    while len(mainMenuRectList) > 0:
        mainMenuRectList.pop() #Clear the list to star afresh
    window.fill(bkgColor)
    display_TITLE("--Space Invaders--", 20)
    for i in range(0, len(menuMessages)):
        word = menuMessages[i]
        currentMenuRect = py.draw.rect(window, WHITE, square)
        mainMenuRectList.append(currentMenuRect) #Store all menu rects in a list
        text = TITLE_FONT.render(word, 1, WHITE)
        window.blit(text, (x+wbox+10, y))
        py.display.flip()
        py.time.delay(100)
        y += 80
        square.y = y
    py.display.set_caption("Menu Window")
    py.display.update()
    return DISPLAY_MAIN_MENU

def Settings_Menu():
    x = 40
    y = 90
    square.x = x
    square.y = y
    while len(settingsRectList) > 0:
        settingsRectList.pop() #Clear the list to star afresh
    for i in range(0, len(messages)):
        word = messages[i]
        currentSettingRect = py.draw.rect(window, WHITE, square)
        settingsRectList.append(currentSettingRect) #Store all setting menu rects in a list
        text = TITLE_FONT.render(word, 1, WHITE)
        window.blit(text, (x+wbox+10, y))
        py.display.flip()
        py.time.delay(100)
        y += 80
        square.y = y

def BKG_Color():
    x = 40
    y = 90
    square.x = x
    square.y = y
    while len(backgroundColorsRectList) > 0:
        backgroundColorsRectList.pop() #Clear the list to star afresh
    for i in range(0,len(bkgColorMessage)):
        word = bkgColorMessage[i]
        currentBackgroundColorRect = py.draw.rect(window, WHITE, square)
        backgroundColorsRectList.append(currentBackgroundColorRect)
        text = TITLE_FONT.render(word, 1, WHITE)
        window.blit(text, (x+wbox+10, y))
        py.display.flip()
        py.time.delay(100)
        y += 80
        square.y = y

def display_Instructions():
    global instructionBackRect
    window.fill(bkgColor)
    display_TITLE("Instructions:", 30)
    instructionBackRect = display_subtitle("Back", 560)
    display_text("Aliens are invading our planet!", 80)
    display_text("Protect the planet until everyone has fully evacuted. Good luck.", 110)
    display_subtitle("--Controls--", 180)
    display_text("Left arrow key: Move left", 210)
    display_text("Right arrow key: Move right", 230)
    display_text("Spacebar: Shoot", 250)
    py.display.update()
    return DISPLAY_INSTRUCTIONS

def display_Level1():
    global level1BackRect
    #window.fill(bkgColor)
    # display_TITLE("Level 1", 30)
    # level1BackRect = display_subtitle("Back", 560)
    level1_Game()
    #Call score function here
    return DISPLAY_LEVEL1

def level1_Game():
    bg1 = py.image.load('GameImages\purple space.jpg')
    window.blit(bg1, (0,0))
    #screen.fill(myColor)
    py.display.set_caption("Space Invaders Level 1")
    level1BackRect = display_subtitle("Quit", 560)
    py.display.flip()
    #Add logic/game code here

def display_Level2():
    global level2BackRect
    # window.fill(bkgColor)
    # display_TITLE("Level 2", 30)
    # level2BackRect = display_subtitle("Back", 560)
    # py.display.update()
    level2_Game()
    return DISPLAY_LEVEL2

def level2_Game():
    bg2 = py.image.load('GameImages\\asteroid field.jpg')
    window.blit(bg2, (0,0))
    py.display.set_caption("Space Invaders Level 2")
    level2BackRect = display_subtitle("Quit", 560)
    py.display.flip()

def display_Scoreboard():
    global scoreboardBackRect
    window.fill(bkgColor)
    display_TITLE("Scoreboard", 30)
    scoreboardBackRect = display_subtitle("Back", 560)
    py.display.update()
    return DISPLAY_SCOREBOARD

def display_Settings():
    global settingsBackRect
    window.fill(bkgColor)
    display_TITLE("--Settings--", 20)
    Settings_Menu()
    py.display.update()
    settingsBackRect = display_subtitle("Back", 560)
    py.display.set_caption("Settings Window")
    py.display.update()
    return DISPLAY_SETTINGS

def display_Background_Colors():
    window.fill(bkgColor)
    display_TITLE("Background Color", 20)
    backgroundColorBackRect = display_subtitle("Back", 560)
    BKG_Color()
    py.display.update()
    return DISPLAY_SETTINGS_BKGCOLOR

def display_Object_Colors():
    window.fill(bkgColor)
    display_TITLE("Object Color", 20)
    objectColorBackRect = display_subtitle("Back", 560)
    py.display.update()
    return DISPLAY_SETTINGS_OBJCOLOR

def display_Settings_ScrnSize():
    window.fill(bkgColor)
    display_TITLE("Screen Size", 20)
    screenSizeBackRect = display_subtitle("Back", 560)
    py.display.update()
    return DISPLAY_SETTINGS_SCNSIZE

def rectMove():
    window.fill(bkgColor) #Clear entire display window
    py.display.flip()
    #If rect is out of bounds, flip it to the other side of the display
    if rect.y > height:
        rect.y = 0
    elif rect.y < 0:
        rect.y = height - hbox
    elif rect.x > width:
        rect.x = 0
    elif rect.x < 0:
        rect.x = width - wbox
    py.draw.rect(window, colors.get('blue'), rect) #Redraw rectangle
    py.draw.circle(window, 'red', (xc,yc), radius) #Redraw circle
    py.display.flip()

def rectDelete(currentRect, newRadius):
    window.fill(bkgColor)
    py.display.flip()
    py.draw.rect(window, colors.get('blue'), currentRect, -1) #Undraw original rectangle
    py.draw.circle(window, 'red', (xc,yc), newRadius) #Redraw the circle where it is with the specified new radius
    xRect2 = random.randint(0, width - wbox)
    yRect2 = random.randint(0, height - hbox)
    newRect = py.Rect(xRect2, yRect2, wbox, hbox)
    py.draw.rect(window, colors.get('blue'), newRect) #Draw a new rectangle at a random position
    py.display.flip()
    return newRect

def circleCheck(currentRadius):
    #Pass current radius in and return new increased radius, but if it decides radius cannot be increased then return 0
    newRadius = currentRadius + 10
    if newRadius >= width/2 or newRadius >= height/2:
        newRadius = 0
    return newRadius

def MainMenuWin():
    global currentDisplay
    global mouse_pos
    global run
    global mouse_pos
    global currentDisplay

    if mainMenuRectList[0].collidepoint(mouse_pos[0], mouse_pos[1]):
        currentDisplay = display_Instructions()    
        #print("After display_instructions: rect", instructionBackRect.topleft, instructionBackRect.topright, instructionBackRect.bottomleft, instructionBackRect.bottomright)
        print("Main Menu: Clicked on Instructions")
    #elif mouse_pos[0] >= 40 and mouse_pos[0] <= 65 and mouse_pos[1] >= 170 and mouse_pos[1] <=195: #Clicked on level 1
    elif mainMenuRectList[1].collidepoint(mouse_pos[0], mouse_pos[1]):   
        currentDisplay = display_Level1()
        #print("Main Menu: Clicked on Level 1")
    elif mainMenuRectList[2].collidepoint(mouse_pos[0], mouse_pos[1]):   
        currentDisplay = display_Level2()
        #print("Main Menu: Clicked on Level 2")
    elif mainMenuRectList[3].collidepoint(mouse_pos[0], mouse_pos[1]):   
        currentDisplay = display_Scoreboard()
        #print("Main Menu: Clicked on Scoreboard")
    #elif mouse_pos[0] >= 40 and mouse_pos[0] <= 65 and mouse_pos[1] >= 250 and mouse_pos[1] <=275: #Clicked on settings
    elif mainMenuRectList[4].collidepoint(mouse_pos[0], mouse_pos[1]):
        currentDisplay = display_Settings()
        #print("Main Menu: Clicked on Settings")
    #elif mouse_pos[0] >= 40 and mouse_pos[0] <= 65 and mouse_pos[1] >= 330 and mouse_pos[1] <= 355: #Clicked on exit
    elif mainMenuRectList[5].collidepoint(mouse_pos[0], mouse_pos[1]):
        #print("Main Menu: Clicked on Exit")
        run = False

def backButtonToMenu():
    global currentDisplay
    if mouse_pos[0] >= 270 and mouse_pos[0] <= 330 and mouse_pos[1] >= 560 and mouse_pos[1] <= 580: 
        currentDisplay = display_Menu()

def backButtonToSettings():
    global currentDisplay
    if mouse_pos[0] >= 270 and mouse_pos[0] <= 330 and mouse_pos[1] >= 560 and mouse_pos[1] <= 580:
        currentDisplay = display_Settings()

xc = random.randint(25, 100)
yc = random.randint(25, 100)
radius = wbox/2
rect = py.Rect(width/2, height/2, wbox, hbox)
hbox=50 
wbox=50
speed=5


#counter=0
run = True
bkgColor = BLACK
currentDisplay = display_Menu()

while run:
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run = False
            py.quit()
        elif eve.type == py.MOUSEBUTTONDOWN:
            mouse_pressed = py.mouse.get_pressed()
            if mouse_pressed[0]: #Left mouse button clicked
                mouse_pos = py.mouse.get_pos()
                print(mouse_pos)

                if currentDisplay == DISPLAY_MAIN_MENU:   
                    MainMenuWin()
                elif currentDisplay == DISPLAY_INSTRUCTIONS:
                    backButtonToMenu()#Clicked on back on instructions
                    #if instructionBackRect.collidepoint(mouse_pos[0], mouse_pos[1]):
                        #print("Instructions: Clicked on Back")
 
                        #print("Level 1: Clicked on Back
                elif currentDisplay == DISPLAY_LEVEL1:
                    backButtonToMenu()
                    #clicked on level 1 back
                elif currentDisplay == DISPLAY_LEVEL2:
                    backButtonToMenu() #Clicked on back on level 1
                        #print("Level 2: Clicked on Back")
                elif currentDisplay == DISPLAY_SCOREBOARD:
                    backButtonToMenu()#Clicked on back on level 1
                        #print("Scoreboard: Clicked on Back")

                elif currentDisplay == DISPLAY_SETTINGS:
                    backButtonToMenu()#Clicked on back on settings
                        #print("Settings: Clicked on Back")
                    if settingsRectList[0].collidepoint(mouse_pos[0], mouse_pos[1]):
                    #elif mouse_pos[0] >= 40 and mouse_pos[0] <= 65 and mouse_pos[1] >= 90 and mouse_pos[1] <= 115: #Clicked on bkg color
                        #print("Settings: Clicked on Background Color")
                        currentDisplay = display_Background_Colors()
                    elif settingsRectList[1].collidepoint(mouse_pos[0], mouse_pos[1]):
                    #elif mouse_pos[0] >= 40 and mouse_pos[0] <= 65 and mouse_pos[1] >= 170 and mouse_pos[1] <= 195: #Clicked on object color
                        #print("Settings: Clicked on Object Color")
                        currentDisplay = display_Object_Colors()
                    elif settingsRectList[2].collidepoint(mouse_pos[0], mouse_pos[1]):
                        print("Settings: Clicked on Sound On/Off")
                    elif settingsRectList[3].collidepoint(mouse_pos[0], mouse_pos[1]):
                        #print("Settings: Clicked on Screen Size")
                        currentDisplay = display_Settings_ScrnSize()
                    else:
                        continue
                elif currentDisplay == DISPLAY_SETTINGS_SCNSIZE:
                    backButtonToSettings()
                elif currentDisplay == DISPLAY_SETTINGS_OBJCOLOR:
                    backButtonToSettings() #Clicked back on object color
                        #print("Settings/Object Color: Clicked on Back")
                elif currentDisplay == DISPLAY_SETTINGS_BKGCOLOR:
                    BKG_Color()
                    py.display.update
                    backButtonToSettings()
                    if backgroundColorsRectList[0].collidepoint(mouse_pos[0], mouse_pos[1]):
                    #if mouse_pos[0] >= 40 and mouse_pos[0] <= 90 and mouse_pos[1] >= 90 and mouse_pos[1] <= 115: #Changes color to green
                        bkgColor = GREEN
                        currentDisplay = display_Background_Colors()
                    elif backgroundColorsRectList[1].collidepoint(mouse_pos[0], mouse_pos[1]):
                    #elif mouse_pos[0] >= 40 and mouse_pos[0] <= 65 and mouse_pos[1] >= 170 and mouse_pos[1] <= 195: #Changes color to orange
                        bkgColor = ORANGE
                        currentDisplay = display_Background_Colors()
                    elif backgroundColorsRectList[2].collidepoint(mouse_pos[0], mouse_pos[1]):
                    #elif mouse_pos[0] >= 40 and mouse_pos[0] <= 65 and mouse_pos[1] >= 250 and mouse_pos[1] <= 275: #Changes color to black
                        bkgColor = BLACK
                        currentDisplay = display_Background_Colors()
                    #Clicked on back on bkg color
                    else:
                        continue

                else:
                    continue

py.display.quit
#Hw 11/2/21: Add game into level 1
            
#             if mouse_pos[0] >= 40 and mouse_pos[0] <= 65 and mouse_pos[1] >= 90 and mouse_pos[1] <= 114:
#                 window.fill(BLACK)
#                 display_TITLE("Background Color", 70)
#             if mouse_pos[0] >= 40 and mouse_pos[0] <= 65 and mouse_pos[1] >=170 and mouse_pos[1] <=195:
#                 window.fill(BLACK)
#                 display_TITLE("Object Colors", 70) 
        #Will say (true, false, false) Left is left click, middle is middle click, right is right click
        #Hw 10/29/21: Add to main menu
        #Menu
        #Instructions
        #Level 1
        #Level 2
        #Settings
        #ScoreBoard
        #Exit


# def Display_back():
#     x = 200
#     y = 550
#     square.x = x
#     square.y = y
#     for i in range(0, len(messages)):
#         word = backMessage[i]
#         py.draw.rect(window, WHITE, square)
#         text = TITLE_FONT.render(word, 1, WHITE)
#         window.blit(text, (x+wbox+10, y))
#         py.display.flip()
#         py.time.delay(100)
#         y += 80
#         square.y = y


    #if counter == 0: (if want to work, indent)
    # display_TITLE("--SETTINGS--")
    # display_message1("Background Color")
    # display_message2("Object Colors")
    # display_message3("Sound On/Off") 
    # display_message4("Screen Size")
    #py.time.delay(10000)
    #counter +=1
    #Y increases downwards
    #X increases to the right

# def display_message1(message):
#     #py.time.delay(100)
#     text = subtitle.render(message, 1, WHITE )
#    # window.blit(text, (width/2-text.get_width()/2, height/2-text.get_height()/2))
#     window.blit(text, (width/2-text.get_width()/2, 90))
#     py.display.update()
#     #py.time.delay(100)

# def display_message2(message):
#     #py.time.delay(100)
#     text = subtitle.render(message, 1, WHITE )
#    # window.blit(text, (width/2-text.get_width()/2, height/2-text.get_height()/2))
#     window.blit(text, (width/2-text.get_width()/2, 170))
#     py.display.update()
#     #py.time.delay(100)

# def display_message3(message):
#     #py.time.delay(100)
#     text = subtitle.render(message, 4, WHITE )
#    # window.blit(text, (width/2-text.get_width()/2, height/2-text.get_height()/2))
#     window.blit(text, (width/2-text.get_width()/2, 250))
#     py.display.update()
#     #py.time.delay(100)

# def display_message4(message):
#     #py.time.delay(100)
#     text = subtitle.render(message, 4, WHITE )
#    # window.blit(text, (width/2-text.get_width()/2, height/2-text.get_height()/2))
#     window.blit(text, (width/2-text.get_width()/2, 330))
#     py.display.update()
#     #py.time.delay(100)




            #    elif currentDisplay == DISPLAY_LEVEL1:
            #         py.display.set_caption("My game Window")
            #         py.display.flip()
            #         hbox=50 
            #         wbox=50
            #         speed=5
            #         rect = py.Rect(width/2, height/2, wbox, hbox)
            #         xc = random.randint(25, 100)
            #         yc = random.randint(25, 100)
            #         radius = wbox/2
            #         py.draw.rect(window, colors.get(str('blue')), rect)
            #         circleRect = py.draw.circle(window, 'red', (xc,yc), radius)
            #         py.display.flip()
            #         keyPressed = py.key.get_pressed()
            #         if keyPressed[py.K_UP]: #and rect.y-speed>=0:
            #             rect.y -= speed
            #             rectMove()
            #         elif keyPressed[py.K_DOWN]: #and (rect.y+hbox+speed)<=height
            #             rect.y += speed
            #             rectMove()
            #         elif keyPressed[py.K_RIGHT]: #and (rect.x+wbox+speed)<=width
            #             rect.x += speed
            #             rectMove()
            #         elif keyPressed[py.K_LEFT]: #and rect.x-speed>=0:
            #             rect.x -=speed
            #             rectMove()
            #         elif keyPressed[py.K_w] and (yc-speed-radius)>=0:
            #             yc -= speed
            #             rectMove()
            #         elif keyPressed[py.K_a] and (xc-speed-radius)>=0:
            #             xc -= speed
            #             rectMove() 
            #         elif keyPressed[py.K_s] and (yc+speed+radius)<=height:
            #             yc +=speed
            #             rectMove()
            #         elif keyPressed[py.K_d] and (xc+speed+radius)<=width:
            #             xc += speed
            #             rectMove()
            #         else:
            #             continue

            #         shapesTouched = False
            #         if xc >= rect.x and xc <= (rect.right):
            #             if (rect.y-yc) > 0 and (rect.y-yc) <= radius:
            #                 #print("Touched on top edge")
            #                 shapesTouched = True
            #             elif (yc - rect.bottom) > 0 and (yc - rect.bottom) <= radius:
            #                 #print("Touched on bottom edge")
            #                 shapesTouched = True
            #         elif yc >= rect.y and yc <= (rect.bottom):
            #             if (rect.x - xc) > 0 and (rect.x - xc) <= radius:
            #                 #print("Touched on left edge")
            #                 shapesTouched = True
            #             elif (xc - rect.right) > 0 and (xc - rect.right) <= radius:
            #                 #print("Touched on right edge")
            #                 shapesTouched = True
            #         elif (rect.x - xc) > 0 and (rect.x - xc) < radius:
            #             if (rect.y - yc) > 0 and (rect.y - yc) < radius:
            #                 #print("Touched on top left corner")
            #                 shapesTouched = True
            #             elif (yc - rect.bottom) > 0 and (yc - rect.bottom) < radius:
            #                 #print("Touched on bottom left corner")
            #                 shapesTouched = True
            #         elif (xc - rect.right) > 0 and (xc - rect.right) < radius:
            #             if (rect.y - yc) > 0 and (rect.y - yc) < radius:
            #                 #print("Touched on top right corner")
            #                 shapesTouched = True
            #             elif (yc - rect.bottom) > 0 and (yc - rect.bottom) < radius:
            #                 #print("Touched on bottom right corner")
            #                 shapesTouched = True
            #         else:
            #             continue



