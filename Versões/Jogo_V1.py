# Inicialização
import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

# Gera Tela inicial
Comprimento_tela = 1000
Altura_tela = 800
Tela_inicial = pygame.display.set_mode((Comprimento_tela,Altura_tela))
pygame.display.set_caption("Tower defense")
background_image = pygame.image.load("assets/img/background_inicial.jpeg")

# Gera Tela Principal
game_screen = pygame.display.set_mode((Comprimento_tela,Altura_tela))
pygame.display.set_caption("Main Game")
# Inicia Assets
background_tela_inicial = pygame.image.load("assets/img/background_inicial.jpeg")
game_background_image = pygame.image.load("assets/img/game_background.jpeg")

# Create font object
font = pygame.font.Font(None, 60)

# Create text objects
title_text = font.render("Tower Defense", True, (255, 255, 255))
start_text = font.render("Press SPACE to Start", True, (255, 255, 255))

# Set the positions of the text objects
title_text_rect = title_text.get_rect(center=(Comprimento_tela // 2, Altura_tela // 2 - 50))
start_text_rect = start_text.get_rect(center=(Comprimento_tela // 2, Altura_tela// 2 + 50))

# Main game loop
running = True
Jogo_iniciado = False
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Jogo_iniciado = True
    if not Jogo_iniciado:
        Tela_inicial.blit(background_tela_inicial, (0, 0))
        Tela_inicial.blit(title_text, title_text_rect)
        Tela_inicial.blit(start_text, start_text_rect)
        pygame.display.flip()
    else:
        game_screen.blit((background_image),(0,0))
        pygame.display.flip()

    # Update the display
