import pygame
import random
import string
import sys
import time
import math

ANCHO = 800
ALTO = 600


def iniciar_combate(screen):
    pygame.font.init()

    fuente = pygame.font.Font("PokemonGb-Raeo.ttf", 12)
    fuente_grande = pygame.font.Font("PokemonGb-Raeo.ttf", 14)

    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    GRIS = (180, 180, 180)
    VERDE = (0, 180, 0)
    ROJO = (200, 0, 0)
    AZUL = (0, 100, 220)
    AMARILLO = (255, 230, 120)

    FILAS = 10
    COLUMNAS = 10
    TAM_CELDA = 26

    sopa_x = 55
    sopa_y = 55

    seleccion_inicio = None
    mensaje = "Selecciona una palabra"
    palabras_encontradas = []
    posiciones_encontradas = []

    fondo = pygame.image.load("imagenes/fondo_geo.png")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    def texto_borde(texto, fuente_usada, color, borde, x, y):
        for dx in [-2, 0, 2]:
            for dy in [-2, 0, 2]:
                if dx != 0 or dy != 0:
                    sombra = fuente_usada.render(texto, True, borde)
                    screen.blit(sombra, (x + dx, y + dy))

        base = fuente_usada.render(texto, True, color)
        screen.blit(base, (x, y))

    class Monstruo:
        def __init__(self, nombre, vida, imagen, categoria, palabras):
            self.nombre = nombre
            self.vida = vida
            self.vida_visual = vida
            self.max_vida = vida
            self.categoria = categoria
            self.palabras = palabras

            self.imagen = pygame.image.load(imagen)
            self.imagen = pygame.transform.scale(self.imagen, (170, 140))

        def vivo(self):
            return self.vida > 0

    jugador = Monstruo(
        "nerdito",
        40,
        "imagenes/nerditocombate.png",
        "",
        []
    )

    enemigos = [
        Monstruo(
            "sinonix",
            30,
            "imagenes/paisor.png",
            "Busca sinonimos de FELIZ",
            ["CONTENTO", "ALEGRE", "DICHOSO"]
        ),
        Monstruo(
            "antonix",
            30,
            "imagenes/oceanix.png",
            "Busca antonimos de ALTO",
            ["BAJO", "CHICO", "PEQUENO"]
        )
    ]

    enemigo_actual = 0
    enemigo = enemigos[enemigo_actual]

    def crear_sopa(palabras):
        grilla = [["" for _ in range(COLUMNAS)] for _ in range(FILAS)]

        for palabra in palabras:
            colocada = False
            intentos = 0

            while not colocada and intentos < 200:
                intentos += 1

                direccion = random.choice(["H", "V"])
                fila = random.randint(0, FILAS - 1)
                col = random.randint(0, COLUMNAS - 1)

                if direccion == "H" and col + len(palabra) <= COLUMNAS:
                    libre = True

                    for i in range(len(palabra)):
                        if grilla[fila][col + i] != "":
                            libre = False

                    if libre:
                        for i in range(len(palabra)):
                            grilla[fila][col + i] = palabra[i]

                        colocada = True

                elif direccion == "V" and fila + len(palabra) <= FILAS:
                    libre = True

                    for i in range(len(palabra)):
                        if grilla[fila + i][col] != "":
                            libre = False

                    if libre:
                        for i in range(len(palabra)):
                            grilla[fila + i][col] = palabra[i]

                        colocada = True

        for f in range(FILAS):
            for c in range(COLUMNAS):
                if grilla[f][c] == "":
                    grilla[f][c] = random.choice(string.ascii_uppercase)

        return grilla

    def obtener_celda_mouse(mouse_x, mouse_y):
        col = (mouse_x - sopa_x) // TAM_CELDA
        fila = (mouse_y - sopa_y) // TAM_CELDA

        if 0 <= fila < FILAS and 0 <= col < COLUMNAS:
            return fila, col

        return None

    def obtener_palabra_seleccionada(grilla, inicio, fin):
        fila1, col1 = inicio
        fila2, col2 = fin

        palabra = ""

        if fila1 == fila2:
            if col1 <= col2:
                for c in range(col1, col2 + 1):
                    palabra += grilla[fila1][c]
            else:
                for c in range(col1, col2 - 1, -1):
                    palabra += grilla[fila1][c]

        elif col1 == col2:
            if fila1 <= fila2:
                for f in range(fila1, fila2 + 1):
                    palabra += grilla[f][col1]
            else:
                for f in range(fila1, fila2 - 1, -1):
                    palabra += grilla[f][col1]

        else:
            return ""

        return palabra

    def obtener_posiciones_seleccionadas(inicio, fin):
        fila1, col1 = inicio
        fila2, col2 = fin
        posiciones = []

        if fila1 == fila2:
            if col1 <= col2:
                for c in range(col1, col2 + 1):
                    posiciones.append((fila1, c))
            else:
                for c in range(col1, col2 - 1, -1):
                    posiciones.append((fila1, c))

        elif col1 == col2:
            if fila1 <= fila2:
                for f in range(fila1, fila2 + 1):
                    posiciones.append((f, col1))
            else:
                for f in range(fila1, fila2 - 1, -1):
                    posiciones.append((f, col1))

        return posiciones

    def dibujar_panel_monstruo(x, y, monstruo):
        pygame.draw.rect(screen, BLANCO, (x, y, 250, 80), border_radius=15)
        pygame.draw.rect(screen, NEGRO, (x, y, 250, 80), 3, border_radius=15)

        texto_borde(monstruo.nombre, fuente, NEGRO, BLANCO, x + 10, y + 10)

        if monstruo.vida_visual > monstruo.vida:
            monstruo.vida_visual -= 0.3

        vida_ratio = monstruo.vida_visual / monstruo.max_vida
        vida_ratio = max(vida_ratio, 0)

        pygame.draw.rect(screen, ROJO, (x + 10, y + 42, 200, 14), border_radius=10)
        pygame.draw.rect(screen, VERDE, (x + 10, y + 42, 200 * vida_ratio, 14), border_radius=10)

        texto_borde(
            f"{int(monstruo.vida)}/{monstruo.max_vida}",
            fuente,
            NEGRO,
            BLANCO,
            x + 140,
            y + 60
        )

    sopa = crear_sopa(enemigo.palabras)
    reloj = pygame.time.Clock()

    while True:
        screen.blit(fondo, (0, 0))

        mov_e = math.sin(time.time() * 3) * 5
        mov_j = math.sin(time.time() * 3 + 1) * 5

        screen.blit(jugador.imagen, (70, 315 + mov_j))
        screen.blit(enemigo.imagen, (560, 170 + mov_e))

        dibujar_panel_monstruo(40, 365, jugador)
        dibujar_panel_monstruo(500, 40, enemigo)

        pygame.draw.rect(screen, BLANCO, (40, 35, 290, 290), border_radius=15)
        pygame.draw.rect(screen, NEGRO, (40, 35, 290, 290), 4, border_radius=15)

        for f in range(FILAS):
            for c in range(COLUMNAS):
                rect = pygame.Rect(
                    sopa_x + c * TAM_CELDA,
                    sopa_y + f * TAM_CELDA,
                    TAM_CELDA,
                    TAM_CELDA
                )

                if (f, c) in posiciones_encontradas:
                    pygame.draw.rect(screen, AMARILLO, rect)

                pygame.draw.rect(screen, GRIS, rect, 1)

                if seleccion_inicio == (f, c):
                    pygame.draw.rect(screen, AZUL, rect, 3)

                letra = fuente.render(sopa[f][c], True, NEGRO)
                screen.blit(letra, (rect.x + 7, rect.y + 6))

        pygame.draw.rect(screen, BLANCO, (40, 450, 720, 120), border_radius=20)
        pygame.draw.rect(screen, NEGRO, (40, 450, 720, 120), 4, border_radius=20)

        texto_borde(enemigo.categoria, fuente_grande, NEGRO, BLANCO, 60, 462)
        texto_borde(mensaje, fuente, NEGRO, BLANCO, 60, 492)

        texto_borde(
            f"Encontradas: {len(palabras_encontradas)}/{len(enemigo.palabras)}",
            fuente,
            NEGRO,
            BLANCO,
            560,
            492
        )

        x_palabra = 60
        y_palabra = 525

        for palabra in enemigo.palabras:
            if palabra in palabras_encontradas:
                color = VERDE
            else:
                color = NEGRO

            texto_borde(palabra, fuente, color, BLANCO, x_palabra, y_palabra)
            x_palabra += 150

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                celda = obtener_celda_mouse(mouse_x, mouse_y)

                if celda is not None:
                    if seleccion_inicio is None:
                        seleccion_inicio = celda
                        mensaje = "Ahora toca la ultima letra"

                    else:
                        seleccion_fin = celda

                        palabra = obtener_palabra_seleccionada(
                            sopa,
                            seleccion_inicio,
                            seleccion_fin
                        )

                        palabra_invertida = palabra[::-1]

                        if palabra in enemigo.palabras and palabra not in palabras_encontradas:
                            palabras_encontradas.append(palabra)

                            posiciones = obtener_posiciones_seleccionadas(
                                seleccion_inicio,
                                seleccion_fin
                            )
                            posiciones_encontradas.extend(posiciones)

                            enemigo.vida -= 10
                            mensaje = "Correcto, atacaste"

                        elif palabra_invertida in enemigo.palabras and palabra_invertida not in palabras_encontradas:
                            palabras_encontradas.append(palabra_invertida)

                            posiciones = obtener_posiciones_seleccionadas(
                                seleccion_inicio,
                                seleccion_fin
                            )
                            posiciones_encontradas.extend(posiciones)

                            enemigo.vida -= 10
                            mensaje = "Correcto, atacaste"

                        else:
                            jugador.vida -= 5
                            mensaje = "Fallaste, te atacaron"

                        seleccion_inicio = None

                        if jugador.vida <= 0:
                            texto_borde("PERDISTE", fuente_grande, ROJO, NEGRO, 320, 250)
                            pygame.display.update()
                            pygame.time.delay(2500)
                            return "menu"

                        if len(palabras_encontradas) == len(enemigo.palabras):
                            enemigo.vida = 0
                            enemigo_actual += 1

                            if enemigo_actual >= len(enemigos):
                                texto_borde("GANASTE", fuente_grande, VERDE, NEGRO, 320, 250)
                                pygame.display.update()
                                pygame.time.delay(2500)
                                return "menu"

                            enemigo = enemigos[enemigo_actual]
                            sopa = crear_sopa(enemigo.palabras)
                            palabras_encontradas = []
                            posiciones_encontradas = []
                            seleccion_inicio = None
                            mensaje = "Nuevo monstruo"

        reloj.tick(60)