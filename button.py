import pygame.ftfont

class Button():

    def __init__(self, screen):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.button = pygame.image.load('images/button.bmp')
        self.button_rect = self.button.get_rect()

        self.button_rect.x = self.button_rect.width
        self.button_rect.y = self.button_rect.height

        # Build the button's rect object and center it.
        self.button_rect = pygame.Rect(0, 0, self.button_rect.width, self.button_rect.height)
        self.button_rect.center = self.screen_rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.blit(self.button, self.button_rect)
