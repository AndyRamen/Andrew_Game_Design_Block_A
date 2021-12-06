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

#define global variables
bkgColor = BLACK
width =  700
height = 700
window = py.display.set_mode((width,height))
windowRect = window.get_rect()
tempRect = py.Rect(0,0,10,10)
targetList = [tempRect]
targetList.pop()
bulletList = [tempRect]
bulletList.pop()
bulletVel = 30
bulletWidth = 5
bulletHeight = 15
bulletColor = (255,0,0)
spaceShipRect = py.Rect(0,0,20,20)
spaceShipVel = 15

#define defauly horizontal and vertical target movement speeds
targetHVel = 5
targetVVel = 20
targetDirection = 1 #1 to move right and -1 to move left
TARGET_Y_POS = 20
totalScore = 0
ptsPerTarget = 100

#Define some constants to use as return value from the main game play function
GAME_CONTINUES = 0
PLAYER_WON = 1
PLAYER_LOST = 2
PLAYER_QUIT = 3

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
        py.time.delay(100)
        y += 80
        square.y = y
    py.display.flip()
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

def reset_game():
	global screen
	global targetList
	global bulletList
	global spaceShipRect
	global targetHVel
	global targetVVel
	global totalScore
	
	#clear the entire screen
	window = py.display.set_mode((width, height))
	windowRect = window.get_rect()

	#reset any global variables that may have been changed during game play
	spaceShipRect = py.Rect(0,0,20,20)
	targetHVel = 1
	targetVVel = 15
	totalScore = 0
	while len(targetList)>0:
		del targetList[0]
	while len(bulletList)>0:
		del bulletList[0]

def fire_bullet(bulletLimit):
    global bulletList
    global spaceShipRect

	#create a new bullet rect right above the space ship
    if len(bulletList) < bulletLimit:
        newBulletRect = py.Rect(0, 0, bulletWidth, bulletHeight)
        newBulletRect.midbottom = spaceShipRect.midtop
        #add new bullet to the list of existing bullets
        bulletList.append(newBulletRect)

def update_bullets():
    global bulletList
    global targetList
    global totalScore

    if len(bulletList) == 0:
        return

    #make a copy of bulletList to loop through so the real bulletList can be updated within loop
    tempRect = py.Rect(0,0,10,10)
    bulletListCopy = [tempRect]
    del bulletListCopy[0]
    i = 0
    for i in range(len(bulletList)):
        bulletCopy = bulletList[i].copy()
        bulletListCopy.append(bulletCopy)
        i += 1

	#make a copy of targetList to loop through so the real targetList may be updated within loop
    tempRect = py.Rect(0,0,10,10)
    targetListCopy = [tempRect]
    del targetListCopy[0]
    i = 0
    for i in range(len(targetList)):
        targetCopy = targetList[i].copy()
        targetListCopy.append(targetCopy)
        i += 1
    
    #advance the positions of all bullets in flight
    i = 0
    for bullet in bulletListCopy:
        #safty check
        if i >= len(bulletList):
            print("Error: bulletList length=", len(bulletList), "; i=", i)
            break

        #make sure the two lists are still lined up
        if bullet.y == bulletList[i].y:
            bulletList[i].y = bullet.y - bulletVel
        else:
            print("Error: bullet ", i, " y=", bulletList[i].y, "; copy y=", bullet.y)
        bulletRemoved = False
        #check for bullets going past top of screen
        if bulletList[i].bottom <= 0:
            #remove bullet from the real list
            del bulletList[i]
            bulletRemoved = True
        else:
            #test for target hits
            t = 0
            for target in targetListCopy:
                if t >= len(targetList):
                    #safety check
                    print("Error: targetList length=", len(targetList), "; t=", t)
                    break
                elif targetList[t].colliderect(bulletList[i]):
                    #remove the hit target and the bullet from the real lists then break out of loop,
                    #because each bullet can only hit one target
                    totalScore += ptsPerTarget
                    del targetList[t]
                    del bulletList[i]
                    bulletRemoved = True
                    break
                else:
                    t += 1 
        #do not increment the index if a bullet has been removed from the real list
        #because the next item in the list has moved up one slot
        if bulletRemoved == False:
            i += 1
        else:
            bulletRemove = False

