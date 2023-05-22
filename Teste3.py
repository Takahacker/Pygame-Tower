# ------------------Importação e Inicialização de bibliotecas --------------------------
import pygame
import random
import sys
pygame.init()
pygame.mixer.init()

# --------------------------------- Parâmetros ----------------------------

WIDTH = 800
HEIGHT = 600
FPS = 60
TAMANHO_QUADRADO= 50
GRID_COLOR = (255, 255, 255)
PATH_COLOR = (0, 255, 0)
Raio_bola = 10

#--------------------------------- Gera tela inicial ----------------------------
Tela_inicial = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower defense")

font = pygame.font.Font(None, 60)
title_text = font.render("Tower Defense", True, (255, 255, 255))
start_text = font.render("Press SPACE to Start", True, (255, 255, 255))
title_text_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
start_text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

#--------------------------------- Funções para cálculos ---------------------------------
def calcula_distancia(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
#--------------------------------- Gera Tela principal ---------------------------------

game_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Game")

#--------------------------------- Inicia Assets ---------------------------------

pygame.display.set_caption("Tower defense")
background_image = pygame.image.load("assets/img/background_inicial.jpeg")
game_background_image = pygame.image.load('assets/img/game_background.jpeg')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
game_background_image = pygame.transform.scale(game_background_image, (WIDTH, HEIGHT))

#--------------------------------- Inicia Estruturas de dados --------------------------------- 

# Coordenadas do Trajeto
Coordenadas_caminho = [
    (0, 2),
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
    (7, 6),
    (7, 5),
    (7, 4),
    (7, 3),
    (7, 2),
    (7, 1),
    (8, 1),
    (9, 1),
    (9, 2),
    (9, 3),
    (9, 4),
    (9, 5),
    (9, 6),
    (9, 7),
    (9, 8),
    (8, 8),
    (7, 8),
    (6, 8),
    (5, 8),
    (4, 8),
    (3, 8),
    (2, 8),
    (1, 8),
    (1, 9),
    (1, 10),
    (2, 10),
    (3, 10),
    (4, 10),
    (5, 10),
    (6, 10),
    (7, 10),
    (8, 10),
    (9, 10),
    (10, 10),
    (11, 10),
    (12, 10),
    (13, 10),
    (13, 11),
]

# Classe Bola
class Ball:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
        self.health = 100

clock = pygame.time.Clock()

# Cria Inimigos
red_ball = Ball((255, 0, 0), 6.0)
blue_ball = Ball((0, 0, 255), 5.0)
green_ball = Ball((0, 255, 0), 1.5)

# Ball varia
ball = red_ball
ball_position = (
    Coordenadas_caminho[0][0] * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2,
    Coordenadas_caminho[0][1] * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2,
)
ball_index = 0
Bola_visivel = True


running = True
Jogo_iniciado = False
# Game loop
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Jogo_iniciado = True

    if not Jogo_iniciado:
        Tela_inicial.blit(background_image, (0, 0))
        Tela_inicial.blit(title_text, title_text_rect)
        Tela_inicial.blit(start_text, start_text_rect)
        pygame.display.flip()
    else:
        game_screen.blit(game_background_image, (0, 0))
        
        if ball_index < len(Coordenadas_caminho) - 1:
            target_x = Coordenadas_caminho[ball_index + 1][0] * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2
            target_y = Coordenadas_caminho[ball_index + 1][1] * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2
            dx = target_x - ball_position[0]
            dy = target_y - ball_position[1]
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance > 0:
                speed = min(distance, ball.speed)
                direction_x = dx / distance
                direction_y = dy / distance
                ball_position = (
                    ball_position[0] + direction_x * speed,
                    ball_position[1] + direction_y * speed,
                )
            else:
                ball_index += 1
                if ball_index >= len(Coordenadas_caminho):
                    Bola_visivel = False
        Posicao_final = (13,11)
        # Checa se a bola chegou a última posição do trajeto
        if ball_index >= len(Coordenadas_caminho) - 1 and Coordenadas_caminho[ball_index] == Posicao_final:
            Bola_visivel = False

        # Desenha a Grade
        for x in range(0, WIDTH, TAMANHO_QUADRADO):
            pygame.draw.line(game_screen, GRID_COLOR, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TAMANHO_QUADRADO):
            pygame.draw.line(game_screen, GRID_COLOR, (0, y), (WIDTH, y))

        # Desenha o Trajeto Inimigo
        for point in Coordenadas_caminho:
            x = point[0] * TAMANHO_QUADRADO
            y = point[1] * TAMANHO_QUADRADO
            pygame.draw.rect(game_screen, PATH_COLOR, (x, y, TAMANHO_QUADRADO, TAMANHO_QUADRADO))

        # Desenha a bola se ela for visível
        if Bola_visivel:
            pygame.draw.circle(
                game_screen,
                ball.color,
                (int(ball_position[0]), int(ball_position[1])),
                Raio_bola,
            )

        pygame.display.flip()

pygame.quit()
sys.exit()
# Tower Class
class Tower:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.range = TOWER_RADIUS
        self.damage = TOWER_DAMAGE
        self.attack_speed = TOWER_ATTACK_SPEED
        self.attack_timer = 0.0

    def shoot_projectile(self, target):
        dx = target[0] - self.position[0]
        dy = target[1] - self.position[1]
        distance = (dx ** 2 + dy ** 2) ** 0.5
        direction_x = dx / distance
        direction_y = dy / distance
        projectile_position = (
            self.position[0] + direction_x * Raio_bola,
            self.position[1] + direction_y * Raio_bola,
        )
        return Projectile(projectile_position, (direction_x, direction_y), self.damage)

    def is_ball_in_range(self, ball):
        return distance(self.position, ball) <= self.range

class Projectile:
    def __init__(self, position, direction, damage):
        self.position = position
        self.direction = direction
        self.damage = damage

    def update(self):
        self.position = (
            self.position[0] + self.direction[0] * PROJECTILE_SPEED,
            self.position[1] + self.direction[1] * PROJECTILE_SPEED,
        )

# Create Towers
red_tower = Tower((255, 0, 0), (TAMANHO_QUADRADO // 2, TAMANHO_QUADRADO // 2))
blue_tower = Tower((0, 0, 255), (TAMANHO_QUADRADO // 2 + 2 * TAMANHO_QUADRADO, TAMANHO_QUADRADO // 2))
green_tower = Tower((0, 255, 0), (TAMANHO_QUADRADO // 2 + 4 * TAMANHO_QUADRADO, TAMANHO_QUADRADO // 2))

# Initialize Ball Variables
ball = Ball((255, 0, 0), 6.0)
ball_position = (
    path_points[0][0] * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2,
    path_points[0][1] * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2,
)
ball_index = 0
ball_visible = True

# Initialize Projectile Variables
projectiles = []

# Game State Variables
game_started = False

# Game Loop
running = True
while running:
    clock.tick(FPS)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_started = True
        elif event.type == pygame.MOUSEBUTTONDOWN and game_started:
            if event.button == 1:  # Left Mouse Button
                mouse_pos = pygame.mouse.get_pos()
                if distance(mouse_pos, red_tower.position) <= TAMANHO_QUADRADO // 2:
                    projectiles.append(red_tower.shoot_projectile(ball_position))
                elif distance(mouse_pos, blue_tower.position) <= TAMANHO_QUADRADO // 2:
                    projectiles.append(blue_tower.shoot_projectile(ball_position))
                elif distance(mouse_pos, green_tower.position) <= TAMANHO_QUADRADO // 2:
                    projectiles.append(green_tower.shoot_projectile(ball_position))


        # Update Projectiles
        for projectile in projectiles:
            projectile.update()

        # Check Collision between Projectiles and Ball
        for projectile in projectiles:
            if distance(projectile.position, ball_position) <= Raio_bola:
                ball.health -= projectile.damage
                projectiles.remove(projectile)
                if ball.health <= 0:
                    ball_visible = False

    # Render
    screen.blit(game_background_image, (0, 0))

    # Draw Grid
    for x in range(0, WIDTH, TAMANHO_QUADRADO):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TAMANHO_QUADRADO):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))

    # Draw Path
    for point in path_points:
        x = point[0] * TAMANHO_QUADRADO
        y = point[1] * TAMANHO_QUADRADO
        pygame.draw.rect(screen, PATH_COLOR, (x, y, TAMANHO_QUADRADO, TAMANHO_QUADRADO))

    # Draw Towers
    pygame.draw.circle(screen, red_tower.color, red_tower.position, TAMANHO_QUADRADO // 2)
    pygame.draw.circle(screen, blue_tower.color, blue_tower.position, TAMANHO_QUADRADO // 2)
    pygame.draw.circle(screen, green_tower.color, green_tower.position, TAMANHO_QUADRADO // 2)

