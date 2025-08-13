import asyncio
import pygame

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

async def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
    pygame.display.set_caption("Pong in Browser")
    clock = pygame.time.Clock()

    ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
    ball_speed = [4, 4]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        if ball.left <= 0 or ball.right >= WIDTH:
            ball_speed[0] = -ball_speed[0]
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed[1] = -ball_speed[1]

        screen.fill((0, 0, 0))
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.display.flip()
        clock.tick(60)

        await asyncio.sleep(0)  # required for pygbag

asyncio.run(main())


