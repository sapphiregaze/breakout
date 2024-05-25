import pygame
import classes.game as game

pygame.init()
pygame.font.init()

if __name__ == "__main__":
    game = game.Game()
    game.run()

