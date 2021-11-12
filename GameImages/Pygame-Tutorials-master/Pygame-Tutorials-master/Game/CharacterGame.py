import pygame
pygame.init()

win = pygame.display.set_mode((600,600))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R1.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R2.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R3.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R4.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R5.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R6.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R7.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R8.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R9.png')]
walkLeft = [pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L1.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L2.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L3.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L4.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L5.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L6.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L7.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L8.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L9.png')]
bg = pygame.image.load('GameImages\space image.jpg')
char = pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\standing.png')

x = 0
y = 470
width = 40
height = 60
vel = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    
    win.blit(bg, (0,0))  
    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left:  
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1                          
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0
        
    pygame.display.update() 
    


run = True

while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif eve.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = pygame.mouse.get_pressed()
            if mouse_pressed[0]: #Left mouse button clicked
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
    clock.tick(27)
#(1, 520) (95, 520)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#(100, 510) left and (123, 495) right
    keys = pygame.key.get_pressed()
    #if x of character is less than grapp's x, he cant move right, he will have to jump. Will have to check if x and y is between two other rocks
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 110 - vel - width and y>= 520 - height: #and x < 97 and y>= 520: #and x>= 1 and x<=95: #not(x >= 100 and x <= 123 and y >= 495 and y <= 510)  and x < 100 - vel - width:  
        x += vel
        left = False
        right = True
        
    else: 
        left = False
        right = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    redrawGameWindow() 
    
    
pygame.quit()