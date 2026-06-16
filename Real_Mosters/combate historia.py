import pygame
import random
import sys
import time
import math

pygame.init()

# -------------------------------------------------
# CONFIG
# -------------------------------------------------
ANCHO = 1200
ALTO = 700

screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Historion Battle")

clock = pygame.time.Clock()

# -------------------------------------------------
# FUENTES
# -------------------------------------------------
fuente = pygame.font.SysFont("timesnewroman", 28)
fuente_grande = pygame.font.SysFont("timesnewroman", 42, bold=True)

# -------------------------------------------------
# COLORES
# -------------------------------------------------
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (200,40,40)
VERDE = (50,200,50)
MARRON = (120,70,20)
DORADO = (210,180,70)

# -------------------------------------------------
# FONDO
# -------------------------------------------------
fondo = pygame.image.load(
    "imagenes/fondo_historia.png"
)

fondo = pygame.transform.scale(
    fondo,
    (ANCHO,ALTO)
)

# -------------------------------------------------
# PERGAMINO
# -------------------------------------------------
pergamino = pygame.image.load(
    "imagenes/pergamino.png"
)

pergamino = pygame.transform.scale(
    pergamino,
    (750,300)
)

# -------------------------------------------------
# RELOJ DE ARENA
# -------------------------------------------------
reloj = pygame.image.load(
    "imagenes/reloj.png"
)

reloj = pygame.transform.scale(
    reloj,
    (120,120)
)

# -------------------------------------------------
# MONSTRUOS
# -------------------------------------------------
class Monstruo:

    def __init__(self,nombre,vida,imagen):

        self.nombre = nombre
        self.vida = vida
        self.max_vida = vida

        self.imagen = pygame.image.load(imagen)

        self.imagen = pygame.transform.scale(
            self.imagen,
            (220,220)
        )

    def vivo(self):

        return self.vida > 0

# -------------------------------------------------
# JUGADOR
# -------------------------------------------------
jugador = Monstruo(
    "Chronos",
    120,
    "imagenes/explorion.png"
)

# -------------------------------------------------
# ENEMIGOS
# -------------------------------------------------
enemigos = [

    Monstruo(
        "Imperius",
        70,
        "imagenes/paisor.png"
    ),

    Monstruo(
        "Warlock",
        90,
        "imagenes/oceanix.png"
    )
]

def elegir_enemigo():

    vivos = [
        e for e in enemigos
        if e.vivo()
    ]

    if vivos:
        return vivos[0]

    return None

enemigo = elegir_enemigo()

# -------------------------------------------------
# EVENTOS HISTORICOS
# -------------------------------------------------
eventos = [

    {
        "correcto":[
            "Descubrimiento de América",
            "Revolución Francesa",
            "Primera Guerra Mundial"
        ]
    },

    {
        "correcto":[
            "Caída del Imperio Romano",
            "Descubrimiento de América",
            "Independencia Argentina"
        ]
    },

    {
        "correcto":[
            "Revolución Industrial",
            "Independencia Argentina",
            "Segunda Guerra Mundial"
        ]
    }
]

# -------------------------------------------------
# CARGAR EVENTO
# -------------------------------------------------
evento_actual = random.choice(eventos)

eventos_mezclados = evento_actual["correcto"][:]

random.shuffle(eventos_mezclados)

# -------------------------------------------------
# RECTANGULOS
# -------------------------------------------------
rects = []

for i, texto in enumerate(eventos_mezclados):

    rect = pygame.Rect(
        250,
        220 + i*90,
        700,
        60
    )

    rects.append({

        "texto": texto,
        "rect": rect
    })

# -------------------------------------------------
# DRAG
# -------------------------------------------------
dragging = None
offset_y = 0

# -------------------------------------------------
# TEMPORIZADOR
# -------------------------------------------------
TIEMPO_LIMITE = 20

inicio_tiempo = time.time()

