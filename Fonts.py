#Andrew Cai 10/25/21
#Learning fonts and blit

from typing import Text
import pygame as py, os, random, time

py.init()
menuMessages = ["Instructions", "Level 1", "Level 2", "Scoreboard", "Settings", "Exit"]
messages = ["Background Color", "Object Color", "Sound on/off", "Screen Size"]
backgroundColors = {'Green': (0,128,0), 'Orange': (255,165,0), 'Black': (0,0,0)}
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


def display_Menu():
    x = 40
    y = 90
    square.x = x
    square.y = y
    while len(mainMenuRectList) > 0:
        mainMenuRectList.pop() #Clear the list to star afresh
    window.fill(bkgColor)
    display_TITLE("--Main Menu--", 20)
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
    window.fill(bkgColor)
    display_TITLE("Instructions:", 30)
    instructionBackRect = display_subtitle("Back", 560)
    #print("Inside display_instructions: rect", instructionBackRect.topleft, instructionBackRect.topright, instructionBackRect.bottomleft, instructionBackRect.bottomright)
    py.display.update()
    return DISPLAY_INSTRUCTIONS

def display_Level1():
    window.fill(bkgColor)
    display_TITLE("Level 1", 30)
    level1BackRect = display_subtitle("Back", 560)
    py.display.update()
    return DISPLAY_LEVEL1

def display_Level2():
    window.fill(bkgColor)
    display_TITLE("Level 2", 30)
    level2BackRect = display_subtitle("Back", 560)
    py.display.update()
    return DISPLAY_LEVEL2

def display_Scoreboard():
    window.fill(bkgColor)
    display_TITLE("Scoreboard", 30)
    scoreboardBackRect = display_subtitle("Back", 560)
    py.display.update()
    return DISPLAY_SCOREBOARD

def display_Settings():
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
                    #if mouse_pos[0] >= 40 and mouse_pos[0] <= 65 and mouse_pos[1] >= 90 and mouse_pos[1] <= 114: #Clicked on instructions
                    if mainMenuRectList[0].collidepoint(mouse_pos[0], mouse_pos[1]):
                        currentDisplay = display_Instructions()    
                        #print("After display_instructions: rect", instructionBackRect.topleft, instructionBackRect.topright, instructionBackRect.bottomleft, instructionBackRect.bottomright)
                        #print("Main Menu: Clicked on Instructions")
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
                elif currentDisplay == DISPLAY_INSTRUCTIONS:
                    if mouse_pos[0] >= 270 and mouse_pos[0] <= 330 and mouse_pos[1] >= 560 and mouse_pos[1] <= 580: #Clicked on back on instructions
                    #if instructionBackRect.collidepoint(mouse_pos[0], mouse_pos[1]):
                        #print("Instructions: Clicked on Back")
                        currentDisplay = display_Menu()
                elif currentDisplay == DISPLAY_LEVEL1:
                    if mouse_pos[0] >= 270 and mouse_pos[0] <= 330 and mouse_pos[1] >= 560 and mouse_pos[1] <= 580: #Clicked on back on level 1
                        #print("Level 1: Clicked on Back")
                        currentDisplay = display_Menu()
                elif currentDisplay == DISPLAY_LEVEL2:
                    if mouse_pos[0] >= 270 and mouse_pos[0] <= 330 and mouse_pos[1] >= 560 and mouse_pos[1] <= 580: #Clicked on back on level 1
                        #print("Level 2: Clicked on Back")
                        currentDisplay = display_Menu()
                elif currentDisplay == DISPLAY_SCOREBOARD:
                    if mouse_pos[0] >= 270 and mouse_pos[0] <= 330 and mouse_pos[1] >= 560 and mouse_pos[1] <= 580: #Clicked on back on level 1
                        #print("Scoreboard: Clicked on Back")
                        currentDisplay = display_Menu()
                elif currentDisplay == DISPLAY_SETTINGS:
                    if mouse_pos[0] >= 270 and mouse_pos[0] <= 330 and mouse_pos[1] >= 560 and mouse_pos[1] <= 580: #Clicked on back on settings
                        #print("Settings: Clicked on Back")
                        currentDisplay = display_Menu()
                    elif settingsRectList[0].collidepoint(mouse_pos[0], mouse_pos[1]):
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
                    if mouse_pos[0] >= 270 and mouse_pos[0] <= 330 and mouse_pos[1] >= 560 and mouse_pos[1] <= 580:
                        currentDisplay = display_Settings()
                elif currentDisplay == DISPLAY_SETTINGS_OBJCOLOR:
                    if mouse_pos[0] >= 270 and mouse_pos[0] <= 330 and mouse_pos[1] >= 560 and mouse_pos[1] <= 580: #Clicked back on object color
                        #print("Settings/Object Color: Clicked on Back")
                        currentDisplay = display_Settings()
                elif currentDisplay == DISPLAY_SETTINGS_BKGCOLOR:
                    BKG_Color()
                    py.display.update
                    if backgroundColorsRectList[0].collidepoint(mouse_pos[0], mouse_pos[1]):
                    #if mouse_pos[0] >= 40 and mouse_pos[0] <= 90 and mouse_pos[1] >= 90 and mouse_pos[1] <= 115: #Changes color to green
                        bkgColor = GREEN
                        currentDisplay = display_Background_Colors()
                    if backgroundColorsRectList[1].collidepoint(mouse_pos[0], mouse_pos[1]):
                    #elif mouse_pos[0] >= 40 and mouse_pos[0] <= 65 and mouse_pos[1] >= 170 and mouse_pos[1] <= 195: #Changes color to orange
                        bkgColor = ORANGE
                        currentDisplay = display_Background_Colors()
                    if backgroundColorsRectList[2].collidepoint(mouse_pos[0], mouse_pos[1]):
                    #elif mouse_pos[0] >= 40 and mouse_pos[0] <= 65 and mouse_pos[1] >= 250 and mouse_pos[1] <= 275: #Changes color to black
                        bkgColor = BLACK
                        currentDisplay = display_Background_Colors()
                    elif mouse_pos[0] >= 270 and mouse_pos[0] <= 330 and mouse_pos[1] >= 560 and mouse_pos[1] <= 580: #Clicked on back on bkg color
                        currentDisplay = display_Settings()
                    else:
                        continue
                else:
                    continue

py.display.quit
            
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


