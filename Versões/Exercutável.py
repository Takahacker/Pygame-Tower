import pygame, sys, os, time, math
from Jogo_V14 import main
from Tela_inicial import tela_inicial
#from Tela_vitoria import victory
#from gameover import gameover
pygame.init()
inicio = True
tela_inicial()
main()

from Jogo_V14 import vida,tempo,dinheiros,WIDTH,HEIGHT
pontuacao = ((vida*10 -tempo*10 + dinheiros)/10)*100

background_image = pygame.image.load("assets/img/inicio.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))