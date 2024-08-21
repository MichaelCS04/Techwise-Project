import pygame
import os
from board import boards
import copy
import math

pygame.init()

# Create screen
window = pygame.display.set_mode((980, 920))
WIDTH = 1000
HEIGHT = 950
level = copy.deepcopy(boards)
color = 'blue'
PI = math.pi

# Set framerate
clock = pygame.time.Clock()
FPS = 60

# Title and Icon
pygame.display.set_caption("Replica Pac-Man")
icon = pygame.image.load('game_logo.png')
pygame.display.set_icon(icon)

# Defining player action variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False

class Animation:
    def __init__(self, folder_path, frame_rate):
        self.images = self.load_images_from_folder(folder_path)
        self.frame_rate = frame_rate
        self.current_frame = 0
        self.time_since_last_frame = 0

    def load_images_from_folder(self, folder_path):
        images = []
        for filename in sorted(os.listdir(folder_path)):
            if filename.endswith('.png'):
                img = pygame.image.load(os.path.join(folder_path, filename))
                # Scale the image
                width, height = img.get_size()
                scaled_img = pygame.transform.scale(img, (int(width * 2), int(height * 2)))
                images.append(scaled_img)
        return images

    def update(self, dt):
        self.time_since_last_frame += dt
        if self.time_since_last_frame >= self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.images)
            self.time_since_last_frame = 0

    def draw(self, surface, position, direction):
        image = self.images[self.current_frame]
        if direction == 'left':
            image = pygame.transform.flip(image, True, False)
        elif direction == 'up':
            image = pygame.transform.rotate(image, 90)
        elif direction == 'down':
            image = pygame.transform.rotate(image, -90)
        surface.blit(image, position)

# Player Pac-man
class Pacman(pygame.sprite.Sprite):
    def __init__(self, playerX, playerY, speed, animation):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.animation = animation
        self.rect = self.animation.images[0].get_rect()
        self.rect.center = (playerX, playerY)
        self.direction = 'right'  # Default direction
        self.moving = False

    def move(self, moving_left, moving_right, moving_up, moving_down):
        # Reset movement variables
        dx = 0
        dy = 0

        if moving_left:
            dx = -self.speed
            self.direction = 'left'
            self.moving = True
        
        if moving_right:
            dx = self.speed
            self.direction = 'right'
            self.moving = True

        if moving_up:
            dy = -self.speed
            self.direction = 'up'
            self.moving = True
        
        if moving_down:
            dy = self.speed
            self.direction = 'down'
            self.moving = True

        # Updating rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def update(self, dt):
        if self.moving:
            self.animation.update(dt)
        self.moving = False

    def draw(self):
        self.animation.draw(window, self.rect.topleft, self.direction)

def draw_board():
    num1 = (HEIGHT - 50) // 32
    num2 = WIDTH // 30
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(window, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            elif level[i][j] == 2:
                pygame.draw.circle(window, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
            elif level[i][j] == 3:
                pygame.draw.line(window, color, (j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)
            elif level[i][j] == 4:
                pygame.draw.line(window, color, (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            elif level[i][j] == 5:
                pygame.draw.arc(window, color, pygame.Rect(j * num2 - (num2 * 0.4) - 2, i * num1 + (0.5 * num1), num2, num1),
                                0, PI / 2, 3)
            elif level[i][j] == 6:
                pygame.draw.arc(window, color,
                                pygame.Rect(j * num2 + (num2 * 0.5), i * num1 + (0.5 * num1), num2, num1), PI / 2, PI, 3)
            elif level[i][j] == 7:
                pygame.draw.arc(window, color, pygame.Rect(j * num2 + (num2 * 0.5), i * num1 - (0.4 * num1), num2, num1), PI,
                                3 * PI / 2, 3)
            elif level[i][j] == 8:
                pygame.draw.arc(window, color,
                                pygame.Rect(j * num2 - (num2 * 0.4) - 2, i * num1 - (0.4 * num1), num2, num1), 3 * PI / 2,
                                2 * PI, 3)
            elif level[i][j] == 9:
                pygame.draw.line(window, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)

# Initialize Animation with folder path containing images
folder_path = r'C:\\Users\\Castr\\OneDrive\\Desktop\\pac_animation'  # Replace with your actual folder path
animation = Animation(folder_path, 100)

# Initialize Player
player = Pacman(470, 515, 5, animation)

# Game loop
running = True
while running:
    dt = clock.tick(FPS)
    # Set background color
    window.fill((0, 0, 0))
    draw_board()

    player.move(moving_left, moving_right, moving_up, moving_down)
    player.update(dt)
    player.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                moving_down = True
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                moving_down = False

    pygame.display.update()

pygame.quit()
