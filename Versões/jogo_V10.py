# ------------------Importação de bibliotecas --------------------------
import pygame, sys, os, time, math
pygame.init()
# --------------------------------- Parâmetros ----------------------------
WIDTH = 800
HEIGHT = 600
INIMIGO_HEIGHT = 50
INIMIGO_WIDTH = 38
TORRE_HEIGHT = 200
TORRE_WIDTH = 80


squsize = 50
fps = 60

# --------------------------------- Listas dos elementos do Jogo ----------------------------
Inimigos_lista = []
torres_lista = []
bullet_list = []
icones_lista = []
sender_lista = []
 
# --------------------------------- Cores ----------------------------
cores = {
    'yellow':   (255,255,0),
    'lime':     (0,255,0),
    'darkblue': (0,0,255),
    'aqua':     (0,255,255),
    'magenta':  (255,0,255),
    'purple':   (128,0,128),
    'green':    (97,144,0),
    'purple':   (197,125,190),
    'brown':    (110,73,32),}

# --------------------------------- Sons ----------------------------

# --------------- Música
def toca_musica(file, volume=1, loop=-1):
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loop)
   
def para_musica(): pygame.mixer.music.stop()

# --------------------------------- Imagens----------------------------

#---------- Função para carregar os Assets de Imagens
def carrega_imagem(file,tamanho=None):
    imagem = pygame.image.load(file).convert_alpha()
    return pygame.transform.scale(imagem,tamanho) if tamanho else imagem

# ------------ Classe Jogador -----------------
class Player:
    towers = [
        'Gustavo',
        'Belarmino',
        'Husky',
        ]

    def __init__(self):
        self.health = 100
        self.money = 650

player = Player()


inimigoImageArray = dict()
TowerImageArray = dict()

# --------------------------------- Carrega Imagens das Torres ----------------------------
def loadImages():
    # Torres
    for tower in player.towers: 
        TowerImageArray[tower] = carrega_imagem('towers/'+tower+'.png')
        TowerImageArray[tower] = pygame.transform.scale(TowerImageArray[tower],(TORRE_WIDTH,TORRE_HEIGHT))


# --------------------------------- Inimigo ----------------------------
    Inimigo = carrega_imagem('assets/img/Bola.png')
    Inimigo = pygame.transform.scale(Inimigo,(INIMIGO_WIDTH,INIMIGO_HEIGHT))
    inimigoImageArray['red'] = Inimigo
    WIDTH,HEIGHT = Inimigo.get_size()
    
    for name in cores:
        image = Inimigo.copy()
        for x in range(WIDTH):
            for y in range(HEIGHT):
                p = image.get_at((x,y))[:-1]
                if p not in ((0,0,0),(255,255,255)):
                    c = cores[name]
                    r,g,b = p[0]*c[0]/255, p[0]*c[1]/255, p[0]*c[2]/255
                    image.set_at((x,y),(min(int(r),255),min(int(g),255),min(int(b),255)))
        inimigoImageArray[name] = image


 # --------------------------------- Classe Mapa ----------------------------
class Map:
    def __init__(self):
        self.map = 'monkey lane'
        self.loadmap()

    def loadmap(self):
        self.Coordenadas = eval(open('maps/%s/Coordenadas.txt' % self.map,'r').read())
        self.waves = eval(open('maps/%s/waves.txt' % self.map,'r').read())

    def getmovelist(self):
        self.pathpoints = []
        for i in range(len(self.Coordenadas)-1):
            a,b = self.Coordenadas[i:i+2]
            self.pathpoints+=[0]

    def get_background(self):
        background = carrega_imagem('maps/%s/image.jpeg' % self.map)
        background = pygame.transform.scale(background, (700,600 ))
        for i in range(len(self.Coordenadas)-1): pygame.draw.line(background,(0,0,0),self.Coordenadas[i],self.Coordenadas[i+1])
        return background

mapvar = Map()

 # --------------------------------- Classe Inimigo ----------------------------
class inimigo:
    layers = [ # Nome Vida Speed Recompensa
        ('red',      1, 1.0, 0),
        ('darkblue', 1, 1.0, 0),
        ('green',    1, 1.2, 0),
        ('yellow',   1, 2.0, 0),]

    def __init__(self,layer):
        self.layer = layer
        self.setlayer()
        self.Coordenadas = mapvar.Coordenadas
        self.pos = list(self.Coordenadas[0])
        self.target = 0
        self.next_target()
        self.rect = self.image.get_rect(center=self.pos)
        self.distance = 0

        Inimigos_lista.append(self)

    def setlayer(self): self.name,self.health,self.speed,self.cashprize = self.layers[self.layer]; self.image = inimigoImageArray[self.name]
    def nextlayer(self): self.layer-=1; self.setlayer()

    def next_target(self):
        if self.target<len(self.Coordenadas)-1:
            self.target+=1; t=self.Coordenadas[self.target]; self.angle = 180-(math.atan2(t[0]-self.pos[0],t[1]-self.pos[1]))/(math.pi/180)
            self.vx,self.vy = math.sin(math.radians(self.angle)),-math.cos(math.radians(self.angle))
        else: self.kill(); player.health-=self.layer+1

    def hit(self,damage):
        player.money+=1
        self.health -= damage
        if self.health<=0:
            player.money+=self.cashprize
            self.nextlayer() if self.layer>0 else self.kill()

    def kill(self): Inimigos_lista.remove(self)

    def move(self,frametime):
        speed = frametime*fps*self.speed
        a,b = self.pos,self.Coordenadas[self.target]
        
        a[0] += self.vx*speed
        a[1] += self.vy*speed
        
        if (b[0]-a[0])**2+(b[1]-a[1])**2<=speed**2: self.next_target()
        self.rect.center = self.pos
        self.distance+=speed

