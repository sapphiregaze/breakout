import pygame
import classes.game as game

pygame.init()
pygame.font.init()

pygame.mixer.init()
pygame.mixer.music.load("assets/byte-blast.mp3")
pygame.mixer.music.play(-1)

if __name__ == "__main__":
    game = game.Game()
    game.run()

