import pygame

import config

class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(
            config.SCREEN_WIDTH // 2 - config.PADDLE_WIDTH // 2, 
            config.SCREEN_HEIGHT - 40, 
            config.PADDLE_WIDTH, 
            config.PADDLE_HEIGHT
        )

    def move(self, dx):
        self.rect.x += dx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > config.SCREEN_WIDTH:
            self.rect.right = config.SCREEN_WIDTH

    def draw(self, screen):
        pygame.draw.rect(screen, config.BLUE, self.rect)