def update_targets():
    global targetList
    global spaceShipRect
    global totalScore
    global targetDirection

    if len(targetList) == 0:
		#all targets have been shot down, player wins
        return PLAYER_WON

    move_down = 0
    leftMostTarget = targetList[0]
    rightMostTarget = targetList[len(targetList)-1]

	#test if targets are hitting screen boundaries
    if (leftMostTarget.left <= windowRect.left) or (rightMostTarget.right >= windowRect.right):
		#move all targets downward and then reverse horizontal direction
        move_down = 1
        targetDirection *= -1
    else:
        move_down = 0
    py.time.delay(5)
	
	#adjust positions of all targets
    t = 0
    for t in range(len(targetList)):
        targetList[t].x += (targetHVel * targetDirection)
        targetList[t].y += (targetVVel * move_down)
		#if the target collides with space ship, player loses
        if spaceShipRect.colliderect(targetList[t]):
            totalScore = 0
            return PLAYER_LOST
		#if the target has reached bottom of screen, player loses
        if targetList[t].bottom >= windowRect.bottom:
            totalScore = 0
            return PLAYER_LOST
        t += 1

    return GAME_CONTINUES	

def update_screen(spaceShipImage, targetImage, bg, caption):
    global screen
    global level1BackRect

    window.blit(bg, (0,0))
    level1BackRect = display_subtitle("Quit", 660)
    py.display.set_caption(caption)
    py.display.flip()

    #draw space ship at its new position
    window.blit(spaceShipImage, spaceShipRect)
	#draw targets in their new positions
    for target_rect in targetList:
        window.blit(targetImage, target_rect)
#        py.display.flip()

	#draw all the in-flight bullets at their new positions
    for bullet_rect in bulletList:
        py.draw.rect(window, bulletColor, bullet_rect)
#        py.display.flip()

	#refresh the screen
    py.display.flip()


