import pygame
import sys

import classes.paddle as paddle
import classes.brick as brick
import classes.ball as ball

import config

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("Breakout")
        self.clock = pygame.time.Clock()
        self.reset_game()
        
        self.ball_bounce_sound = pygame.mixer.Sound("assets/ball-bounce.wav")
        self.brick_break_sound = pygame.mixer.Sound("assets/brick-break.wav")

    def reset_game(self):
        self.paddle = paddle.Paddle()
        self.ball = ball.Ball()
        self.bricks = [brick.Brick(
            col * config.BRICK_WIDTH, 
            row * config.BRICK_HEIGHT
        ) for row in range(config.BRICK_ROWS) for col in range(config.BRICK_COLUMNS)]
        
        self.running = True
        self.won = False
        self.lost = False
        
        self.score = 0

    def run(self):
        self.show_screen()
        while True:
            self.handle_events()
            if self.running:
                self.update()
                self.draw()
            elif self.won:
                self.show_screen()
            elif self.lost:
                self.show_screen()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    def show_screen(self):
        if not (self.won or self.lost):
            title = "Breakout"
            subtitle = "Press any key to start"
        elif self.won:
            title = f"You won! Perfect score!"
            subtitle = "Press any key to play again"
        else:
            title = f"You lost with a score of {self.score} :("
            subtitle = "Press any key to play again"

        current_screen = True
        while current_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    current_screen = False

            self.screen.fill(config.BLACK)
            self.draw_text(
                title, 
                64, 
                config.WHITE, 
                config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 - 100
            )
            self.draw_text(
                subtitle, 
                32, 
                config.WHITE, 
                config.SCREEN_WIDTH // 2, 
                config.SCREEN_HEIGHT // 2 + 50
            )
            pygame.display.flip()
            self.clock.tick(15)
            
        if not current_screen and not self.running:
            self.reset_game()
            self.show_screen()

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and (self.won or self.lost):
                self.reset_game()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.move(-config.PADDLE_SPEED)
        if keys[pygame.K_RIGHT]:
            self.paddle.move(config.PADDLE_SPEED)

        self.ball.move()

        if self.ball.rect.colliderect(self.paddle.rect):
            self.ball.dy = -self.ball.dy
            self.ball_bounce_sound.play()

        for brick in self.bricks:
            if brick.active and self.ball.rect.colliderect(brick.rect):
                self.ball.dy = -self.ball.dy
                brick.active = False
                self.brick_break_sound.play()
                self.score += 1
                break

        if self.ball.rect.bottom > config.SCREEN_HEIGHT:
            self.lost = True
            self.running = False

        if all(not brick.active for brick in self.bricks):
            self.won = True
            self.running = False

    def draw(self):
        self.screen.fill(config.BLACK)
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        for brick in self.bricks:
            brick.draw(self.screen)
            
        font = pygame.font.Font(None, 35)
        text = font.render(f"Score: {self.score}", True, config.WHITE)
        text_rect = text.get_rect()
        text_rect.topleft = (10, config.SCREEN_HEIGHT - text_rect.height - 10)
        self.screen.blit(text, text_rect)

        pygame.display.flip()