import pygame
import random
import sys

# ---------------------------------Inicialização -------------------------------
pygame.init()
pygame.mixer.init()

#--------------------------------- Gera tela inicial ----------------------------
Comprimento_tela = 1000
Altura_tela = 800
Tela_inicial = pygame.display.set_mode((Comprimento_tela, Altura_tela))
pygame.display.set_caption("Tower defense")

font = pygame.font.Font(None, 60)
title_text = font.render("Tower Defense", True, (255, 255, 255))
start_text = font.render("Press SPACE to Start", True, (255, 255, 255))
title_text_rect = title_text.get_rect(center=(Comprimento_tela // 2, Altura_tela // 2 - 50))
start_text_rect = start_text.get_rect(center=(Comprimento_tela // 2, Altura_tela // 2 + 50))

#--------------------------------- Gera Tela principal ---------------------------------

game_screen = pygame.display.set_mode((Comprimento_tela, Altura_tela))
pygame.display.set_caption("Main Game")

#--------------------------------- Inicia Assets ---------------------------------

pygame.display.set_caption("Tower defense")
background_image = pygame.image.load("assets/img/background_inicial.jpeg")
game_background_image = pygame.image.load('assets/img/game_background.jpeg')
background_image = pygame.transform.scale(background_image, (Comprimento_tela, Altura_tela))
game_background_image = pygame.transform.scale(game_background_image, (Comprimento_tela, Altura_tela))

#--------------------------------- Inicia Estruturas de dados --------------------------------- 

# Classe Balões

class Balloon(pygame.sprite.Sprite):
    def __init__(self, color, path):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.image = pygame.Surface((20, 20))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = path[0][0]
        self.rect.y = path[0][1]
        self.path = path
        self.path_index = 0

# Classe Torres

class Tower(pygame.sprite.Sprite):
    def __init__(self, color, radius, cost):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.image = pygame.Surface((radius * 2, radius * 2))
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.radius = radius
        self.cost = cost
    def update(self, balloons):
        for balloon in balloons:
            if pygame.sprite.collide_circle(self, balloon):
                pass



running = True
Jogo_iniciado = False

while running:
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
        pygame.display.flip()