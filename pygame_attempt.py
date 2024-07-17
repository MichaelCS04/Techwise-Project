import pygame
pygame.init()
#Create screen

window = pygame.display.set_mode((1200,800))

#Title and Icon
pygame.display.set_caption("Replica Pac-Man")
icon = pygame.image.load('game_logo.png')
pygame.display.set_icon(icon)

#Game loop

#Player Pac-man
playerImg = pygame.image.load('Pacman.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

#Enemy 
enemyImg = pygame.image.load('enemyGhost.png')
enemyX = 370
enemyY = 480
enemyX_change = 0
enemyY_change = 0


def player(x,y):
    #.blit == place an image onto the screens of pygame applications
    window.blit(playerImg, (x,y))
def enemy(x,y):
    #.blit == place an image onto the screens of pygame applications
    window.blit(enemyImg, (x,y))

running = True
while running:
    #Set background color
    window.fill((0,0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #keyboard control 
        #pygame.KEYDOWN = keyboard button being pressed 
        #pygame.KEYUP = keyboard buttons being released
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -0.3

                #print("Left arrow is pressed.")
            if event.key == pygame.K_RIGHT or event.key == pygame. K_d:
                playerX_change = 0.3


            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change = -0.3
                #print("Left arrow is pressed.")
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 0.3
                #print("Right arrow is pressed.")


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0
                #print("Keystoke has been released")
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                playerX_change = 0
                playerY_change = 0
    playerX += playerX_change 
    playerY += playerY_change 
    player(playerX, playerY)
    enemy(enemyX,enemyY) 
    """  
    #Flips pac-man image
    img_copy = playerImg.copy()
    img_with_flip = pygame.transform.flip(img_copy,True,False)
    #.blit == place an image onto the screens of pygame applications
    window.blit(img_with_flip, (playerX, playerY))
    """
    #player()
    pygame.display.update()