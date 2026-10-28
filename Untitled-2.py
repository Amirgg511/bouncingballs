
import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls")

clock = pygame.time.Clock()


class Ball:
    def __init__(self, x, y, speed_x, speed_y, colour):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.colour = colour
        self.radius = 20

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.speed_x = -self.speed_x

        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.speed_y = -self.speed_y

    def draw(self):
        pygame.draw.circle(
            screen,
            self.colour,
            (int(self.x), int(self.y)),
            self.radius
        )


# Create a list of 5 Ball objects
balls = []

for i in range(5):
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
    speed_x = random.choice([-5, -4, 4, 5])
    speed_y = random.choice([-5, -3, 3, 5])
    colour = (
        random.randint(50, 255),
        random.randint(50, 255),
        random.randint(50, 255)
    )

    ball = Ball(x, y, speed_x, speed_y, colour)
    balls.append(ball)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 40))

    for ball in balls:
        ball.move()
        ball.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