class Tower:
    def __init__(self,pos):
        self.targetTimer = 0
        self.rect = self.image.get_rect(center=pos)
        torres_lista.append(self)

    def takeTurn(self,frametime,screen):
        self.startTargetTimer = self.firerate
        self.targetTimer -= frametime
        if self.targetTimer<=0:
            inimigopoint = self.target()
            if inimigopoint:
                pygame.draw.line(screen,(255,255,255),self.rect.center,inimigopoint)
                self.targetTimer=self.startTargetTimer

    def target(self):
        for inimigo in sorted(Inimigos_lista,key=lambda i: i.distance,reverse=True):
            if (self.rect.centerx-inimigo.rect.centerx)**2+(self.rect.centery-inimigo.rect.centery)**2<=self.rangesq:
                self.angle = int(get_angle(self.rect.center,inimigo.rect.center))
                self.image = pygame.transform.rotate(self.imagecopy,-self.angle)
                self.rect = self.image.get_rect(center=self.rect.center)
                inimigo.hit(self.damage)
                return inimigo.rect.center

class createTower(Tower):
    def __init__(self,tower,pos,info):
        self.tower = tower
        self.cost,self.firerate,self.range,self.damage = info
        self.rangesq = self.range**2
        
        self.image = TowerImageArray[tower]
        self.imagecopy = self.image.copy()
        self.angle = 0
        Tower.__init__(self,pos)

# --------------------------------- Classe de ícone no Menu do Jogador ----------------------------
class Icon:
    towers = { # Custo Cadencia_de_Tiro Alcance Dano
        'Gustavo'     : [ 215, 1.0, 100, 1],
        'Belarmino'   : [ 390, 1.0, 40, 1],
        'Husky'       : [ 430, 1.0, 200, 1],
}

    def __init__(self,tower):
        self.tower = tower
        self.cost,self.firerate,self.range,self.damage = self.towers[tower]
        icones_lista.append(self)
        self.img = pygame.transform.scale(TowerImageArray[tower],(50,100))
        i = player.towers.index(tower); x,y = i%2,i//2
        self.rect = self.img.get_rect(x=700+x*(41+6)+6,y=100+y*(41+6)+6)


def dispText(screen,wavenum):
    font = pygame.font.Font(None,20)
    h = font.get_height()+2
    strings = [('Round: %d/%d' % (wavenum,len(mapvar.waves)),(200,20)),
               (str(player.money),(730,15)),
               (str(max(player.health,0)),(730,45))]
    for string,pos in strings:
        text = font.render(string,True,(255,255,255))
        screen.blit(text,text.get_rect(midleft=pos))

 # --------------------------------- Desenha torres no mapa ----------------------------
def desenha_torre(screen,tower,selected):
    screen.blit(tower.image,tower.rect)
    if tower==selected:
        rn = tower.range
        surface = pygame.Surface((2*rn,2*rn)).convert_alpha(); surface.fill((0,0,0,0))
        pygame.draw.circle(surface,(0,255,0,85),(rn,rn),rn)
        screen.blit(surface,tower.rect.move((-1*rn,-1*rn)).center)


 # --------------------------------- Envia Ondas de inimigos ----------------------------
class Sender:
    def __init__(self,wave):
        self.wave = wave; self.timer = 0; self.rate = 1
        self.inimigos = []; inimigos = mapvar.waves[wave-1].split(',')
        for inimigo in inimigos:
            amount,layer = inimigo.split('*')
            self.inimigos += [eval(layer)-1]*eval(amount)
        sender_lista.append(self)

    def update(self,frametime,wave):
        if not self.inimigos:
            if not Inimigos_lista: sender_lista.remove(self); wave+=1; player.money+=99+self.wave
        elif self.timer>0: self.timer -= frametime
        else: self.timer = self.rate; inimigo(self.inimigos[0]); del self.inimigos[0]
        return wave



# Tela principal

def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption('Ibis Defender')
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,20)

    mapvar.getmovelist()

    background = pygame.Surface((800,600)); background.set_colorkey((0,0,0))
    heart = carrega_imagem('images/heart.png')
    money = carrega_imagem('images/money.png')
    plank= carrega_imagem('images/plank.png')
    plank = pygame.transform.scale(plank,(100,25))

    # Preenche o menu com Placas
    w,h = plank.get_size()
    for y in range(HEIGHT//h): background.blit(plank,(WIDTH-w,y*h))
    for y in range(3):
        for x in range(WIDTH//w): 
            background.blit(plank,(x*w,HEIGHT-(y+1)*h))

    background.blit(money,(WIDTH-w+6,h//2-money.get_height()//2))
    background.blit(heart,(WIDTH-w+6,h+h//2-heart.get_height()//2))


    
    level_img= mapvar.get_background()
    loadImages()
    for tower in player.towers: Icon(tower)
    selected = None
    speed = 3
    wave = 1
    toca_musica('music/maintheme.mp3')

    # Loop Principal

   