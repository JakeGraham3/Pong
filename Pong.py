import pygame
import sys
from players import Paddle
from ball import Ball

pygame.init()

# I used some reference from my group project.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

GREEN = (0, 255, 102)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
FPS = 120
# this is where everything runs
def main():
    running = True
    left_paddle = Paddle(30, SCREEN_HEIGHT // 2 - 50)
    right_paddle = Paddle(SCREEN_WIDTH - 40, SCREEN_HEIGHT // 2 - 50)
    ball = Ball(SCREEN_WIDTH // 2 - 7, SCREEN_HEIGHT // 2 - 7)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        
        # Player 1 controls the left paddle
        if keys[pygame.K_w] and left_paddle.rect.top > 0:
            left_paddle.move(up=True)
        if keys[pygame.K_s] and left_paddle.rect.bottom < SCREEN_HEIGHT:
            left_paddle.move(up=False)
        
        # Player 2 controls the right paddle
        if keys[pygame.K_UP] and right_paddle.rect.top > 0:
            right_paddle.move(up=True)
        if keys[pygame.K_DOWN] and right_paddle.rect.bottom < SCREEN_HEIGHT:
            right_paddle.move(up=False)

        ball.move()

        # Ball collision with top and bottom
        if ball.rect.top <= 0 or ball.rect.bottom >= SCREEN_HEIGHT:
            ball.speed_y *= -1

        # Ball collision with paddles
        if ball.rect.colliderect(left_paddle.rect) or ball.rect.colliderect(right_paddle.rect):
            ball.speed_x *= -1

        # Ball out of bounds
        if ball.rect.left <= 0 or ball.rect.right >= SCREEN_WIDTH:
            ball.rect.x = SCREEN_WIDTH // 2 - ball.rect.width // 2
            ball.rect.y = SCREEN_HEIGHT // 2 - ball.rect.height // 2
            ball.speed_x *= -1

        SCREEN.fill(BLACK)
        left_paddle.draw(SCREEN)
        right_paddle.draw(SCREEN)
        ball.draw(SCREEN)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()