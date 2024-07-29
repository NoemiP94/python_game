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

# COSTANTI GLOBALI
# finestra di gioco
SCHERMO = pygame.display.set_mode((288, 512))
# frame per second verrà aggiornata la finestra di gioco
FPS = 50
# velocità di avanzamento
VEL_AVANZ = 3

# CLASSE
# generare i tubi
class tubi_classe:
    # metodo eseguito appena la classe viene chiamata per creare un nuovo oggetto
    def __init__(self):
        # posizione iniziale orizzontale
        self.x = 300
        # posizione verticale diversa random per ogni tubo da -75 a 150
        self.y = random.randint(-75,150)
    # metodo che viene chiamato dopo la creazione dell'oggetto quando vogliamo
    def avanza_e_disegna(self):
        # muoviamo il tubo verso l'uccello ( che è fermo, è il mondo che si muove verso di lui)
        self.x -= VEL_AVANZ
        SCHERMO.blit(tubo_giu, (self.x, self.y+210))
        SCHERMO.blit(tubo_su,(self.x, self.y-210))


# FUNZIONI
def disegna_oggetti():
    SCHERMO.blit(sfondo, (0,0))
    # disegna i tubi
    for t in tubi:
        t.avanza_e_disegna()
    SCHERMO.blit(uccello, (uccellox,uccelloy))
    SCHERMO.blit(base, (basex, 400))

# aggiorna la schermata di gioco e definisce gli FPS
def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def inizializza():
    global uccellox, uccelloy, uccello_vely
    global basex
    global tubi
    uccellox, uccelloy = 60, 150
    uccello_vely = 0
    basex = 0
    # inizialmente la lista dei tubi è vuota
    tubi = []
    # poi viene riempita
    tubi.append(tubi_classe())
   
def hai_perso():
    SCHERMO.blit(gameover, (50,180))
    aggiorna()
    ricominciamo = False
    # verrà eseguito all'infinito fino a quando ricominciamo non diventa True
    while not ricominciamo:
        for event in pygame.event.get():
            # quando viene premuto SPAZIO
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # riporta il gioco allo stato iniziale
                inizializza()
                # interrompe il ciclo
                ricominciamo = True
            # se viene cliccato il tasto di chiusura il gioco si chiude 
            if event.type == pygame.QUIT:
                pygame.quit()

inizializza()

### ciclo infinito principale ###
while True:
    # ad ogni ciclo la base viene spostata sempre più a sinistra
    basex -= VEL_AVANZ
    # se la posizione della base è minore ad un certo valore lo riporta alla posizione iniziale
    if basex < -45: basex = 0
    # gravità
    uccello_vely += 1
    uccelloy += uccello_vely
    # comandi
    for event in pygame.event.get():
        # se viene premuto un tasto sulla tastiera e questo tasto è la FRECCIA SU l'uccello deve dare una botta di ali
        if (event.type == pygame.KEYDOWN
            and event.key == pygame.K_UP):
            # smette di scendere e inizia a salire
            uccello_vely = -10
        # se viene cliccato il tasto di chiusura il gioco si chiude 
        if event.type == pygame.QUIT:
            pygame.quit()
    #quando l'ultimo tubo della lista raggiunge l'uccello ne deve essere disegnato un'altro
    if tubi[-1].x >150: tubi.append(tubi_classe())
    #se l'uccello tocca la base -> gameover
    if uccelloy > 380:
        hai_perso()


    # aggiornamento schermo
    disegna_oggetti()
    aggiorna()
