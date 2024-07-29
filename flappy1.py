import pygame
import random

# avvia pygame
pygame.init() 

# importare immagini
sfondo = pygame.image.load('img/sfondo.png')
uccello = pygame.image.load('img/uccello.png')
base = pygame.image.load('img/base.png')
gameover = pygame.image.load('img/gameover.png')
tubo_giu = pygame.image.load('img/tubo.png')
# per tubo_su usiamo la stessa img di tubo_giu ma utilizzando la funzione trasform e il flip(nome_file_da_trasformare, flip orizzontale(boolean), flip verticale(boolean))
tubo_su = pygame.transform.flip(tubo_giu, False, True)

# finestra di gioco
SCHERMO = pygame.display.set_mode((288, 512))
# frame per second verrà aggiornata la finestra di gioco
FPS = 50

def disegna_oggetti():
    SCHERMO.blit(sfondo, (0,0))
    SCHERMO.blit(uccello, (uccellox,uccelloy))

# aggiorna la schermata di gioco e definisce gli FPS
def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def inizializza():
    global uccellox, uccelloy, uccello_vely
    uccellox, uccelloy = 60, 150
    uccello_vely = 0

inizializza()

# ciclo infinito
while True:
    uccello_vely += 1
    uccelloy += uccello_vely
    disegna_oggetti()
    aggiorna()
