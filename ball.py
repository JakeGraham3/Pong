# This shows the ball and gives it its speed
import pygame

GREEN = (0, 255, 102)

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 15, 15)
        self.speed_x = 4.5
        self.speed_y = 4.5

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.rect)