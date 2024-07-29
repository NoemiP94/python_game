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

### ciclo infinito principale ###
while True:
    # gravità
    uccello_vely += 1
    uccelloy += uccello_vely
    # leggere gli eventi
    for event in pygame.event.get():
        # se viene premuto un tasto sulla tastiera e questo tasto è la FRECCIA SU l'uccello deve dare una botta di ali
        if (event.type == pygame.KEYDOWN
            and event.key == pygame.K_UP):
            # smette di scendere e inizia a salire
            uccello_vely = -10
        # se viene cliccato il tasto di chiusura il gioco si chiude 
        if event.type == pygame.QUIT:
            pygame.quit()


    # aggiornamento schermo
    disegna_oggetti()
    aggiorna()
