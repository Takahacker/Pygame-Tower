import pygame, sys, os, time, math
from Jogo_V14 import WIDTH,HEIGHT
from Jogo_V14 import main
from Tela_inicial import tela_inicial
pygame.init()
def victory():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    clock = pygame.time.Clock()
    victory_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    victory_background = pygame.image.load("assets/img/inicio.png")
    victory_background = pygame.transform.scale(victory_background, (WIDTH, HEIGHT))

    perdeu = True

    while perdeu:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    tela_inicial()
                    main()
                elif event.key == pygame.K_ESCAPE:
                    perdeu = False
                    pygame.quit
            
        victory_screen.blit(victory_background, (0, 0))
        pygame.display.flip()