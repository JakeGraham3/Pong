# This will show the paddles for each player
import pygame

GREEN = (0, 255, 102)

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)
        self.speed = 6

    def move(self, up=True):
        if up:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.rect)