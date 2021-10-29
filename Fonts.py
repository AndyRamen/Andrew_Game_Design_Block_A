#Andrew Cai 10/25/21
#Learning fonts and blit

from typing import Text
import pygame as py, os, random, time

py.init()
menuMessages = ["Instructions", "Level 1", "Settings", "Exit"]
messages = ["Background Color", "Object Color", "Sound on/off", "Screen Size"]
backMessage = ["wfoi", "Back"]
BLACK = (0,0,0)
WHITE=(255,255,255)
DISPLAY_MAIN_MENU = 0
DISPLAY_INSTRUCTIONS = 1
DISPLAY_LEVEL1 = 2
DISPLAY_SETTINGS = 3
DISPLAY_SETTINGS_BKGCOLOR = 4
DISPLAY_SETTINGS_OBJCOLOR = 5
DISPLAY_SETTINGS_SOUND = 6
DISPLAY_SETTINGS_SCNSIZE = 7
currentDisplay = DISPLAY_MAIN_MENU
width = 600
height = 600
window = py.display.set_mode((width,height))
py.display.set_caption("Settings Window")

# TITLE_FONT = py.font.SysFont(name, size, bold=False, italic=False )
TITLE_FONT = py.font.SysFont('Heveltica', 80)
SUBTITLE_FONT = py.font.SysFont('Heveltica', 40)
wbox = 25
hbox = 25
square = py.Rect(10,10, wbox, hbox)

def display_TITLE(message, y):
    py.time.delay(100)
    text = TITLE_FONT.render(message, 1, WHITE )
    x = width/2-text.get_width()/2
   # window.blit(text, (width/2-text.get_width()/2, height/2-text.get_height()/2))
    window.blit(text, (x, y))
    py.display.update()
    #py.time.delay(100)

def display_subtitle (message, y):
    py.time.delay(100)
    text = SUBTITLE_FONT.render(message, 1, WHITE)
    x = width/2 - text.get_width()/2
    window.blit(text, (x,y))
    py.display.update()

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
    for i in range(0, len(messages)):
        word = menuMessages[i]
        py.draw.rect(window, WHITE, square)
        text = TITLE_FONT.render(word, 1, WHITE)
        window.blit(text, (x+wbox+10, y))
        py.display.flip()
        py.time.delay(100)
        y += 80
        square.y = y

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

def Settings_Menu():
    x = 40
    y = 90
    square.x = x
    square.y = y
    for i in range(0,len(messages)):
        word = messages[i]
        py.draw.rect(window, WHITE, square)
        text = TITLE_FONT.render(word, 1, WHITE)
        window.blit(text, (x+wbox+10, y))
        py.display.flip()
        py.time.delay(100)
        y += 80
        square.y = y
#counter=0
run = True
window.fill((0,0,0))
display_TITLE("--Main Menu--", 20)
# display_TITLE("--Settings--", 20)
display_Menu()
py.display.update()
currentDisplay = DISPLAY_MAIN_MENU

while run:
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run = False
            py.quit()
    
    if eve.type == py.MOUSEBUTTONDOWN:
        mouse_pressed = py.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos = py.mouse.get_pos()
            print(py.mouse.get_pos())

            if currentDisplay == DISPLAY_MAIN_MENU:   
                if mouse_pos[0] >= 40 and mouse_pos[0] <= 65 and mouse_pos[1] >= 90 and mouse_pos[1] <= 114:
                    window.fill(BLACK)
                    display_TITLE("Instructions:", 30)
                    display_subtitle("Back", 560)
                    currentDisplay = DISPLAY_INSTRUCTIONS
                    #x = 270, 330 y = 560 580
                elif mouse_pos[0] >= 40 and mouse_pos[0] <= 65 and mouse_pos[1] >= 170 and mouse_pos[1] <=195:
                    window.fill(BLACK)
                    display_TITLE("Level 1", 30)
                    display_subtitle("Back", 560)
                    currentDisplay = DISPLAY_LEVEL1
                #x: 40 65 y: 250 275
                elif mouse_pos[0] >= 40 and mouse_pos[0] <= 65 and mouse_pos[1] >= 250 and mouse_pos[1] <=275:
                    window.fill(BLACK)
                    display_TITLE("--Settings--", 20)
                    Settings_Menu()
                    py.display.update()
                    display_subtitle("Back", 560)
                    currentDisplay = DISPLAY_SETTINGS
                elif mouse_pos[0] >= 40 and mouse_pos[0] <= 65 and mouse_pos[1] >= 330 and mouse_pos[1] <= 355:
                    #Clicked on Exit
                    run = False
            elif currentDisplay == DISPLAY_INSTRUCTIONS:
                if mouse_pos[0] >= 270 and mouse_pos[0] <= 330 and mouse_pos[1] >= 560 and mouse_pos[1] <= 580:
                    window.fill(BLACK)
                    display_TITLE("--Main Menu--", 20)
                    display_Menu()
                    py.display.update()
                    currentDisplay = DISPLAY_MAIN_MENU
            elif currentDisplay == DISPLAY_LEVEL1:
                if mouse_pos[0] >= 270 and mouse_pos[0] <= 330 and mouse_pos[1] >= 560 and mouse_pos[1] <= 580:
                    window.fill(BLACK)
                    display_TITLE("--Main Menu--", 20)
                    display_Menu()
                    py.display.update()
                    currentDisplay = DISPLAY_MAIN_MENU
            elif currentDisplay == DISPLAY_SETTINGS:
                if mouse_pos[0] >= 270 and mouse_pos[0] <= 330 and mouse_pos[1] >= 560 and mouse_pos[1] <= 580:
                    window.fill(BLACK)
                    display_TITLE("--Main Menu--", 20)
                    display_Menu()
                    py.display.update()
                    currentDisplay = DISPLAY_MAIN_MENU




py.display.quit
            
#             if mouse_pos[0] >= 40 and mouse_pos[0] <= 65 and mouse_pos[1] >= 90 and mouse_pos[1] <= 114:
#                 window.fill(BLACK)
#                 display_TITLE("Background Color", 70)
#             if mouse_pos[0] >= 40 and mouse_pos[0] <= 65 and mouse_pos[1] >=170 and mouse_pos[1] <=195:
#                 window.fill(BLACK)
#                 display_TITLE("Object Colors", 70) 
        #Will say (true, false, false) Left is left click, middle is middle click, right is right click
        #Hw 10/27/21: Make main menu
        #Menu
        #Instructions
        #Level 1
        #Settings
        #Exit






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
#--Settings--
#Window size
#Background color
#Object colors
#Sound on/off

#HW: print the rest of the menu (ex above)
    # display_TITLE("This is awesome")
    # py.time.delay(300)
    # window.fill((0,0,0))
    # display_TITLE("Whoops")
    # py.time.delay(300)
    # window.fill((0,0,0))
    # display_TITLE("Closing")
    # window.fill((0,0,0))
    # py.time.delay(200)

py.quit()
