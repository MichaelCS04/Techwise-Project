import pygame
#from sprite_viewer import SpriteViewer
pygame.init()
#Create screen
#SpriteViewer()
window = pygame.display.set_mode((1200,800))
#set framerate
clock = pygame.time.Clock()
FPS = 60
#Title and Icon
pygame.display.set_caption("Replica Pac-Man")
icon = pygame.image.load('game_logo.png')
pygame.display.set_icon(icon)

#defining player action variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False

#Player Pac-man
class Pacman(pygame.sprite.Sprite):
    def __init__(self, playerX, playerY, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        playerImg = pygame.image.load('Pacman.png')
        self.image = playerImg
        self.rect = playerImg.get_rect()
        self.rect.center = (playerX,playerY)

    def move(self, moving_left, moving_right, moving_up, moving_down):
        #reset movement variables
        #dx= deltax dx = deltay
        dx = 0
        dy = 0

        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        if moving_up: 
            dy = -self.speed
        if moving_down: 
            dy = self.speed

        #updating rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        window.blit(pygame.transform.flip(self.image,self.flip, False), self.rect) 
player = Pacman(500,480, 5)


#Game loop
running = True
while running:
    
    clock.tick(FPS)
    #Set background color
    window.fill((0,0,0))

    player.draw()
    player.move(moving_left, moving_right, moving_up,moving_down)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #keyboard control 
        #pygame.KEYDOWN = keyboard button being pressed 
        #pygame.KEYUP = keyboard buttons being released
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                moving_left = True

                #print("Left arrow is pressed.")
            if event.key == pygame.K_RIGHT or event.key == pygame. K_d:
                moving_right = True
            if event.key == pygame.K_UP or event.key == pygame. K_w:
                moving_up = True
            if event.key == pygame.K_DOWN or event.key == pygame. K_s:
                moving_down = True

            if event.key == pygame.K_ESCAPE:
                running = True



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_UP or event.key == pygame. K_w:
                moving_up = False
            if event.key == pygame.K_DOWN or event.key == pygame. K_s:
                moving_down = False
            
#player()
    pygame.display.update()

"""
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
"""
"""
    playerX += playerX_change 
    playerY += playerY_change 
    player(playerX, playerY)
    enemy(enemyX,enemyY) 
"""
"""  
    #Flips pac-man image
    img_copy = playerImg.copy()
    img_with_flip = pygame.transform.flip(img_copy,True,False)
    #.blit == place an image onto the screens of pygame applications
    window.blit(img_with_flip, (playerX, playerY))
"""


"""
#Enemy 
enemyImg = pygame.image.load('enemyGhost.png')
enemyX = 370
enemyY = 480
enemyX_change = 0
enemyY_change = 0


def player(x,y):
    #.blit == place an image onto the screens of pygame applications
    window.blit(playerImg, (playerX,playerY))
def enemy(x,y):
    #.blit == place an image onto the screens of pygame applications
    window.blit(enemyImg, (x,y))
"""