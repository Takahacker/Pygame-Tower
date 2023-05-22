# ------------------Importação e Inicialização de bibliotecas ---------------------------------
import pygame
import sys
pygame.init()
pygame.mixer.init()

# --------------------------------- Parâmetros ------------------------------------------

WIDTH = 1500
HEIGHT = 900
FPS = 60
TAMANHO_QUADRADO = 70
GRID_COLOR = (255, 255, 255)
PATH_COLOR = (111, 132, 50)
INIMIGO_WIDTH = 38
INIMIGO_HEIGHT = 50
Raio_bola = 10

#--------------------------------- Gera tela inicial ------------------------------------

Tela_inicial = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ibis defender")

font = pygame.font.Font(None, 60)
title_text = font.render("Ibis Defender", True, (255, 255, 255))
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

# Backgrounds
pygame.display.set_caption("Tower defense")
background_image = pygame.image.load("assets/img/background_inicial.jpeg")
game_background_image = pygame.image.load('assets/img/game_background.jpeg')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
game_background_image = pygame.transform.scale(game_background_image, (WIDTH, HEIGHT))

# Inimigos
Amongus = pygame.image.load("assets/img/Amongus.png").convert_alpha()
Amongus = pygame.transform.scale(Amongus,(INIMIGO_WIDTH,INIMIGO_HEIGHT))


# Torres

tower_image = pygame.image.load("assets/img/Lionel-Messi.png").convert_alpha()
tower_image = pygame.transform.scale(tower_image, (TAMANHO_QUADRADO, TAMANHO_QUADRADO))


tower_icon_image = pygame.image.load("assets/img/Lionel-Messi.png").convert_alpha()
tower_icon_image = pygame.transform.scale(tower_icon_image, (50, 50))



#--------------------------------- Inicia Estruturas de dados ---------------------------------

# Coordenadas do Trajeto
Coordenadas_caminho = [
(0,2),
(1,2),
(2, 2),
(3, 2),
(4, 2),
(5, 2),
(6, 2),
(7, 2),
(7, 3),
(7, 4),
(6, 4),
(5, 4),
(4, 4),
(3, 4),
(3, 5),
(3, 6),
(4, 6),
(5, 6),
(6, 6),
(7, 6),
(8, 6),
(9, 6),
(9, 5),
(9, 4),
(9, 3),
(9, 2),
(9, 1),
(10, 1),
(11, 1),
(11, 2),
(11, 3),
(11, 4),
(11, 5),
(11, 6),
(11, 7),
(11, 8),
(10, 8),
(9, 8),
(8, 8),
(7, 8),
(6, 8),
(5, 8),
(4, 8),
(3, 8),
(3, 9),
(3, 10),
(4, 10),
(5, 10),
(6, 10),
(7, 10),
(8, 10),
(9, 10),
(10, 10),
(11, 10),
(12,10),
(13, 10),
(13, 9),
(13, 8),
(13, 7),
(13, 6),
(13, 6),
(14, 6),
(15, 6),
(16, 6),
(17, 6),
(18, 6),
(19, 6),
(20, 6),
]
# ------------------------------------------ Classe Bola----------------------------------------------------
class Ball:
    def __init__(self, color, speed, damage, vida):
        self.color = color
        self.speed = speed
        self.health = 100
        self.damage = damage
        self.vida = vida

clock = pygame.time.Clock()

# Cria Inimigos
red_ball = Ball((255, 0, 0), 6.0, 10, 100)
blue_ball = Ball((0, 0, 255), 5.0, 20, 150)
green_ball = Ball((0, 255, 0), 1.5, 30, 200)

# Ball varia
ball = red_ball
damage_applied = False
ball_position = (
    Coordenadas_caminho[0][0] * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2,
    Coordenadas_caminho[0][1] * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2,
)
ball_index = 0
Bola_visivel = True
# --------------------------------- Classe Torre --------------------------------------

class Tower:
    def __init__(self, image, damage, range):
        self.image = image
        self.damage = damage
        self.range = range
        self.position = None

    def set_position(self, position):
        self.position = position

    def draw(self, screen):
        if self.position:
            screen.blit(self.image, self.position)

# Create tower
tower = Tower(tower_image, 10, 100)

# ---------------------------------Inicia o Loop Principal --------------------------------------
running = True
Jogo_iniciado = False

# Indicador de vida do Jogador
Player_life = 100


# Game loop
while running:
    clock.tick(FPS)
    # checa eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Jogo_iniciado = True
                
    # Tela inicial

    if not Jogo_iniciado:
        Tela_inicial.blit(background_image, (0, 0))
        Tela_inicial.blit(title_text, title_text_rect)
        Tela_inicial.blit(start_text, start_text_rect)
        pygame.display.flip()

    # Inicia a tela principal 

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

        Posicao_final = Coordenadas_caminho[-1]
        # Checa se a bola chegou a última posição do trajeto
        if ball_index >= len(Coordenadas_caminho) - 1 and ball_position == (
            Posicao_final[0] * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2,
            Posicao_final[1] * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2,
        ):
            if not damage_applied:
                damage_applied = True
                Player_life -= ball.damage
                Bola_visivel = False

        # Atualiza a tela
        game_screen.blit(game_background_image, (0, 0))

        # Desenha o trajeto

        for coord in Coordenadas_caminho:
            x = coord[0] * TAMANHO_QUADRADO
            y = coord[1] * TAMANHO_QUADRADO
            pygame.draw.rect(game_screen, PATH_COLOR, (x, y, TAMANHO_QUADRADO,TAMANHO_QUADRADO))


        # Desenha a bola
        if Bola_visivel:
            ball_rect = Amongus.get_rect(center=(int(ball_position[0]), int(ball_position[1])))
            game_screen.blit(Amongus, ball_rect)
            #pygame.draw.circle(game_screen, ball.color, (int(ball_position[0]), int(ball_position[1])), Raio_bola)

        # Desenha a vida do jogador
        player_health_text = font.render(f"Vida: {Player_life}", True, (255, 255, 255))
        game_screen.blit(player_health_text, (10, 10))

        pygame.display.flip()

    # Verifica se o jogo acabou
    if Player_life <= 0:
        running = False
        game_over_text = font.render("Game Over", True, (255, 255, 255))
        game_screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(3000)

pygame.quit()
sys.exit()