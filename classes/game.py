import pygame
import sys

import classes.paddle as paddle
import classes.brick as brick
import classes.ball as ball

import config

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("Block Breaker")
        self.clock = pygame.time.Clock()
        self.paddle = paddle.Paddle()
        self.ball = ball.Ball()
        self.bricks = [brick.Brick(col * config.BRICK_WIDTH, row * config.BRICK_HEIGHT) for row in range(config.BRICK_ROWS) for col in range(config.BRICK_COLUMNS)]
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.move(-config.PADDLE_SPEED)
        if keys[pygame.K_RIGHT]:
            self.paddle.move(config.PADDLE_SPEED)

        self.ball.move()

        if self.ball.rect.colliderect(self.paddle.rect):
            self.ball.dy = -self.ball.dy

        for brick in self.bricks:
            if brick.active and self.ball.rect.colliderect(brick.rect):
                self.ball.dy = -self.ball.dy
                brick.active = False
                break

        if self.ball.rect.bottom > config.SCREEN_HEIGHT:
            print("Game Over")
            self.running = False

    def draw(self):
        self.screen.fill(config.BLACK)
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        for brick in self.bricks:
            brick.draw(self.screen)
        pygame.display.flip()