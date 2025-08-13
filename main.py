import asyncio
import pygame
import random

# Game constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 6
BALL_SIZE = 20
BALL_SPEED_X, BALL_SPEED_Y = 5, 5
WIN_SCORE = 20
AI_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

async def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong with AI")

    font = pygame.font.Font(None, 74)

    player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2,
                                PADDLE_WIDTH, PADDLE_HEIGHT)
    ai_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2,
                             PADDLE_WIDTH, PADDLE_HEIGHT)

    ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2,
                       BALL_SIZE, BALL_SIZE)
    ball_dx = random.choice([-BALL_SPEED_X, BALL_SPEED_X])
    ball_dy = random.choice([-BALL_SPEED_Y, BALL_SPEED_Y])

    player_score = 0
    ai_score = 0
    game_over = False
    winner_text = ""

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                running = False

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and player_paddle.top > 0:
                player_paddle.y -= PADDLE_SPEED
            if keys[pygame.K_s] and player_paddle.bottom < HEIGHT:
                player_paddle.y += PADDLE_SPEED

            if ai_paddle.centery < ball.centery and ai_paddle.bottom < HEIGHT:
                ai_paddle.y += AI_SPEED
            elif ai_paddle.centery > ball.centery and ai_paddle.top > 0:
                ai_paddle.y -= AI_SPEED

            ball.x += ball_dx
            ball.y += ball_dy

            if ball.top <= 0 or ball.bottom >= HEIGHT:
                ball_dy *= -1

            if ball.colliderect(player_paddle):
                ball.left = player_paddle.right
                ball_dx *= -1
            elif ball.colliderect(ai_paddle):
                ball.right = ai_paddle.left
                ball_dx *= -1

            if ball.left <= 0:
                ai_score += 1
                ball.center = (WIDTH // 2, HEIGHT // 2)
                ball_dx = random.choice([-BALL_SPEED_X, BALL_SPEED_X])
                ball_dy = random.choice([-BALL_SPEED_Y, BALL_SPEED_Y])
            elif ball.right >= WIDTH:
                player_score += 1
                ball.center = (WIDTH // 2, HEIGHT // 2)
                ball_dx = random.choice([-BALL_SPEED_X, BALL_SPEED_X])
                ball_dy = random.choice([-BALL_SPEED_Y, BALL_SPEED_Y])

            if player_score >= WIN_SCORE:
                winner_text = "You Win!"
                game_over = True
            elif ai_score >= WIN_SCORE:
                winner_text = "You Lose!"
                game_over = True

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, player_paddle)
        pygame.draw.rect(screen, WHITE, ai_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        player_text = font.render(str(player_score), True, WHITE)
        ai_text = font.render(str(ai_score), True, WHITE)
        screen.blit(player_text, (WIDTH // 4, 20))
        screen.blit(ai_text, (WIDTH * 3 // 4, 20))

        if game_over:
            win_surface = font.render(winner_text, True, WHITE)
            screen.blit(win_surface, (WIDTH // 2 - win_surface.get_width() // 2,
                                      HEIGHT // 2 - win_surface.get_height() // 2))

        pygame.display.flip()
        clock.tick(60)

        # Yield control to browser so it doesn't freeze
        await asyncio.sleep(0)

asyncio.run(main())
