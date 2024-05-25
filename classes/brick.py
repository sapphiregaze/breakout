import pygame

import config

class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(
            x, 
            y, 
            config.BRICK_WIDTH - config.BRICK_PADDING, 
            config.BRICK_HEIGHT - config.BRICK_PADDING
        )
        self.active = True

    def draw(self, screen):
        if self.active:
            pygame.draw.rect(screen, config.GREEN, self.rect)