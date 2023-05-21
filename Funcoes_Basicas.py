# Inicialização
import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

# Gera Tela inicial
Comprimento_tela_inicial = 700
Altura_tela_inicial = 800
window = pygame.display.set_mode((Comprimento_tela_inicial,Altura_tela_inicial))
pygame.display.set_caption("Tower defense")
background_image = pygame.image.load("assets/img/background_inicial.jpeg")

# Inicia Assets


# Load background image
background_image = pygame.image.load("assets/img/background_inicial.jpeg")  # Replace "background.jpg" with your image file

# Create font object
font = pygame.font.Font(None, 60)

# Create text objects
title_text = font.render("Tower Defense", True, (255, 255, 255))
start_text = font.render("Press SPACE to Start", True, (255, 255, 255))

# Set the positions of the text objects
title_text_rect = title_text.get_rect(center=(Comprimento_tela_inicial // 2, Altura_tela_inicial // 2 - 50))
start_text_rect = start_text.get_rect(center=(Comprimento_tela_inicial // 2, Altura_tela_inicial // 2 + 50))

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False

    # Draw the background image
    window.blit(background_image, (0, 0))

    # Draw the text objects on the screen
    window.blit(title_text, title_text_rect)
    window.blit(start_text, start_text_rect)

    # Update the display
    pygame.display.flip()

