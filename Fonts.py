#Andrew Cai 10/25/21
#Learning fonts and blit

import pygame as py, os, random, time

py.init()
BLACK = (0,0,0)
COLOR=(255,255,255)
width = 600
height = 600
window = py.display.set_mode((width,height))
py.display.set_caption("Settings Window")

# TITLE_FONT = py.font.SysFont(name, size, bold=False, italic=False )
TITLE_FONT = py.font.SysFont('Heveltica', 80)
subtitle = py.font.SysFont('comicsans', 40, italic=True)

def display_TITLE(message):
    py.time.delay(100)
    text = TITLE_FONT.render(message, 1, COLOR )
   # window.blit(text, (width/2-text.get_width()/2, height/2-text.get_height()/2))
    window.blit(text, (width/2-text.get_width()/2, 10))
    py.display.update()
    #py.time.delay(100)

def display_message1(message):
    #py.time.delay(100)
    text = TITLE_FONT.render(message, 1, COLOR )
   # window.blit(text, (width/2-text.get_width()/2, height/2-text.get_height()/2))
    window.blit(text, (width/2-text.get_width()/2, 70))
    py.display.update()
    #py.time.delay(100)

def display_message2(message):
    #py.time.delay(100)
    text = TITLE_FONT.render(message, 1, COLOR )
   # window.blit(text, (width/2-text.get_width()/2, height/2-text.get_height()/2))
    window.blit(text, (width/2-text.get_width()/2, 130))
    py.display.update()
    #py.time.delay(100)

def display_message3(message):
    #py.time.delay(100)
    text = TITLE_FONT.render(message, 4, COLOR )
   # window.blit(text, (width/2-text.get_width()/2, height/2-text.get_height()/2))
    window.blit(text, (width/2-text.get_width()/2, 200))
    py.display.update()
    #py.time.delay(100)
run = True

while run:
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run = False
            py.quit()
    window.fill((0,0,0))
    display_TITLE("--SETTINGS--")
    display_message1("⨞ Background Color")
    display_message2("⨞ Object Colors")
    display_message3("⨞ Sound") 
    #py.time.delay(10000)
    py.display.update()



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