# -------------------------------------------------
# MENSAJES
# -------------------------------------------------
mensaje = "Ordená los eventos históricos"

# -------------------------------------------------
# PARTICULAS
# -------------------------------------------------
particulas = []

def crear_particulas(x,y):

    for i in range(25):

        particulas.append({

            "x":x,
            "y":y,

            "vx":random.randint(-5,5),
            "vy":random.randint(-5,5),

            "vida":random.randint(20,40)
        })

def actualizar_particulas():

    for p in particulas[:]:

        p["x"] += p["vx"]
        p["y"] += p["vy"]

        p["vida"] -= 1

        pygame.draw.circle(
            screen,
            DORADO,
            (int(p["x"]),int(p["y"])),
            4
        )

        if p["vida"] <= 0:
            particulas.remove(p)

# -------------------------------------------------
# TEXTO BORDE
# -------------------------------------------------
def texto_borde(texto,fuente,color,borde,x,y):

    for dx in [-2,0,2]:
        for dy in [-2,0,2]:

            if dx != 0 or dy != 0:

                sombra = fuente.render(
                    texto,
                    True,
                    borde
                )

                screen.blit(
                    sombra,
                    (x+dx,y+dy)
                )

    base = fuente.render(
        texto,
        True,
        color
    )

    screen.blit(base,(x,y))

# -------------------------------------------------
# PANEL VIDA
# -------------------------------------------------
def dibujar_panel(x,y,monstruo):

    pygame.draw.rect(
        screen,
        BLANCO,
        (x,y,260,90),
        border_radius=20
    )

    pygame.draw.rect(
        screen,
        NEGRO,
        (x,y,260,90),
        4,
        border_radius=20
    )

    texto_borde(
        monstruo.nombre,
        fuente,
        NEGRO,
        BLANCO,
        x+15,
        y+10
    )

    vida_ratio = monstruo.vida / monstruo.max_vida

    pygame.draw.rect(
        screen,
        ROJO,
        (x+15,y+50,210,18),
        border_radius=10
    )

    pygame.draw.rect(
        screen,
        VERDE,
        (x+15,y+50,210*vida_ratio,18),
        border_radius=10
    )

# -------------------------------------------------
# NUEVA RONDA
# -------------------------------------------------
def nueva_ronda():

    global evento_actual
    global eventos_mezclados
    global rects
    global inicio_tiempo

    evento_actual = random.choice(eventos)

    eventos_mezclados = evento_actual["correcto"][:]

    random.shuffle(eventos_mezclados)

    rects = []

    for i, texto in enumerate(eventos_mezclados):

        rect = pygame.Rect(
            250,
            220 + i*90,
            700,
            60
        )

        rects.append({

            "texto": texto,
            "rect": rect
        })

    inicio_tiempo = time.time()

# -------------------------------------------------
# VERIFICAR ORDEN
# -------------------------------------------------
def verificar():

    orden_actual = []

    rects_ordenados = sorted(
        rects,
        key=lambda r: r["rect"].y
    )

    for r in rects_ordenados:

        orden_actual.append(
            r["texto"]
        )

    return (
        orden_actual ==
        evento_actual["correcto"]
    )

# -------------------------------------------------
# LOOP
# -------------------------------------------------
running = True

