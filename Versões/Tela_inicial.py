import pygame, sys, os, time, math
pygame.init()
from Jogo_V14 import WIDTH, HEIGHT

def tela_inicial():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    clock = pygame.time.Clock()
    Tela_inicial = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ibis defender")
    font = pygame.font.Font(None, 60)
    title_text = font.render("Ibis Defender", True, (255, 255, 255))
    start_text = font.render("Press SPACE to Start", True, (255, 255, 255))
    title_text_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    start_text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    tutorial_tela = pygame.image.load('assets/img/tutorialatual.png')
    tutorial_tela = pygame.transform.scale(tutorial_tela, (WIDTH, HEIGHT))
    background_image = pygame.image.load("assets/img/inicio.png")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    def toca_musica(file, volume=1, loop=-1):
        pygame.mixer.music.load(file)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loop)

    def para_musica():
        pygame.mixer.music.stop()

    # Adicione as configurações da caixa de texto
    caixa_texto = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 + 100, 400, 40)
    cor_caixa_texto = (255, 255, 255)
    texto_digitado = ""

    inicio = True
    Jogo_iniciado = False
    tutorial = False

    # Game loop
    toca_musica('assets/snd/Musicas/musica.mp3')
    while inicio:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not Jogo_iniciado:
                        if not tutorial:
                            tutorial = True
                        else:
                            Jogo_iniciado = True

                    else:
                        tutorial = False
                        Jogo_iniciado = True
                        inicio = False
                elif event.key == pygame.K_BACKSPACE:
                    texto_digitado = texto_digitado[:-1]  # Remove o último caractere digitado
                else:
                    texto_digitado += event.unicode  # Adiciona o caractere digitado

        if not Jogo_iniciado:
            Tela_inicial.blit(background_image, (0, 0))
            Tela_inicial.blit(title_text, title_text_rect)
            Tela_inicial.blit(start_text, start_text_rect)
            pygame.draw.rect(Tela_inicial, cor_caixa_texto, caixa_texto, 2)
            fonte_caixa_texto = pygame.font.Font(None, 28)
            texto_caixa_texto = fonte_caixa_texto.render(texto_digitado, True, cor_caixa_texto)
            Tela_inicial.blit(texto_caixa_texto, (caixa_texto.x + 5, caixa_texto.y + 10))
            pygame.display.flip()

        elif tutorial:
            Tela_inicial.blit(tutorial_tela, (0, 0))
            pygame.display.flip()
        else:
            para_musica()
            inicio = False
