import pygame
import spritesheet

class SpriteViewer:
    def __init__(self, screen_width=674, screen_height=745, sprite_sheet_path='map.png', bg_color=(50, 50, 50), black=(0, 0, 0)):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Spritesheets')

        sprite_sheet_image = pygame.image.load(sprite_sheet_path).convert_alpha()
        self.sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

        self.bg_color = bg_color
        self.black = black

        self.frame_0 = self.sprite_sheet.get_image(0, 225, 300, 3, self.black)
        """
        self.frame_1 = self.sprite_sheet.get_image(1, 24, 24, 3, self.black)
        self.frame_2 = self.sprite_sheet.get_image(2, 24, 24, 3, self.black)
        self.frame_3 = self.sprite_sheet.get_image(3, 24, 24, 3, self.black)
        """

    def run(self):
        running = True
        while running:
            # Update background
            self.screen.fill(self.bg_color)

            # Show frame image
            self.screen.blit(self.frame_0, (0, 0))
            """
            self.screen.blit(self.frame_1, (72, 0))
            self.screen.blit(self.frame_2, (150, 0))
            self.screen.blit(self.frame_3, (250, 0))
            """

            # Event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()
        
        pygame.quit()

# Example usage:
viewer = SpriteViewer()
viewer.run()