def playGame(gameLevel):
    global screen
    global targetList
    global bulletList
    global targetHVel
    global targetVVel
    global totalScore
    global spaceShipRect
    global mouse_pos

    hOffset = 100 #how many pixels that bottom of space ship needs to be above bottom of screen
    if gameLevel == 1:
        spaceShipImage = py.image.load('GameImages\mainshipResized.png')
        targetImage = py.image.load('GameImages\enemy ship 1Resized.png')
        bg = py.image.load('GameImages\planetwithcraters.jpg')
        caption = ("Space Invaders Level 1")
        bulletLimit = 10
    else:
        spaceShipImage = py.image.load('GameImages\mainship2Resized.png')
        targetImage = py.image.load('GameImages\enemy ship 2Resized.png')
        bg = py.image.load('GameImages\\nubula.jpg')
        caption = ("Space Invaders Level 2")
        bulletLimit = 5

    #create space ship at starting position
    spaceShipRect = spaceShipImage.get_rect()
    spaceShipRect.midbottom = windowRect.midbottom
    spaceShipRect.bottom = windowRect.bottom - hOffset

	#adjust horizontal and vertical target movement speeds based on gameLevel
    targetHVel *= gameLevel
    targetVVel *= gameLevel

    #Create a list of targets
    targetRect = targetImage.get_rect()
    target_width = targetRect.width
    available_space_x = width - (2*target_width)
    number_targets_x = available_space_x // (2*target_width)
    for t in range(number_targets_x):
        newTargetRect = targetRect.copy()
        newTargetRect.x = target_width + 2*target_width*t
        newTargetRect.y = TARGET_Y_POS
        targetList.append(newTargetRect)

	#refresh the screen
    update_screen(spaceShipImage, targetImage, bg, caption)

	#delay for one second before starting the game
    py.time.delay(1000)

	#main game loop in which targets move continuously, ship moves and fires based on key presses
    continueGame = True
    totalScore = 0
    while continueGame:
		#check for keyboard input
        for event in py.event.get():
            if event.type == py.QUIT:
                py.display.quit()
            keyPressed = py.key.get_pressed()    
            if keyPressed[py.K_RIGHT] and (spaceShipRect.right+spaceShipVel)<=windowRect.right:
                spaceShipRect.x += spaceShipVel
            elif keyPressed[py.K_LEFT] and (spaceShipRect.left-spaceShipVel)>=windowRect.left:
                spaceShipRect.x -= spaceShipVel
            elif keyPressed[py.K_SPACE]: 
                fire_bullet(bulletLimit)
            elif event.type == py.MOUSEBUTTONDOWN:
                mouse_pressed = py.mouse.get_pressed()
                if mouse_pressed[0]: #Left mouse button clicked
                    mouse_pos = py.mouse.get_pos()
                    #quit game play and return to main program if mouse click is within Quit rect
                    reset_game()
                    continueGame = False
                    return PLAYER_QUIT

		#move up positions of all bullets in flight, check for target hits, update score
        update_bullets()

		#update positions of all remaining targets and check for win-lose scenarios
        outcome = update_targets()
        if outcome == PLAYER_LOST:
            spaceShipImage = py.image.load('GameImages\explosion imageResized.png')
		#draw all images on screen and refresh screen
        update_screen(spaceShipImage, targetImage, bg, caption)

        if outcome == PLAYER_WON or outcome == PLAYER_LOST:
            continueGame = False
            reset_game()
            return outcome


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
        currentDisplay = DISPLAY_LEVEL1
#        print("Main Menu: Clicked on Level 1")
        outCome = playGame(1)
        if outCome == PLAYER_WON:
            #write player name, game level, totalScore to score file
            #then display main menu window
            print("Player has won level 1 with score ", totalScore)
        elif outCome == PLAYER_LOST:
            #write player name, game level, 0 score to score file
            #then display main menu window
            print("Player has lost level 1. Total score: ", totalScore)

            
        elif outCome == PLAYER_QUIT:
            #display main menu window
            print("Player has quit level 1. Total score: ", totalScore)
    elif mainMenuRectList[2].collidepoint(mouse_pos[0], mouse_pos[1]):   
        currentDisplay = DISPLAY_LEVEL2
#        print("Main Menu: Clicked on Level 2")
        outCome = playGame(2)
        if outCome == PLAYER_WON:
            #write player name, game level, totalScore to score file
            #then display main menu window
            print("Player has won level 2 with score ", totalScore)
        elif outCome == PLAYER_LOST:
            #write player name, game level, 0 score to score file
            #then display main menu window
            print("Player has lost level 2. Total score: ", totalScore)
        elif outCome == PLAYER_QUIT:
            #display main menu window
            print("Player has quit level 2. Total score: ", totalScore)
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
    global mouse_pos
    if mouse_pos[0] >= 320 and mouse_pos[0] <= 380 and mouse_pos[1] >= 660 and mouse_pos[1] <= 680: 
        currentDisplay = display_Menu()
        print(mouse_pos)
        currentDisplay == DISPLAY_MAIN_MENU
        #800x800: 

def backButtonToSettings():
    global currentDisplay
    if mouse_pos[0] >= 320 and mouse_pos[0] <= 380 and mouse_pos[1] >= 660 and mouse_pos[1] <= 680:
        currentDisplay = display_Settings()

xc = random.randint(25, 100)
yc = random.randint(25, 100)
# rect = py.Rect(width/2, height/2, wbox, hbox)
hbox=50 
wbox=50



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

py.display.quit()
#Hw 11/2/21: Add game into level 1
            
