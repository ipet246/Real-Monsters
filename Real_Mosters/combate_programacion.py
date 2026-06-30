import pygame
import random
import sys
import time
import math
pygame.mixer.init()

# ---------------------------
# CONFIG
# ---------------------------
ANCHO = 800
ALTO = 600

def iniciar_combate(screen):
    fuente = pygame.font.Font("PokemonGb-Raeo.ttf", 12)
    fuente_grande = pygame.font.Font("PokemonGb-Raeo.ttf", 14)

    BLANCO = (255,255,255)
    NEGRO = (0,0,0)
    VERDE = (0,220,0)
    ROJO = (220,0,0)

    TIEMPO_LIMITE = 15
    sonido_golpe = pygame.mixer.Sound("sonidos.musica/golpe.mp3")
    sonido_menu = pygame.mixer.Sound("sonidos.musica/opcion.mp3")
    sonido_dado = pygame.mixer.Sound("sonidos.musica/dado.mp3")
    sonido_error = pygame.mixer.Sound("sonidos.musica/error.mp3")
    canal_victoria = pygame.mixer.Sound("sonidos.musica/victoria.mp3")
    sonido_escudo = pygame.mixer.Sound("sonidos.musica/escudo.mp3")

    sonido_golpe.set_volume(0.2)
    sonido_menu.set_volume(0.3)
    sonido_dado.set_volume(0.5)
    sonido_error.set_volume(0.2)
    canal_victoria.set_volume(0.5)
    sonido_escudo.set_volume(0.5)
    sonido_golpe.play(maxtime=2000)

    ultimo_dado = None
    mensaje_turno = ""

    sacudir_enemigo = False
    tiempo_sacudida = 0

    sacudir_jugador = False
    tiempo_sacudida_jugador = 0

    # ---------------------------
    # FONDO
    # ---------------------------
    fondo = pygame.image.load("imagenes/fondoprogramacion.jfif")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    # ---------------------------
    # ENTRENADOR RIVAL
    # ---------------------------
    entrenador_rival = pygame.image.load(
        "imagenes/entrenador_rival.png"
    )

    entrenador_rival = pygame.transform.scale(
        entrenador_rival,
        (180,180)
    )

    # ---------------------------
    # DADOS
    # ---------------------------
    dados = []

    for i in range(1,13):

        img = pygame.image.load(
            f"imagenes/dado/dado{i}.png"
        )

        img = pygame.transform.scale(
            img,
            (100,100)
        )

        dados.append(img)

    # ---------------------------
    # PARTICULAS
    # ---------------------------
    particulas = []

    # ---------------------------
    # TEXTO BORDE
    # ---------------------------
    def texto_borde(texto, fuente, color, borde, x, y):

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

        screen.blit(base, (x,y))

    # ---------------------------
    # MONSTRUO
    # ---------------------------
    class Monstruo:

        def __init__(self, nombre, vida, imagen):

            self.nombre = nombre
            self.vida = vida
            self.vida_visual = vida
            self.max_vida = vida

            self.imagen = pygame.image.load(imagen)

            self.imagen = pygame.transform.scale(
                self.imagen,
                (200,160)
            )

        def vivo(self):

            return self.vida > 0

    # ---------------------------
    # PREGUNTAS
    # ---------------------------
    # ---------------------------
    # PREGUNTAS POR MONSTRUO
    # ---------------------------

    preguntas_por_monstruo = {

        "brocca": [
            (
                "Que funcion muestra texto en pantalla?",
                ["print()", "input()", "while", "pygame"],
                "print()"
            ),
            (
                "Completa: print( ? ) para mostrar Hola",
                ["\"Hola\"", "Hola", "print", "texto"],
                "\"Hola\""
            ),
            (
                "Que hace esta linea: nombre = \"Ana\"?",
                ["Guarda Ana en una variable", "Muestra Ana", "Borra Ana", "Cierra Python"],
                "Guarda Ana en una variable"
            ),
            (
                "Si x = 5, que muestra print(x)?",
                ["5", "x", "print", "Error"],
                "5"
            ),
            (
                "Que simbolo se usa para asignar un valor?",
                ["=", "==", "+", "()"],
                "="
            ),
            (
                "En Python, un texto se escribe entre...",
                ["comillas", "flechas", "puntos", "llaves"],
                "comillas"
            ),
            (
                "Que muestra print(3 + 2)?",
                ["5", "32", "3 + 2", "Error"],
                "5"
            ),
            (
                "Completa: edad = 15. Para mostrarla uso...",
                ["print(edad)", "print(\"edad\")", "edad(print)", "mostrar edad"],
                "print(edad)"
            ),
            (
                "Que hace input()?",
                ["Pide datos al usuario", "Muestra texto", "Crea una imagen", "Borra una variable"],
                "Pide datos al usuario"
            ),
            (
                "Como se llama un dato guardado con un nombre?",
                ["Variable", "Pantalla", "Sonido", "Mapa"],
                "Variable"
            )
        ],

        "cufre": [
            (
                "Que significa == en una condicion?",
                ["Comparar igualdad", "Asignar valor", "Sumar", "Dividir"],
                "Comparar igualdad"
            ),
            (
                "Cual sirve para tomar una decision?",
                ["if", "print", "color", "imagen"],
                "if"
            ),
            (
                "Completa: if edad >= 18:",
                ["es una condicion", "muestra texto", "borra edad", "crea musica"],
                "es una condicion"
            ),
            (
                "Que palabra sirve para repetir acciones?",
                ["while", "print", "image", "font"],
                "while"
            ),
            (
                "Completa: vidas = vidas - 1 sirve para...",
                ["Restar una vida", "Sumar una vida", "Mostrar vidas", "Crear vidas"],
                "Restar una vida"
            ),
            (
                "Cual es correcto para comparar una clave?",
                ["if clave == \"1234\":", "if clave = \"1234\":", "clave if 1234", "print clave"],
                "if clave == \"1234\":"
            ),
            (
                "Que hace una variable?",
                ["Guarda un dato", "Solo dibuja", "Solo reproduce sonido", "Apaga el juego"],
                "Guarda un dato"
            ),
            (
                "Completa: puntos = puntos + 10 sirve para...",
                ["Sumar puntos", "Borrar puntos", "Crear texto", "Cerrar ventana"],
                "Sumar puntos"
            ),
            (
                "Que estructura usa pygame para detectar teclas o cerrar ventana?",
                ["eventos", "colores", "imagenes", "fuentes"],
                "eventos"
            ),
            (
                "Que pasa si una condicion if es verdadera?",
                ["Se ejecuta su bloque", "Siempre da error", "Se cierra Python", "No pasa nada"],
                "Se ejecuta su bloque"
            )
        ]
    }

    # Guarda las preguntas que todavia no salieron.
    # Asi no se repiten durante el combate.
    preguntas_disponibles = {}

    # ---------------------------
    # OBTENER PREGUNTA
    # ---------------------------
    def obtener_pregunta(monstruo_nombre):

        if monstruo_nombre not in preguntas_disponibles or len(preguntas_disponibles[monstruo_nombre]) == 0:
            preguntas_disponibles[monstruo_nombre] = preguntas_por_monstruo[monstruo_nombre].copy()
            random.shuffle(preguntas_disponibles[monstruo_nombre])

        return preguntas_disponibles[monstruo_nombre].pop()

    # ---------------------------
    # PARTICULAS
    # ---------------------------
    def crear_particulas(x, y):

        for i in range(20):

            particulas.append({

                "x": x,
                "y": y,

                "vx": random.randint(-5,5),
                "vy": random.randint(-5,5),

                "vida": random.randint(20,40)
            })

    def actualizar_particulas():

        for p in particulas[:]:

            p["x"] += p["vx"]
            p["y"] += p["vy"]

            p["vida"] -= 1

            pygame.draw.circle(
                screen,
                (255,255,0),
                (int(p["x"]), int(p["y"])),
                4
            )

            if p["vida"] <= 0:

                particulas.remove(p)

    # ---------------------------
    # FLASH
    # ---------------------------
    def flash_rojo():

        flash = pygame.Surface(
            (ANCHO,ALTO)
        )

        flash.set_alpha(80)

        flash.fill((255,0,0))

        screen.blit(flash, (0,0))

    # ---------------------------
    # ENTRADA MONSTRUOS
    # ---------------------------
    def entrada_monstruos(j, e):

        inicio = time.time()

        duracion = 1.2

        while True:

            tiempo = time.time() - inicio

            progreso = min(tiempo / duracion, 1)

            screen.blit(fondo, (0,0))

            suavizado = 1 - (1 - progreso) ** 3
            # ENTRENADOR RIVAL CON MOVIMIENTO
            rival_x = 900 - (900 - 600) * suavizado

            screen.blit(
                entrenador_rival,
                (rival_x,100)
            )

            

            jugador_x = -200 + (70 + 200) * suavizado
            enemigo_x = 900 - (900 - 500) * suavizado

            jugador_y = 200
            enemigo_y = 120

            screen.blit(
                j.imagen,
                (jugador_x, jugador_y)
            )

            screen.blit(
                e.imagen,
                (enemigo_x, enemigo_y)
            )

            dibujar_panel_monstruo(
                500,
                30,
                e
            )

            dibujar_panel_monstruo(
                30,
                330,
                j
            )

            texto_borde(
                "¡UN NUEVO MONSTRUO APARECE!",
                fuente,
                BLANCO,
                NEGRO,
                180,
                40
            )

            pygame.display.update()

            if progreso >= 1:
                break

            pygame.time.delay(16)

    # ---------------------------
    # PANEL MONSTRUO
    # ---------------------------
    def dibujar_panel_monstruo(
        x,
        y,
        monstruo,
        activo=False
    ):

        color_borde = (
            (0,255,0)
            if activo else NEGRO
        )

        sombra = pygame.Surface(
            (250,80),
            pygame.SRCALPHA
        )

        sombra.fill((0,0,0,80))

        screen.blit(
            sombra,
            (x+5,y+5)
        )

        pygame.draw.rect(
            screen,
            BLANCO,
            (x,y,250,80),
            border_radius=15
        )

        pygame.draw.rect(
            screen,
            color_borde,
            (x,y,250,80),
            width=3,
            border_radius=15
        )

        texto_borde(
            monstruo.nombre,
            fuente,
            NEGRO,
            BLANCO,
            x+10,
            y+10
        )

        if monstruo.vida_visual > monstruo.vida:

            monstruo.vida_visual -= 0.2

        vida_ratio = max(
            monstruo.vida_visual / monstruo.max_vida,
            0
        )

        pygame.draw.rect(
            screen,
            ROJO,
            (x+10,y+40,200,15),
            border_radius=10
        )

        pygame.draw.rect(
            screen,
            VERDE,
            (x+10,y+40,200*vida_ratio,15),
            border_radius=10
        )

        texto_borde(
            f"{int(monstruo.vida)}/{monstruo.max_vida}",
            fuente,
            NEGRO,
            BLANCO,
            x+150,
            y+58
        )

    # ---------------------------
    # PANEL DADO
    # ---------------------------
    def dibujar_panel_dado(valor):

        pygame.draw.rect(
            screen,
            BLANCO,
            (290,290,220,140),
            border_radius=15
        )

        pygame.draw.rect(
            screen,
            NEGRO,
            (290,290,220,140),
            3,
            border_radius=15
        )

        texto_borde(
            "DADO",
            fuente_grande,
            NEGRO,
            BLANCO,
            335,
            305
        )

        if valor:

            screen.blit(
                dados[valor-1],
                (345,335)
            )

    # ---------------------------
    # SACUDIDAS
    # ---------------------------
    def activar_sacudida():

        global sacudir_enemigo
        global tiempo_sacudida

        sacudir_enemigo = True
        tiempo_sacudida = time.time()

    def activar_sacudida_jugador():

        global sacudir_jugador
        global tiempo_sacudida_jugador

        sacudir_jugador = True
        tiempo_sacudida_jugador = time.time()

    # ---------------------------
    # ANIMAR DADO
    # ---------------------------
    # ---------------------------
    # ANIMAR DADO
    # ---------------------------
    def animar_dado():

        global ultimo_dado

        j = elegir(jugador)
        e = elegir(enemigo)

        centro_x = 400
        centro_y = 230

        inicio = time.time()

        numero_actual = random.randint(1,12)

        # duración MÁS CORTA
        while time.time() - inicio < 1:

            screen.blit(fondo, (0,0))

            # ENTRENADOR RIVAL
            screen.blit(
                entrenador_rival,
                (600,100)
            )

            mov_e = math.sin(time.time()*3)*5
            mov_j = math.sin(time.time()*3+1)*5

            # ENEMIGO
            screen.blit(
                e.imagen,
                (500,120 + mov_e)
            )

            # JUGADOR
            screen.blit(
                j.imagen,
                (70,200 + mov_j)
            )

            # PANELES
            dibujar_panel_monstruo(
                500,
                30,
                e
            )

            dibujar_panel_monstruo(
                30,
                330,
                j
            )

            # CAMBIA MÁS LENTO
            if random.randint(1,4) == 1:

                numero_actual = random.randint(1,12)

            # EFECTO ZOOM
            tamaño = 120 + math.sin(time.time()*10)*8

            img = pygame.transform.scale(
                dados[numero_actual-1],
                (int(tamaño), int(tamaño))
            )

            rect = img.get_rect(
                center=(centro_x, centro_y)
            )

            screen.blit(img, rect)

            texto_borde(
                "Girando...",
                fuente_grande,
                BLANCO,
                NEGRO,
                290,
                100
            )

            pygame.display.update()

            # MÁS FLUIDO
            pygame.time.delay(35)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

        # RESULTADO FINAL
        ultimo_dado = random.randint(1,12)

        inicio_resultado = time.time()

        while time.time() - inicio_resultado < 1:

            screen.blit(fondo, (0,0))

            # ENTRENADOR RIVAL
            screen.blit(
                entrenador_rival,
                (600,100)
            )

            mov_e = math.sin(time.time()*3)*5
            mov_j = math.sin(time.time()*3+1)*5

            screen.blit(
                e.imagen,
                (500,120 + mov_e)
            )

            screen.blit(
                j.imagen,
                (70,200 + mov_j)
            )

            dibujar_panel_monstruo(
                500,
                30,
                e
            )

            dibujar_panel_monstruo(
                30,
                330,
                j
            )

            # DADO MÁS GRANDE
            tamaño = 140 + math.sin(time.time()*8)*5

            img = pygame.transform.scale(
                dados[ultimo_dado-1],
                (int(tamaño), int(tamaño))
            )

            rect = img.get_rect(
                center=(400,230)
            )

            screen.blit(img, rect)

            texto_borde(
                f"¡Salió {ultimo_dado}!",
                fuente_grande,
                BLANCO,
                NEGRO,
                280,
                100
            )

            pygame.display.update()

            pygame.time.delay(16)

        return ultimo_dado

    # ---------------------------
    # PREGUNTAR
    # ---------------------------
    def preguntar():

        pregunta, opciones, correcta = obtener_pregunta(e.nombre)

        # Mezcla las respuestas para que no siempre esten en el mismo lugar
        opciones_mezcladas = opciones.copy()
        random.shuffle(opciones_mezcladas)

        seleccion = 0

        inicio = time.time()

        while True:

            screen.blit(fondo, (0,0))

            # ENTRENADOR RIVAL
            screen.blit(
                entrenador_rival,
                (600,100)
            )

            mov_e = math.sin(time.time()*3)*5
            mov_j = math.sin(time.time()*3+1)*5

            enemigo_x = 500
            enemigo_y = 120

            screen.blit(
                e.imagen,
                (
                    enemigo_x,
                    enemigo_y + mov_e
                )
            )

            jugador_x = 70
            jugador_y = 200

            screen.blit(
                j.imagen,
                (
                    jugador_x,
                    jugador_y + mov_j
                )
            )

            dibujar_panel_monstruo(
                500,
                30,
                e
            )

            dibujar_panel_monstruo(
                30,
                330,
                j
            )

            pygame.draw.rect(
                screen,
                BLANCO,
                (40,430,720,140),
                border_radius=20
            )

            pygame.draw.rect(
                screen,
                NEGRO,
                (40,430,720,140),
                4,
                border_radius=20
            )

            texto_borde(
                pregunta,
                fuente_grande,
                NEGRO,
                BLANCO,
                60,
                440
            )

            letras = ["A", "B", "C", "D"]

            for i, op in enumerate(opciones_mezcladas):

                color = (
                    (0,100,255)
                    if i == seleccion
                    else NEGRO
                )

                texto_borde(
                    letras[i] + ") " + op,
                    fuente,
                    color,
                    BLANCO,
                    60,
                    470 + i*26
                )

            tiempo_restante = int(
                TIEMPO_LIMITE - (time.time() - inicio)
            )

            texto_borde(
                f"Tiempo: {tiempo_restante}",
                fuente,
                ROJO,
                BLANCO,
                620,
                545
            )

            pygame.display.update()

            if tiempo_restante <= 0:

                return False

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:
                        sonido_menu.play()
                        seleccion = (
                            seleccion - 1
                        ) % 4

                    elif event.key == pygame.K_DOWN:
                        sonido_menu.play()

                        seleccion = (
                            seleccion + 1
                        ) % 4

                    elif event.key == pygame.K_RETURN:

                        return opciones_mezcladas[seleccion] == correcta

    # ---------------------------
    # MONSTRUOS
    # ---------------------------
    jugador = [

        Monstruo(
            "nerdito",
            40,
            "imagenes/nerditocombate.png"
        )
    ]

    enemigo = [

        Monstruo(
            "brocca",
            20,
            "imagenes/brocca.png"
        ),

        Monstruo(
            "cufre",
            25,
            "imagenes/cufre.png"
        )
    ]

    def elegir(lista):

        vivos = [
            m for m in lista
            if m.vivo()
        ]

        return vivos[0] if vivos else None

    # Ahora no hay sistema de turnos.
    # Cada vez que apretas ESPACIO respondes una pregunta:
    # - Si aciertas, golpeas al enemigo.
    # - Si fallas, el enemigo te golpea automaticamente.

    # ---------------------------
    # TRANSICIÓN INICIAL
    # ---------------------------
    j = elegir(jugador)
    e = elegir(enemigo)

    entrada_monstruos(j, e)

    # ===========================
    # LOOP PRINCIPAL
    # ===========================
    while True:

        screen.blit(fondo, (0,0))

        # ENTRENADOR
        screen.blit(
            entrenador_rival,
            (600,100)
        )

        j = elegir(jugador)
        e = elegir(enemigo)

        if j is None:
            texto_borde("PERDISTE", fuente_grande, ROJO, NEGRO, 300, 200)
            pygame.display.update()
            pygame.time.delay(3000)
            pygame.mixer.music.stop
            return "lab_programacion"

        if e is None:
            canal_victoria.play()
            texto_borde("GANASTE", fuente_grande, VERDE, NEGRO, 300, 200)
            pygame.display.update()
            pygame.mixer.music.stop()
            pygame.time.delay(3000)
            canal_victoria.stop()
            return "lab_programacion"

        if not j:

            texto_borde(
                "PERDISTE",
                fuente_grande,
                ROJO,
                NEGRO,
                300,
                200
            )

            pygame.display.update()
            pygame.time.delay(3000)  
            return "lab_programacion"
            
        



        if not e:
            canal_victoria.play()
            texto_borde(
                "GANASTE",
                fuente_grande,
                VERDE,
                NEGRO,
                300,
                200
            )

            pygame.display.update()
            pygame.time.delay(3000)
            pygame.mixer.music.stop()
            canal_victoria.stop()
            return "lab_programacion"

        mov_e = math.sin(time.time()*3)*5
        mov_j = math.sin(time.time()*3+1)*5

        enemigo_x = 500
        enemigo_y = 120

        offset = (
            random.randint(-10,10)
            if sacudir_enemigo and
            time.time()-tiempo_sacudida < 0.5
            else 0
        )

        screen.blit(
            e.imagen,
            (
                enemigo_x + offset,
                enemigo_y + mov_e
            )
        )

        jugador_x = 70
        jugador_y = 200

        offset_j = (
            random.randint(-10,10)
            if sacudir_jugador and
            time.time()-tiempo_sacudida_jugador < 0.5
            else 0
        )

        screen.blit(
            j.imagen,
            (
                jugador_x + offset_j,
                jugador_y + mov_j
            )
        )

        dibujar_panel_monstruo(
            500,
            30,
            e,
            False
        )

        dibujar_panel_monstruo(
            30,
            330,
            j,
            True
        )

        dibujar_panel_dado(
            ultimo_dado
        )

        actualizar_particulas()

        # TEXTOS
        texto_borde(
            "COMPLETA EL CODIGO",
            fuente_grande,
            BLANCO,
            NEGRO,
            120,
            20
        )

        if mensaje_turno:

            texto_borde(
                mensaje_turno,
                fuente_grande,
                BLANCO,
                NEGRO,
                250,
                240
            )

        texto_borde(
            "ESPACIO = responder",
            fuente,
            BLANCO,
            NEGRO,
            270,
            460
        )

        pygame.display.update()

        # EVENTOS
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if (
                event.type == pygame.KEYDOWN and
                event.key == pygame.K_SPACE
            ):
                sonido_dado.play()
                dado = animar_dado()

                acierta = preguntar()

                if acierta:
                    sonido_golpe.play()
                    e.vida -= dado

                    activar_sacudida()

                    crear_particulas(
                        580,
                        180
                    )

                    flash_rojo()

                    mensaje_turno = (
                        f"Golpeaste por {dado}"
                    )

                    if e.vida <= 0:

                        mensaje_turno = f"{e.nombre} fue derrotado"

                        # ESPERA PARA VER EL GOLPE FINAL
                        tiempo_derrota = time.time()

                        while time.time() - tiempo_derrota < 1.2:

                            screen.blit(fondo, (0,0))

                            # ENTRENADOR RIVAL
                            screen.blit(
                                entrenador_rival,
                                (600,100)
                            )

                            mov_j = math.sin(time.time()*3)*5

                            # JUGADOR
                            screen.blit(
                                j.imagen,
                                (70,200 + mov_j)
                            )

                            dibujar_panel_monstruo(
                                30,
                                330,
                                j
                            )

                            # ENEMIGO PARPADEA
                            if int((time.time() - tiempo_derrota) * 10) % 2 == 0:

                                screen.blit(
                                    e.imagen,
                                    (500,120)
                                )

                            dibujar_panel_monstruo(
                                500,
                                30,
                                e
                            )

                            texto_borde(
                                f"{e.nombre} fue derrotado",
                                fuente_grande,
                                BLANCO,
                                NEGRO,
                                170,
                                220
                            )

                            pygame.display.update()

                            pygame.time.delay(16)

                        # TRANSICIÓN DESAPARECER
                        inicio_muerte = time.time()

                        while time.time() - inicio_muerte < 1:

                            screen.blit(fondo, (0,0))

                            # ENTRENADOR RIVAL
                            screen.blit(
                                entrenador_rival,
                                (600,100)
                            )

                            mov_j = math.sin(time.time()*3)*5

                            screen.blit(
                                j.imagen,
                                (70,200 + mov_j)
                            )

                            dibujar_panel_monstruo(
                                30,
                                330,
                                j
                            )

                            progreso = (
                                time.time() - inicio_muerte
                            ) / 1

                            alpha = max(
                                255 - int(progreso * 255),
                                0
                            )

                            tamaño = max(
                                int(120 - progreso * 40),
                                20
                            )

                            img = pygame.transform.scale(
                                e.imagen.copy(),
                                (tamaño,tamaño)
                            )

                            img.set_alpha(alpha)

                            screen.blit(
                                img,
                                (
                                    500 + (120 - tamaño)//2,
                                    120 + (120 - tamaño)//2
                                )
                            )

                            texto_borde(
                                f"{e.nombre} fue derrotado",
                                fuente_grande,
                                BLANCO,
                                NEGRO,
                                170,
                                220
                            )

                            pygame.display.update()

                            pygame.time.delay(16)

                        enemigo.remove(e)

                        vivos = [
                            m for m in enemigo
                            if m.vivo()
                        ]

                        if vivos:
                            entrada_monstruos(
                                j,
                                vivos[0]
                            )

                else:
                    sonido_error.play()
                    j.vida -= dado

                    activar_sacudida_jugador()

                    crear_particulas(
                        150,
                        250
                    )

                    flash_rojo()

                    mensaje_turno = (
                        f"Fallaste. Te hicieron {dado}"
                    )

                    if j.vida <= 0:

                        vivos = [
                            m for m in jugador
                            if m.vivo()
                        ]

                        if vivos:

                            entrada_monstruos(
                                vivos[0],
                                e
                            )