import pygame
pygame.init()

win = pygame.display.set_mode((600,600))
winRect = win.get_rect()
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R1.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R2.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R3.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R4.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R5.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R6.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R7.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R8.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R9.png')]
walkLeft = [pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L1.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L2.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L3.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L4.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L5.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L6.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L7.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L8.png'), pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L9.png')]
bg = pygame.image.load('GameImages\space image.jpg')
char = pygame.image.load('GameImages\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\standing.png')

#Define 4 rectangles boxing in the 4 obstacles that the character must jump onto in sequence
Obstacle1_rect = pygame.Rect(97, 496, 124-97, winRect.height-496)
Obstacle2_rect = pygame.Rect(125, 458, 174-125, winRect.height-458)
Obstacle3_rect = pygame.Rect(232, 372, 308-232, winRect.height-372)
Obstacle4_rect = pygame.Rect(175, 250, 231-175, winRect.height-250)
obstacleCleared = 0

x = 0
y_ground = 470
y = y_ground
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
        redrawn_rect = win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1                          
    elif right:
        redrawn_rect = win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        redrawn_rect = win.blit(char, (x, y))
        walkCount = 0
        
    pygame.display.update()
    return redrawn_rect 
    


run = True
char_rect = char.get_bounding_rect() #Define a rect variable to hold the character's rect after each position change

while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif eve.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = pygame.mouse.get_pressed()
            if mouse_pressed[0]: #Left mouse button clicked
                mouse_pos = pygame.mouse.get_pos()
                # print(mouse_pos)
    clock.tick(27)
#Obstacle 1: (97, 520) is start/top left, (158, 457) is highest point, (175, 464) is end/top right
#Obstacle 2: (200, 415) is start, (290, 372) is highest point, (310, 409) is end 
#Obstacle 3: (197, 306) is start, (213, 250) is highest point, (230, 367) is end
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#(100, 510) left and (123, 495) right
    keys = pygame.key.get_pressed()
    #if x of character is less than grapp's x, he cant move right, he will have to jump. Will have to check if x and y is between two other rocks
    if keys[pygame.K_LEFT] and x > vel: 
        if obstacleCleared == 1 and (x+width)<=Obstacle1_rect.midtop[0]:
            #Char on obstacle 1. He will fall to ground level if he moves too far left
            x -= vel
            y = y_ground
            obstacleCleared = 0
        elif obstacleCleared == 2 and (x+width)<=Obstacle2_rect.midtop[0]:
            #Char on obstacle 2. He will fall to ground level if he moves too far left
            x -= vel
            y = y_ground
            obstacleCleared = 0
        elif not(isJump) and obstacleCleared == 3 and (x-vel)<=Obstacle3_rect.left:
            #Char on obstacle 3, which is blocked on the left by obstacle 4; char cannot walk past left boundary but can jump left to obstacle 4
            x = Obstacle3_rect.left
        elif obstacleCleared == 4 and (x+width)<=Obstacle4_rect.midtop[0]:
            #Char on obstacle 4. He will fall to ground level if he moves too far left
            x -= vel
            y = y_ground
            obstacleCleared = 0
        else:
            #Char on groud level, so free to move left
            x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and (x+width+vel)<winRect.right: #and x < 110 - vel - width and y>= 520 - height: #and x < 97 and y>= 520: #and x>= 1 and x<=95: #not(x >= 100 and x <= 123 and y >= 495 and y <= 510)  and x < 100 - vel - width:  
        if not(isJump) and obstacleCleared == 1 and (x+width)>=Obstacle2_rect.left:
            #Char on obstacle 1, which is blocked on the right by obstacle 2. He cannot walk right past the boundary but can jump right
            x = Obstacle2_rect.left - width
        elif not(isJump) and obstacleCleared == 2 and x >= Obstacle2_rect.midtop[0]:
            #Char on obstacle 2. He will fall to ground level if he walks too far right but he can jump right towards obstacle 3
            x += vel
            y = y_ground
            obstacleCleared = 0
        elif obstacleCleared == 3 and (x+width/2) >= (Obstacle3_rect.right):
            #Char on obstacle 3, he will fall to ground level if he moves past right edge of obstacle 3
            x += vel
            y = y_ground
            obstacleCleared = 0
        elif obstacleCleared == 4 and x >= Obstacle4_rect.midtop[0]:
            #Char on obstacle 4. He will fall to ground level if he moves too far right
            x += vel
            y = y_ground
            obstacleCleared = 0
        else:
            #Char on groud level, so free to move left
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
            if jumpCount < 0: #character is coming down
                #Test if char's rect will collide with obstacle 1 rect
                char_rect.y = y - (jumpCount * abs(jumpCount)) * 0.5
                #print("char_rect: ", char_rect.bottomleft[0], ",", char_rect.bottomleft[1], " | ", char_rect.bottomright[0], ",", char_rect.bottomright[1])
                #print("obstacle1_rect: ", Obstacle1_rect.bottomleft[0], ",", Obstacle1_rect.bottomleft[1], " | ", Obstacle1_rect.bottomright[0], ",", Obstacle1_rect.bottomright[1])
                if obstacleCleared==0 and Obstacle1_rect.colliderect(char_rect):
                     y = Obstacle1_rect.top - char_rect.height #Stop char on top of the obstacle's rect
                     x = Obstacle1_rect.midtop[0] - char_rect.width/2 #Center char on top of the obstacle's rect
                     obstacleCleared = 1 #Set the flag that char is on top of obstacle 1
                     jumpCount = 10
                     isJump = False
                     print("Collided with Obstacle 1!")
                elif obstacleCleared==1 and Obstacle2_rect.colliderect(char_rect):
                     y = Obstacle2_rect.top - char_rect.height #Stop char on top of the obstacle's rect
                     x = Obstacle2_rect.midtop[0] - char_rect.width/2 #Center char on top of the obstacle's rect
                     obstacleCleared = 2 #Set the flag that char is on top of obstacle 2
                     jumpCount = 10
                     isJump = False
                     print("Collided with Obstacle 2!")
                elif obstacleCleared==2 and Obstacle3_rect.colliderect(char_rect):
                     y = Obstacle3_rect.top - char_rect.height #Stop char on top of the obstacle's rect
                     x = Obstacle3_rect.midtop[0] - char_rect.width/2 #Center char on top of the obstacle's rect
                     obstacleCleared = 3 #Set the flag that char is on top of obstacle 3
                     jumpCount = 10
                     isJump = False
                     print("Collided with Obstacle 3!")
                elif obstacleCleared==3 and Obstacle4_rect.colliderect(char_rect):
                     y = Obstacle4_rect.top - char_rect.height #Stop char on top of the obstacle's rect
                     x = Obstacle4_rect.midtop[0] - char_rect.width/2 #Center char on top of the obstacle's rect
                     obstacleCleared = 4 #Set the flag that char is on top of obstacle 4
                     jumpCount = 10
                     isJump = False
                     print("Collided with Obstacle 4!")
                else:
                    if (y - (jumpCount * abs(jumpCount)) * 0.5) > y_ground: #Char is about to fall past ground level, make him stop
                        y = y_ground
                        jumpCount = 10
                        isJump = False
                    else:
                        y -= (jumpCount * abs(jumpCount)) * 0.5
                        jumpCount -= 1
            else:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    char_rect = redrawGameWindow() 
    
    
pygame.quit()