#Andrew Cai 10/25/21
#Learning fonts and blit

from typing import Text
import pygame as py, os, random, time

py.init()
menuMessages = ["Instructions", "Level 1", "Level 2", "Scoreboard", "Settings", "Exit"]
messages = ["Background Color", "Screen Size"]
screenSizeMessages = ["700x700", "800x800", "850x850"]
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
width = 700
height = 700
# Define a list of Rects to store the main menu selection boxes
tempRect = py.Rect(0,0,5,5)
mainMenuRectList = [tempRect]
# Define a list of Rects to store the Settings selection boxes
settingsRectList = [tempRect]
# Define a list of Rects to store the Background Color selection boxes
backgroundColorsRectList = [tempRect]
# Define rect variables for each window's Back button
screenSizeRectList = [tempRect]
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

def ScreenSize_Menu():
    x = 40
    y = 90
    square.x = x
    square.y = y
    while len(screenSizeRectList) > 0:
        screenSizeRectList.pop() #Clear the list to star afresh
    for i in range(0, len(screenSizeMessages)):
        word = screenSizeMessages[i]
        currentScreenSizeRect = py.draw.rect(window, WHITE, square)
        screenSizeRectList.append(currentScreenSizeRect) #Store all setting menu rects in a list
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
    instructionBackRect = display_subtitle("Back", 660)
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
    bg1 = py.image.load('GameImages\planetwithcraters.jpg')
    window.blit(bg1, (0,0))
    targetCount = 12
    spaceship = py.image.load('GameImages\mainshipResized.png')
    window.blit(spaceship, (50, 600))
    target1 = py.image.load('GameImages\enemy ship 2Resized.png')
    target1Special = py.image.load('GameImages\enemy ship 2Resized.png')
    target2 = py.image.load('GameImages\enemy ship 1Resized.png')
    target3 = py.image.load('GameImages\enemy ship 3Resized.png')
    target4 = py.image.load('GameImages\enemy ship 4Resized.png')

    window.blit(target1Special, (30,5))
    window.blit(target2, (80,5))
    window.blit(target3, (130,5))
    window.blit(target4, (180,5))
    window.blit(target1, (230,5))
    window.blit(target2, (280,5))
    window.blit(target3, (330,5))
    window.blit(target4, (380,5))
    window.blit(target1, (430,5))
    window.blit(target2, (480,5))
    window.blit(target3, (530,5))
    window.blit(target4, (580,5))
    window.blit(target1, (630,5))
    hVelocity = 5
    vVelocity = 5
    targetRefreshFreq = 5
	# loop through (number of targets - 1): #because first target is almost in the list
	# 	create a target rect sized based on a predefined image appropriate for gameLevel
	# 	position the target rect a set distance from the previous rect in targetList
	# 	append the new target rect to targetList
	# end loop
    target1LeftMostRect = py.Rect(width - 670, height - 695, 50, 50)
    target1RightMostRect = py.Rect(width - 70, height - 695, 50, 50)
    spaceshipRect = py.Rect(width - 650, height - 100, 50, 50)
    targetlist = [target1LeftMostRect]
    bulletRectList = []
    continuegame = True
    loopcount = 0
    hDirection = "right"
    moveDown = False
    totalScore = 0
    #screen.fill(myColor)
    #py.display.set_caption("Space Invaders Level 1")
    level1BackRect = display_subtitle("Quit", 660)
    py.display.flip()
    while continuegame:
        if len(targetlist) == 0:
            ScoreFile = open('SpaceInvadersScore.txt', 'a')
            ScoreFile.write("\n The Score: \t" + str(totalScore))
        loopcount += 1
        if loopcount == targetRefreshFreq:
            advanceTargets = True
            loopcount = 0
        else:
            advanceTargets = False
	    #clear the display window so everything can be redrawn

        # if hDirection == "right": 
        #     if target1RightMostRect + 5 > width:
		# 		#move down and start moving left
        #         hDirection = "left"
        #         moveDown = True
        #     else: 
        #         moveDown = False



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
    bg2 = py.image.load('GameImages\\nubula.jpg')
    window.blit(bg2, (0,0))
    py.display.set_caption("Space Invaders Level 2")
    level2BackRect = display_subtitle("Quit", 660)
    py.display.flip()

def display_Scoreboard():
    global scoreboardBackRect
    window.fill(bkgColor)
    display_TITLE("Scoreboard", 30)
    scoreboardBackRect = display_subtitle("Back", 660)
    py.display.update()
    return DISPLAY_SCOREBOARD

def display_Settings():
    global settingsBackRect
    window.fill(bkgColor)
    display_TITLE("--Settings--", 20)
    Settings_Menu()
    py.display.update()
    settingsBackRect = display_subtitle("Back", 660)
    py.display.set_caption("Settings Window")
    py.display.update()
    return DISPLAY_SETTINGS

def display_Background_Colors():
    window.fill(bkgColor)
    display_TITLE("Background Color", 20)
    backgroundColorBackRect = display_subtitle("Back", 660)
    BKG_Color()
    py.display.update()
    return DISPLAY_SETTINGS_BKGCOLOR

# def display_Object_Colors():
#     window.fill(bkgColor)
#     display_TITLE("Object Color", 20)
#     objectColorBackRect = display_subtitle("Back", 560)
#     py.display.update()
#     return DISPLAY_SETTINGS_OBJCOLOR

def display_Settings_ScrnSize():
    window.fill(bkgColor)
    display_TITLE("Screen Size", 20)
    screenSizeBackRect = display_subtitle("Back", 660)
    ScreenSize_Menu()
    py.display.update()
    return DISPLAY_SETTINGS_SCNSIZE

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
    if mouse_pos[0] >= 320 and mouse_pos[0] <= 380 and mouse_pos[1] >= 660 and mouse_pos[1] <= 680: 
        currentDisplay = display_Menu()
        #800x800: 

def backButtonToSettings():
    global currentDisplay
    if mouse_pos[0] >= 320 and mouse_pos[0] <= 380 and mouse_pos[1] >= 660 and mouse_pos[1] <= 680:
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
                        currentDisplay = display_Settings_ScrnSize()
                    # elif settingsRectList[2].collidepoint(mouse_pos[0], mouse_pos[1]):
                    #     currentDisplay = display_Settings_ScrnSize()
                    # elif settingsRectList[3].collidepoint(mouse_pos[0], mouse_pos[1]):
                    #     #print("Settings: Clicked on Screen Size")
                    #     currentDisplay = display_Settings_ScrnSize()
                    else:
                        continue
                elif currentDisplay == DISPLAY_SETTINGS_SCNSIZE:
                    ScreenSize_Menu()
                    backButtonToSettings()
                    if screenSizeRectList[0].collidepoint(mouse_pos[0], mouse_pos[1]):
                        width = 700
                        height = 700
                        window = py.display.set_mode((width, height))
                    elif screenSizeRectList[1].collidepoint(mouse_pos[0], mouse_pos[1]):
                        width = 800
                        height = 800
                        window = py.display.set_mode((width, height))
                    elif screenSizeRectList[2].collidepoint(mouse_pos[0], mouse_pos[1]):
                        width = 850
                        height = 850
                        window = py.display.set_mode((width, height))
                    else:
                        continue
                # elif currentDisplay == DISPLAY_SETTINGS_OBJCOLOR:
                #     backButtonToSettings() #Clicked back on object color
                #         #print("Settings/Object Color: Clicked on Back")
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
            
