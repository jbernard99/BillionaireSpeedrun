import pygame

class Bar:
    def __init__(self, x, y, w, h, bg_color):
        self.rect = pygame.Rect(x, y, w, h)
        self.bg_color = bg_color
        
    def draw(self, surface):
        # Draw the button
        pygame.draw.rect(surface, self.bg_color, self.rect)
        