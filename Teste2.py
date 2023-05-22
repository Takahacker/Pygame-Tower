import pygame
import sys

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60
SQUARE_SIZE = 50
GRID_COLOR = (255, 255, 255)
PATH_COLOR = (0, 255, 0)
BALL_COLOR = (255, 0, 0)
BALL_RADIUS = 10

# Path coordinates
path_points = [
    (0,2),
    (1, 2),
    (2, 2),
    (3, 2),
    (4, 2),
    (4, 3),
    (4, 4),
    (3, 4),
    (2, 4),
    (1, 4),
    (1, 5),
    (1, 6),
    (2, 6),
    (3, 6),
    (4, 6),
    (5, 6),
    (6, 6),
    (7,6),
    (7,5,),
    (7,4),
    (7,3),
    (7,2),
    (7,1),
    (8,1),
    (9,1),
    (9,2),
    (9,3),
    (9,4),
    (9,5),
    (9,6),
    (9,7),
    (9,8),
    (8,8),
    (7,8),
    (6,8),
    (5,8),
    (4,8),
    (3,8),
    (2,8),
    (1,8),
    (1,9),
    (1,10),
    (2,10),
    (3,10),
    (4,10),
    (5,10),
    (6,10),
    (7,10),
    (8,10),
    (9,10),
    (10,10),
    (11,10),
    (12,10),
    (13,10),
    (13,11),
]

# Initialize Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()

# Ball variables
ball_position = (path_points[0][0] * SQUARE_SIZE + SQUARE_SIZE // 2,
                 path_points[0][1] * SQUARE_SIZE + SQUARE_SIZE // 2)
ball_index = 0

# Game loop
running = True
while running:
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ball position
    if ball_index < len(path_points) - 1:
        target_x = path_points[ball_index + 1][0] * SQUARE_SIZE + SQUARE_SIZE // 2
        target_y = path_points[ball_index + 1][1] * SQUARE_SIZE + SQUARE_SIZE // 2
        dx = target_x - ball_position[0]
        dy = target_y - ball_position[1]
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance > 0:
            speed = min(distance, 2.5)
            direction_x = dx / distance
            direction_y = dy / distance
            ball_position = (ball_position[0] + direction_x * speed, ball_position[1] + direction_y * speed)
        else:
            ball_index += 1
            if ball_index >= len(path_points):
                running = False

    # Draw grid overlay
    for x in range(0, WIDTH, SQUARE_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, SQUARE_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))

    # Draw path
    for point in path_points:
        x = point[0] * SQUARE_SIZE
        y = point[1] * SQUARE_SIZE
        pygame.draw.rect(screen, PATH_COLOR, (x, y, SQUARE_SIZE, SQUARE_SIZE))

    # Draw ball
    pygame.draw.circle(screen, BALL_COLOR, (int(ball_position[0]), int(ball_position[1])), BALL_RADIUS)

    pygame.display.flip()

pygame.quit()
sys.exit()