while running:

    enemigo = elegir_enemigo()

    screen.blit(fondo,(0,0))

    # GANAR
    if enemigo is None:

        texto_borde(
            "GANASTE",
            fuente_grande,
            VERDE,
            NEGRO,
            470,
            320
        )

        pygame.display.update()

        pygame.time.delay(4000)

        break

    # PERDER
    if jugador.vida <= 0:

        texto_borde(
            "PERDISTE",
            fuente_grande,
            ROJO,
            NEGRO,
            450,
            320
        )

        pygame.display.update()

        pygame.time.delay(4000)

        break

    # -------------------------------------------------
    # MOVIMIENTO
    # -------------------------------------------------
    mov1 = math.sin(time.time()*3)*5
    mov2 = math.sin(time.time()*3+1)*5

    # JUGADOR
    screen.blit(
        jugador.imagen,
        (30,380 + mov1)
    )

    # ENEMIGO
    screen.blit(
        enemigo.imagen,
        (930,80 + mov2)
    )

    # -------------------------------------------------
    # PANELES
    # -------------------------------------------------
    dibujar_panel(
        20,
        20,
        jugador
    )

    dibujar_panel(
        900,
        20,
        enemigo
    )

    # -------------------------------------------------
    # PERGAMINO
    # -------------------------------------------------
    screen.blit(
        pergamino,
        (220,180)
    )

    texto_borde(
        "ORDENA LOS EVENTOS",
        fuente_grande,
        MARRON,
        NEGRO,
        350,
        120
    )

    # -------------------------------------------------
    # RELOJ
    # -------------------------------------------------
    screen.blit(
        reloj,
        (530,20)
    )

    tiempo_restante = max(
        0,
        int(
            TIEMPO_LIMITE -
            (time.time() - inicio_tiempo)
        )
    )

    texto_borde(
        str(tiempo_restante),
        fuente_grande,
        ROJO,
        NEGRO,
        570,
        130
    )

    # -------------------------------------------------
    # MENSAJE
    # -------------------------------------------------
    texto_borde(
        mensaje,
        fuente,
        BLANCO,
        NEGRO,
        370,
        620
    )

    # -------------------------------------------------
    # EVENTOS
    # -------------------------------------------------
    for item in rects:

        pygame.draw.rect(
            screen,
            (210,180,120),
            item["rect"],
            border_radius=12
        )

        pygame.draw.rect(
            screen,
            NEGRO,
            item["rect"],
            3,
            border_radius=12
        )

        texto_borde(
            item["texto"],
            fuente,
            NEGRO,
            BLANCO,
            item["rect"].x + 15,
            item["rect"].y + 15
        )

    # -------------------------------------------------
    # PARTICULAS
    # -------------------------------------------------
    actualizar_particulas()

    # -------------------------------------------------
    # TIEMPO TERMINADO
    # -------------------------------------------------
    if tiempo_restante <= 0:

        # Ordenar visualmente
        rects.sort(
            key=lambda r:r["rect"].y
        )

        for i,item in enumerate(rects):

            item["rect"].y = (
                220 + i*90
            )

        # VERIFICAR SI ESTA BIEN
        if verificar():

            daño = random.randint(20,35)

            enemigo.vida -= daño

            mensaje = (
                f"¡Correcto! Hiciste {daño}"
            )

            crear_particulas(
                980,
                170
            )

            if enemigo.vida <= 0:

                mensaje = (
                    f"{enemigo.nombre} fue derrotado"
                )

        else:

            daño = random.randint(8,15)

            jugador.vida -= daño

            mensaje = (
                f"Orden incorrecto. Recibiste {daño}"
            )

            crear_particulas(
                130,
                470
            )

        pygame.display.update()

        pygame.time.delay(1500)

        nueva_ronda()

    pygame.display.update()

    # -------------------------------------------------
    # INPUTS
    # -------------------------------------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        # -------------------------------------------------
        # CLICK
        # -------------------------------------------------
        if event.type == pygame.MOUSEBUTTONDOWN:

            mx,my = pygame.mouse.get_pos()

            for item in rects:

                if item["rect"].collidepoint(mx,my):

                    dragging = item

                    offset_y = (
                        my - item["rect"].y
                    )

        # -------------------------------------------------
        # SOLTAR
        # -------------------------------------------------
        if event.type == pygame.MOUSEBUTTONUP:

            dragging = None
        # -------------------------------------------------
        # MOVER
        # -------------------------------------------------
        if event.type == pygame.MOUSEMOTION:

            if dragging:

                dragging["rect"].y = (
                    event.pos[1] - offset_y
                )

    clock.tick(60)

pygame.quit()
sys.exit()