import pygame
import random

import config

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(
            config.SCREEN_WIDTH // 2, 
            config.SCREEN_HEIGHT // 2, 
            config.BALL_RADIUS * 2, 
            config.BALL_RADIUS * 2
        )
        self.dx = config.BALL_SPEED * random.choice([-1, 1])
        self.dy = config.BALL_SPEED * random.choice([-1, 1])

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left < 0 or self.rect.right > config.SCREEN_WIDTH:
            self.dx = -self.dx
        if self.rect.top < 0:
            self.dy = -self.dy

    def draw(self, screen):
        pygame.draw.ellipse(screen, config.RED, self.rect)
