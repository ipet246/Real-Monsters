from time import time
import pygame
import combate_geo
import combate_mate
import combate_lengua
import combate_logica
import time
from combate_mate import iniciar_combate
pygame.init()
pygame.mixer.init()

# Por ahora el juego solo deja entrar a Matemáticas.
# Cuando agreguen las otras materias, cambien esto o vuelvan a agregar las casas al diccionario.
SOLO_MATEMATICAS = True
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# CARGA DE IMÁGENES #########################################################################################################################################################################################################################
# MENUS
titulo = pygame.image.load("titulo.png").convert_alpha()
titulo = pygame.transform.scale(titulo, (600, 300))

cielo = pygame.image.load("cielo.png").convert()
cielo = pygame.transform.scale(cielo, (800, 600))

liga = pygame.image.load("liga realmonster.png").convert_alpha()
liga = pygame.transform.scale(liga, (850, 500))

protagonista = pygame.image.load("pj principal.png").convert_alpha()
protagonista = pygame.transform.scale(protagonista, (300, 350))

fondo_tutorial = pygame.image.load("fondo_tutorial.jfif").convert()
fondo_tutorial = pygame.transform.scale(fondo_tutorial, (800, 600))

profesor = pygame.image.load("personajes/cufre.png").convert_alpha()
profesor = pygame.transform.scale(profesor, (300, 310))

# PERSONAJES
spritesheet = pygame.image.load("spritesheet.png").convert_alpha()
spritesheet = pygame.transform.scale(spritesheet, (192, 256))

boss_matematicas = pygame.image.load("personajes/pitagoras.png").convert_alpha()

boss_geografia = pygame.image.load("personajes/Mainini.png").convert_alpha()
boss_geografia = pygame.transform.scale(boss_geografia, (950, 700))

boss_lengua = pygame.image.load("personajes/barassi.png").convert_alpha()
boss_lengua = pygame.transform.scale(boss_lengua, (950, 700))

boss_historia = pygame.image.load("personajes/calzoski.png").convert_alpha()
boss_historia = pygame.transform.scale(boss_historia, (950, 700))

boss_programacion = pygame.image.load("personajes/broccacufre.png").convert_alpha()
boss_programacion = pygame.transform.scale(boss_programacion, (950, 700))

# OBJETOS
# matematicas
triangulo = pygame.image.load("objetos/coso triangular.png").convert_alpha()
triangulo = pygame.transform.scale(triangulo, (115, 100))
# geografia
globo = pygame.image.load("objetos/globo.png").convert_alpha()
globo = pygame.transform.scale(globo, (185, 195))
# lengua
mesa1 = pygame.image.load("objetos/mesa1.png").convert_alpha()
mesa1 = pygame.transform.scale(mesa1, (172, 30))
mesa2 = pygame.image.load("objetos/mesa2.png").convert_alpha()
mesa2 = pygame.transform.scale(mesa2, (84, 27))
# historia
mesahis1 = pygame.image.load("objetos/mesahis1.png")
mesahis1 = pygame.transform.scale(mesahis1, (239, 30))
mesahis2 = pygame.image.load("objetos/mesahis2.png").convert_alpha()
mesahis2 = pygame.transform.scale(mesahis2, (113, 40))
mesahis3 = pygame.image.load("objetos/mesahis3.png").convert_alpha()
mesahis3 = pygame.transform.scale(mesahis3, (96, 93))
# MAPAS
mapa_pueblo = pygame.image.load("mapas/pueblo.png").convert()
mapa_pueblo = pygame.transform.scale(mapa_pueblo, (1600, 1200))

mapa_pueblo_2 = pygame.image.load("mapas/pueblo2.png").convert()
mapa_pueblo_2 = pygame.transform.scale(mapa_pueblo_2, (1600, 1200))

mapa_matematicas = pygame.image.load("mapas/lab_mate.png").convert()
mapa_matematicas = pygame.transform.scale(mapa_matematicas, (800, 600))

mapa_geografia = pygame.image.load("mapas/lab_geo.png").convert()
mapa_geografia = pygame.transform.scale(mapa_geografia, (800, 600))

mapa_lengua = pygame.image.load("mapas/lab_len.png").convert()
mapa_lengua = pygame.transform.scale(mapa_lengua, (800, 600))

mapa_historia = pygame.image.load("mapas/lab_his.png").convert()
mapa_historia = pygame.transform.scale(mapa_historia, (800, 600))

mapa_programacion = pygame.image.load("mapas/lab_prog.png").convert()
mapa_programacion = pygame.transform.scale(mapa_programacion, (800, 600))

# CASAS
matematicas = pygame.image.load("casas/casa_mate.png").convert_alpha()
matematicas = pygame.transform.scale(matematicas, (500, 310))

geografia = pygame.image.load("casas/casa_geo.png").convert_alpha()
geografia = pygame.transform.scale(geografia, (700, 350))

lengua = pygame.image.load("casas/casa_lengua.png").convert_alpha()
lengua = pygame.transform.scale(lengua, (250, 220))

historias = pygame.image.load("casas/casa_historia.png").convert_alpha()
historias = pygame.transform.scale(historias, (340, 320))

programacion = pygame.image.load("casas/casa_programacion.png").convert_alpha()
programacion = pygame.transform.scale(programacion, (290, 260))

logica = pygame.image.load("casas/casa_logica.png").convert_alpha()
logica = pygame.transform.scale(logica, (250, 220))

ingles = pygame.image.load("casas/casa_ingles.png").convert_alpha()
ingles = pygame.transform.scale(ingles, (250, 220))

filosofia = pygame.image.load("casas/casa_filosofia.png").convert_alpha()
filosofia = pygame.transform.scale(filosofia, (290, 260))

mate_arriba = pygame.image.load("casas/casa_mate_ arriba.png").convert_alpha()
mate_arriba = pygame.transform.scale(mate_arriba, (500, 150))

geo_arriba = pygame.image.load("casas/casa_geo_arriba.png").convert_alpha()
geo_arriba = pygame.transform.scale(geo_arriba, (700, 170))

lengua_arriba = pygame.image.load("casas/casa_lengua_arriba.png").convert_alpha()
lengua_arriba = pygame.transform.scale(lengua_arriba, (250, 108))

historia_arriba = pygame.image.load("casas/casa_historia_arriba.png").convert_alpha()
historia_arriba = pygame.transform.scale(historia_arriba, (340, 160))

programacion_arriba = pygame.image.load("casas/casa_programacion_arriba.png").convert_alpha()
programacion_arriba = pygame.transform.scale(programacion_arriba, (500, 150))

logica_arriba = pygame.image.load("casas/casa_logica_arriba.png").convert_alpha()
logica_arriba = pygame.transform.scale(logica_arriba, (500, 150))

ingles_arriba = pygame.image.load("casas/casa_ingles_arriba.png").convert_alpha()
ingles_arriba = pygame.transform.scale(ingles_arriba, (250, 108))

filosofia_arriba = pygame.image.load("casas/casa_filosofia_arriba.png").convert_alpha()
filosofia_arriba = pygame.transform.scale(filosofia_arriba, (340, 160))


# EXTRACCIÓN DE FRAMES DE LA SPRITESHEET (ajusta las coordenadas según tu spritesheet)
down_1 = spritesheet.subsurface((0, 0, 64, 64))
down_2 = spritesheet.subsurface((64, 0, 64, 64))
down_3 = spritesheet.subsurface((128, 0, 64, 64))

up_1 = spritesheet.subsurface((0, 66, 64, 62))
up_2 = spritesheet.subsurface((64, 66, 64, 62))
up_3 = spritesheet.subsurface((128, 66, 64, 62))

left_1 = spritesheet.subsurface((0, 194, 64, 62))
left_2 = spritesheet.subsurface((64, 194, 64, 62))
left_3 = spritesheet.subsurface((128, 194, 64, 62))

right_1 = spritesheet.subsurface((0, 134, 62, 62))
right_2 = spritesheet.subsurface((64, 134, 64, 62))
right_3 = spritesheet.subsurface((128, 134, 64, 62))

# ORGANIZACIÓN DE FRAMES EN LISTAS

walk_down = [down_1, down_2, down_3 ]
walk_up = [up_1, up_2, up_3 ]
walk_left = [left_1, left_2, left_3]
walk_right = [right_1, right_2, right_3]
#sonidos #################################################################################################################################################
siguiente = pygame.mixer.Sound("sonidos.musica/next.mp3")
siguiente.set_volume(0.2)
puerta = pygame.mixer.Sound("sonidos.musica/door.mp3")
puerta.set_volume(0.2)
adriana_salte = pygame.mixer.Sound("sonidos.musica/adriana salte.mp3")
adriana_salte.set_volume(0.2)
# VARIABLES DE CONTROL ############################################################################################################################

start_time = pygame.time.get_ticks()
cielo_x = 0
cielo_offset = 0
liga_x = 0 
liga_offset = 0
liga_rect = 0
protagonista_x = WIDTH
current_music = ""
indice_historia = 0
enter_presionado = 0
casa_mate_arriba_x, casa_mate_arriba_y = 278, 94
casa_mate_x, casa_mate_y = 278, 100
casa_geo_arriba_x, casa_geo_arriba_y = 120, 640
casa_geo_x, casa_geo_y = 120, 680
casa_lengua_arriba_x, casa_lengua_arriba_y = 934, 165
casa_lengua_x, casa_lengua_y = 934, 165
casa_historia_arriba_x, casa_historia_arriba_y = 965, 640
casa_historia_x, casa_historia_y = 965, 640
casa_programacion_x, casa_programacion_y = 383, 180
casa_programacion_arriba_x, casa_programacion_arriba_y = 383, 180
casa_ingles_x, casa_ingles_y = 385, 740
casa_ingles_arriba_x, casa_ingles_arriba_y = 385, 740
casa_logica_x, casa_logica_y = 990, 740
casa_logica_arriba_x, casa_logica_arriba_y = 965, 640
casa_filosofia_x, casa_filosofia_y = 944, 165
casa_filosofia_arriba_x, casa_filosofia_arriba_y = 944, 165




# DEFS      #########################################################################################################################################################
def pantalla_controles(screen):
    esperando = True
    titulo_font = pygame.font.Font("PokemonGb-Raeo.ttf", 36)
    texto_font = pygame.font.Font("PokemonGb-Raeo.ttf", 22)
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                transicion_batalla()
                return "exploracion"

        screen.fill((15, 15, 40))
        titulo = titulo_font.render("CONTROLES", True, (255,255,255))
        screen.blit(titulo, (230, 60))

        lineas = [
            "W A S D  -> Mover personaje",
            "E        -> Interactuar",
            "ESPACIO  -> Lanzar dados y avanzar",
            "ENTER    -> Continuar",
            "ALT + F4      -> Salir del juego",
            "",
            "Presiona ENTER para comenzar"
        ]
        y=150
        for linea in lineas:
            t = texto_font.render(linea, True, (255,255,255))
            screen.blit(t, (28,y))
            y += 50

        pygame.display.flip()
        clock.tick(60)
        
#
def transicion_batalla():
    cambiar_musica("sonidos.musica/battle.mp3")
    for x in range(0, WIDTH//2 + 20, 20): 
        pygame.draw.rect(screen, (0,0,0), (0, 0, x, HEIGHT))
        pygame.draw.rect(screen, (0,0,0), (WIDTH - x, 0, x, HEIGHT))
        pygame.display.flip()
        pygame.time.delay(20)

# variable para controlar las paredes actuales (pueblo o laboratorio)
def cambiar_musica(cancion):

    global current_music

    if current_music != cancion:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(cancion)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)  # Reproduce en bucle
        
        current_music = cancion

# FUNCIONES DE ESTADOS
def menu(screen):
    global cielo_offset, liga_offset, liga_rect

    screen.fill((0,0,0))

    # animación de fondo y liga
    cielo_offset -= 0.2
    liga_offset += 0.1
    
    # fondo
    screen.blit(cielo, (cielo_offset, 0))
    screen.blit(cielo, (cielo_offset + WIDTH, 0))

    # titulo
    tiempo = pygame.time.get_ticks() - start_time
    # ajusta la duración del fade-in (en milisegundos)
    fade_duracion = 2000  # 2 segundos
    # calcula el alpha (0 a 255) basado en el tiempo transcurrido
    alpha_blanco = max(0, 255 - int((tiempo / fade_duracion) * 255))
    # crea una copia del título para el efecto de fade-in
    titulo_blanco = titulo.copy()
    titulo_blanco.fill((255, 255, 255), special_flags=pygame.BLEND_RGB_MAX)
    # dibuja el título original y luego el blanco encima para el efecto de fade-in
    screen.blit(titulo, (WIDTH//2 - 300, -20))

    titulo_blanco.set_alpha(alpha_blanco)
    screen.blit(titulo_blanco, (WIDTH//2 - 300, -20))

    # liga centrado
    base_x = WIDTH // 2
    base_y = HEIGHT // 2 - 50

    liga_rect = liga.get_rect(center=(base_x, base_y ))

    #  AJUSTE FINO (acá va)
    liga_rect.x += liga_offset
    liga_rect.y += 120  #  movelo hasta que se vea bien

   
    screen.blit(liga, liga_rect)
    if liga_offset > 10:
        liga_offset = 10

    # protagonista grande
    prota_rect = protagonista.get_rect(bottomleft=(50, HEIGHT -40))
    prota_rect.y += 40
    screen.blit(protagonista, prota_rect)

    # texto tipo "presiona algo"
    font = pygame.font.Font("PokemonGb-Raeo.ttf", 15)
    texto_negro = font.render("Presiona ENTER para comenzar", True, (0,0,0))
    texto_blanco = font.render("Presiona ENTER para comenzar", True, (255,255,255))
    x, y = WIDTH//2 - 350, HEIGHT - 40
    # outline negro
    screen.blit(texto_negro, (x-2, y))
    screen.blit(texto_negro, (x+2, y))
    screen.blit(texto_negro, (x, y-2))
    screen.blit(texto_negro, (x, y+2))

    # texto principal
    screen.blit(texto_blanco, (x, y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        transicion_batalla()
        return "historia"

    return "menu"

def historia(screen):
    global indice_historia, enter_presionado

    screen.blit(fondo_tutorial, (0,0))
    screen.blit(profesor, (280, 100))

    dialogos = [
        ["Hola, soy el Profesor", "Cufre."],
        ["Este mundo esta lleno de desafios", "de todo tipo."],
        ["Por ahora vas a jugar", "la parte de Matematicas."],
        ["tenes que responder preguntas", "para poder avanzar"],
        ["Recuerda siempre ser el mejor y", "tener la puntuación más alta."],
        ["Tu aventura comienza ahora.","mucha suerte"]
    ]
    
    pygame.draw.rect(screen, (20,20,20), (40, 430, 720, 130))
    pygame.draw.rect(screen, (255,255,255), (40, 430, 720, 130), 4)

    font = pygame.font.Font("PokemonGb-Raeo.ttf", 20)
    texto1 = font.render(dialogos[indice_historia][0], True, (255,255,255))
    texto2 = font.render(dialogos[indice_historia][1], True, (255,255,255))
    
    screen.blit(texto1, (60, 450))
    screen.blit(texto2, (60, 475))

    aviso = font.render("ESPACIO", True, (255,255,255))
    screen.blit(aviso, (610, 530))

    keys = pygame.key.get_pressed()
    # control para avanzar el diálogo con ESPACIOS, evitando que se salte múltiples líneas por un solo toque
    if keys[pygame.K_SPACE] and not enter_presionado:
        enter_presionado = True

        if indice_historia < len(dialogos) - 1:
            siguiente.play()
            indice_historia += 1
        else:
            transicion_batalla()
            return "tutorial"

    if not keys[pygame.K_SPACE]:
        enter_presionado = False

    return "historia"
# mover al pj principal, con animación y colisiones
def mover_jugador():
    global player_x, player_y, direction, frame_index, current_sprite
    global paredes_actuales
    moving = False
    # Crear rectángulo del jugador para colisiones
    player_rect = pygame.Rect(player_x + 18, player_y + 45,  28, 24)
    # bloqueamos el movimiento si estamos en el diálogo con pitágoras
    
    if not dialogo_pitagoras:
        if keys[pygame.K_w]:
            nuevo_rect = player_rect.move(0, -3)
            if not any(nuevo_rect.colliderect(pared) for pared in paredes_actuales):
                player_y -= 3
            direction = "up"
            moving = True

        if keys[pygame.K_s]:
            nuevo_rect = player_rect.move(0, 3)
            if not any(nuevo_rect.colliderect(pared) for pared in paredes_actuales):
                player_y += 3
            direction = "down"
            moving = True

        if keys[pygame.K_a]:
            nuevo_rect = player_rect.move(-3, 0)
            if not any(nuevo_rect.colliderect(pared) for pared in paredes_actuales):
                player_x -= 3
            direction = "left"
            moving = True

        if keys[pygame.K_d]:
            nuevo_rect = player_rect.move(3, 0)
            if not any(nuevo_rect.colliderect(pared) for pared in paredes_actuales):
                player_x += 3
            direction = "right"
            moving = True
        
        if moving:
            frame_index += 0.1
        else:
            frame_index = 0

        if direction == "down":
            current_sprite = walk_down[int(frame_index) % 3]

        elif direction == "up":
            current_sprite = walk_up[int(frame_index) % 3]

        elif direction == "left":
            current_sprite = walk_left[int(frame_index) % 3]

        elif direction == "right":
            current_sprite = walk_right[int(frame_index) % 3]

def mostrar_cartel_zona(screen, nombre_zona, fuente, inicio):
    global cartel_activo, tiempo_cartel

    tiempo = time.time() - inicio

    if tiempo < 0.4:
        y = -80 + tiempo * 250

    elif tiempo < 2.6:
        y = 20

    else:
        y = 20 - (tiempo - 2.6) * 250

    pygame.draw.rect(screen, (255,255,255), (10, y, 360, 60))
    pygame.draw.rect(screen, (0,0,0), (10, y, 360, 60), 3)

    texto = fuente.render(nombre_zona, True, (0,0,0))
    texto_rect = texto.get_rect(center=(180, y + 30))
    

    screen.blit(texto, texto_rect)
    
    

#########################################################################################################################################################################################################################
estado = "menu"
# MAS VARIABLES #########################################################################################################################################################################################################################
player_x, player_y = 760, 450
direction = "down"
frame_index = 0
boss_x, boss_y = 365, 120
triangulo_x, triangulo_y = 342, 280
globo_x, globo_y = 308, 168
mesa1_x, mesa1_y = 314, 279
mesa2_x, mesa2_y = 646, 290
mesahis1_x, mesahis1_y = 280, 271
mesahis2_x, mesahis2_y = 604, 290
mesahis3_x, mesahis3_y = 77, 245
dialogo_pitagoras= False
dialogo_mainini = False
dialogo_barassi = False
dialogo_calzoski = False
ultimo_uso_e = 0
cartel_activo = False
tiempo_cartel = 0
fuente_grande = pygame.font.Font("PokemonGb-Raeo.ttf",20)
#sistema de colisiones
paredes_pueblo = [
            # límites del mapa
            pygame.Rect(0, 0, 1800, 100),      # arriba
            pygame.Rect(0, 1300, 1800, 100),   # abajo

            pygame.Rect(0, 0, 100, 1400),      # izquierda
            pygame.Rect(1700, 0, 100, 1400),   # derecha

            pygame.Rect(360, 200, 340, 140),  # casa mate
            pygame.Rect(940, 160, 236, 160),  # casa lengua
            pygame.Rect(360, 735, 225, 160), # casa geografia
            pygame.Rect(975, 760, 266, 155),  # casa historia
            pygame.Rect(705, 535, 165, 150),  # fuente
            pygame.Rect(635, 1000, 263, 150),    # lago
        ]
paredes_pueblo_2 = [
            # límites del mapa
            pygame.Rect(0, 0, 1800, 100),      # arriba
            pygame.Rect(0, 1300, 1800, 100),   # abajo

            pygame.Rect(0, 0, 100, 1400),      # izquierda
            pygame.Rect(1700, 0, 100, 1400),   # derecha

            pygame.Rect(383, 250, 290, 160),  # casa programacion
            pygame.Rect(944, 250, 290, 160),  # casa filosofia
            pygame.Rect(385, 780, 235, 160), # casa ingles
            pygame.Rect(990, 780, 266, 155),  # casa logica

        ]

paredes_matematicas = [
            pygame.Rect(0, 30, 800, 95),        # pared arriba
            pygame.Rect(0, 545, 800, 40),      # pared abajo
            pygame.Rect(0, 0, 35, 600),        # pared izquierda
            pygame.Rect(765, 0, 35, 600),      # pared derecha
            pygame.Rect(716, 125, 50, 50),      #esquina derecha
            pygame.Rect(40, 125, 50, 70),      #esquina izquierda
            

            pygame.Rect(340, 345, 120, 75),    # máquina/triángulo
            pygame.Rect(370, 135, 60, 50),     # pitagoras
        ]

paredes_geografia = [
            pygame.Rect(0, 30, 800, 95),        # pared arriba
            pygame.Rect(0, 545, 800, 40),      # pared abajo
            pygame.Rect(65, 0, 35, 600),        # pared izquierda
            pygame.Rect(700, 0, 35, 600),      # pared derecha

            pygame.Rect(355, 240, 90, 75),    # globo terraqueo
            pygame.Rect(370, 120, 60, 50),     # mainini
        ]

paredes_lengua = [
            pygame.Rect(0, 45, 800, 95),        # pared arriba
            pygame.Rect(0, 530, 800, 40),      # pared abajo
            pygame.Rect(0, 0, 35, 600),        # pared izquierda
            pygame.Rect(760, 0, 35, 600),      # pared derecha
            pygame.Rect(716, 125, 50, 50),      #esquina derecha
            pygame.Rect(40, 125, 50, 50),      #esquina izquierda

            pygame.Rect(450, 150, 120, 20),   #estanteria
            pygame.Rect(315, 305, 170, 90),    # mesa 1
            pygame.Rect(640, 310, 90, 80),    # mesa 2
            
            pygame.Rect(370, 140, 60, 50),     # barassi
        ]
paredes_historia = [
            pygame.Rect(0, 50, 800, 115),        # pared arriba
            pygame.Rect(0, 530, 800, 40),      # pared abajo
            pygame.Rect(0, 0, 35, 600),        # pared izquierda
            pygame.Rect(760, 0, 35, 600),      # pared derecha
            pygame.Rect(716, 125, 50, 50),      #esquina derecha
            pygame.Rect(40, 125, 50, 50),      #esquina izquierda

            pygame.Rect(500, 150, 80, 80),   #estanteria
            pygame.Rect(280, 295, 237, 100),    # mesa 1
            pygame.Rect(610, 325, 110, 65),    # mesa 2
            pygame.Rect(90, 340, 67, 50),    # mesa 2

            pygame.Rect(370, 150, 60, 50),     # calzoski
        ]
paredes_programacion = [
            pygame.Rect(0, 50, 800, 115),        # pared arriba
            pygame.Rect(0, 530, 800, 40),      # pared abajo
            pygame.Rect(0, 0, 35, 600),        # pared izquierda
            pygame.Rect(760, 0, 35, 600),      # pared derecha
            pygame.Rect(716, 125, 50, 50),      #esquina derecha
            pygame.Rect(40, 125, 50, 50),      #esquina izquierda

            pygame.Rect(500, 150, 80, 80),   #estanteria
            pygame.Rect(280, 295, 237, 100),    # mesa 1
            pygame.Rect(610, 325, 110, 65),    # mesa 2
            pygame.Rect(90, 340, 67, 50),    # mesa 2

            pygame.Rect(370, 150, 60, 50),     # calzoski
        ]

running = True
# Bucle principal del juego ##########################################################################################################################################################################################################################
while running:
    
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    #  CINEMÁTICA
    if estado == "menu":
        cambiar_musica("sonidos.musica/menu.mp3")
        estado = menu(screen)

    elif estado == "historia":
        cambiar_musica("sonidos.musica/tutorial.mp3")
        estado= historia(screen)

    elif estado == "tutorial":
        estado = pantalla_controles(screen)
        cartel_activo = True
        tiempo_cartel = time.time()

    #  EXPLORACIÓN
    elif estado == "exploracion":

        cambiar_musica("sonidos.musica/pueblo.mp3")
        paredes_actuales = paredes_pueblo
        # lógica de movimiento y colisiones
        mover_jugador()
        # lógica de cámara (centrada en el jugador)
        sprite_w, sprite_h = 66, 73
        camera_x = player_x + sprite_w//2 - WIDTH // 2
        camera_y = player_y + sprite_h//2 - HEIGHT // 2
        camera_x = max(0, min(camera_x, mapa_pueblo.get_width() - WIDTH))
        camera_y = max(0, min(camera_y, mapa_pueblo.get_height() - HEIGHT))
        screen.blit(mapa_pueblo, (-camera_x, -camera_y))
        screen.blit(matematicas, (casa_mate_x - camera_x, casa_mate_y - camera_y))
        screen.blit(geografia, (casa_geo_x - camera_x, casa_geo_y - camera_y))
        screen.blit(lengua, (casa_lengua_x - camera_x, casa_lengua_y - camera_y))
        screen.blit(historias, (casa_historia_x - camera_x, casa_historia_y - camera_y))

        current_sprite = pygame.transform.scale(current_sprite, (64, 73)) 
        screen.blit(current_sprite,(player_x - camera_x,player_y - camera_y))
        
        # dibujar rectángulo de colisión del jugador (opcional, para debug)
        player_rect = pygame.Rect(player_x + 18, player_y + 45, 28, 24)

        # Casas a las que se puede entrar.
        # Por ahora dejamos únicamente Matemáticas.
        casas = {
            "matematicas": pygame.Rect(500, 330, 60, 40),
            "lengua": pygame.Rect(1030, 330, 60, 40),
            "geografia": pygame.Rect(440, 900, 60, 40),
            "historia": pygame.Rect(1080, 900, 60, 40),
            "segundo pueblo": pygame.Rect(710, 0, 165, 150),
        }
        

        screen.blit(mate_arriba, (casa_mate_arriba_x - camera_x, casa_mate_arriba_y - camera_y))
        screen.blit(geo_arriba, (casa_geo_arriba_x - camera_x, casa_geo_arriba_y - camera_y))
        screen.blit(lengua_arriba, (casa_lengua_arriba_x - camera_x, casa_lengua_arriba_y - camera_y))
        screen.blit(historia_arriba, (casa_historia_arriba_x - camera_x, casa_historia_arriba_y - camera_y))
        if cartel_activo:

            mostrar_cartel_zona(
                screen,
                "primer pueblo",
                fuente_grande, 
                tiempo_cartel
            )

        if time.time() - tiempo_cartel > 3:
            cartel_activo = False
        for nombre, rect in casas.items():

            if player_rect.colliderect(rect):

                font = pygame.font.Font("PokemonGb-Raeo.ttf", 18)
                msg_negro = font.render(f"Entrar a {nombre}", True, (0,0,0))
                msg_blanco = font.render(f"Entrar a {nombre}", True, (255,255,255))
                x, y = 250,520
                 # outline negro
                screen.blit(msg_negro, (x-2, y))
                screen.blit(msg_negro, (x+2, y))
                screen.blit(msg_negro, (x, y-2))
                screen.blit(msg_negro, (x, y+2))

                # texto principal
                screen.blit(msg_blanco, (x, y))
            
                if keys[pygame.K_e] and time.time() - ultimo_uso_e > 0.5:
                    ultimo_uso_e = time.time()
                    if nombre == "matematicas":
                        puerta.play()
                        player_x = 365
                        player_y = 460
                        estado = "lab_mate"

                    elif nombre == "lengua":
                        puerta.play()
                        player_x = 365
                        player_y = 460
                        estado = "lab_lengua"

                    elif nombre == "geografia":
                        puerta.play()
                        player_x = 365
                        player_y = 460
                        estado = "lab_geo"

                    elif nombre == "historia":
                        puerta.play()
                        player_x = 365
                        player_y = 460
                        estado = "lab_his"

                    elif nombre == "segundo pueblo":
                        cartel_activo = True
                        tiempo_cartel = time.time()

                        puerta.play()
                        player_x = 755
                        player_y = 1000
                        estado = "exploracion_2"
            
    elif estado == "exploracion_2":
        
        paredes_actuales = paredes_pueblo_2
        # lógica de movimiento y colisiones
        mover_jugador()
        # lógica de cámara (centrada en el jugador)
        sprite_w, sprite_h = 66, 73
        camera_x = player_x + sprite_w//2 - WIDTH // 2
        camera_y = player_y + sprite_h//2 - HEIGHT // 2
        camera_x = max(0, min(camera_x, mapa_pueblo_2.get_width() - WIDTH))
        camera_y = max(0, min(camera_y, mapa_pueblo_2.get_height() - HEIGHT))
        screen.blit(mapa_pueblo_2, (-camera_x, -camera_y))    

        current_sprite = pygame.transform.scale(current_sprite, (64, 73)) 
        screen.blit(current_sprite,(player_x - camera_x,player_y - camera_y))
        screen.blit(programacion, (casa_programacion_x - camera_x, casa_programacion_y - camera_y))
        screen.blit(ingles, (casa_ingles_x - camera_x, casa_ingles_y - camera_y))
        screen.blit(logica, (casa_logica_x - camera_x, casa_logica_y - camera_y))
        screen.blit(filosofia, (casa_filosofia_x - camera_x, casa_filosofia_y - camera_y))
        

        

        current_sprite = pygame.transform.scale(current_sprite, (64, 73))

        screen.blit(
            current_sprite,
            (
                player_x - camera_x,
                player_y - camera_y
            )
        )
        player_rect = pygame.Rect(player_x + 18, player_y + 45, 28, 24)

            


        # Casas a las que se puede entrar.
        # Por ahora dejamos únicamente Matemáticas.
        casas = {
            "programacion": pygame.Rect(492, 388, 60, 40),
            "filosofia": pygame.Rect(1060, 388, 60, 40),
            "ingles": pygame.Rect(475, 920, 60, 40),
            "logica": pygame.Rect(1086, 900, 60, 40),
            "primer pueblo": pygame.Rect(710, 1050, 165, 150),
        }
        if cartel_activo:

            mostrar_cartel_zona(
                screen,
                "Segundo Pueblo",
                fuente_grande,
                tiempo_cartel
            )

        if time.time() - tiempo_cartel > 3:
            cartel_activo = False
        
        for nombre, rect in casas.items():

            if player_rect.colliderect(rect):

                font = pygame.font.Font("PokemonGb-Raeo.ttf", 18)
                msg_negro = font.render(f"Entrar a {nombre}", True, (0,0,0))
                msg_blanco = font.render(f"Entrar a {nombre}", True, (255,255,255))
                x, y = 250,520
                 # outline negro
                screen.blit(msg_negro, (x-2, y))
                screen.blit(msg_negro, (x+2, y))
                screen.blit(msg_negro, (x, y-2))
                screen.blit(msg_negro, (x, y+2))

                # texto principal
                screen.blit(msg_blanco, (x, y))
            
                if keys[pygame.K_e] and time.time() - ultimo_uso_e > 0.5:
                    ultimo_uso_e = time.time()
                    if nombre == "logica":
                        puerta.play()
                        player_x = 365
                        player_y = 460
                        estado = "lab_logica"
                    elif nombre == "programacion":
                        puerta.play()
                        player_x = 365
                        player_y = 460
                        estado = "lab_prog"
                    elif nombre == "filosofia":
                        puerta.play()
                        player_x = 365
                        player_y = 460
                        estado = "lab_filosofia"
                    elif nombre == "ingles":
                        estado = "lab_ingles"
                    elif nombre == "primer pueblo":
                        cartel_activo = True
                        tiempo_cartel = time.time()
                        puerta.play()
                        player_x = 757
                        player_y = 150
                        estado = "exploracion"
                        
        
                            
    elif estado=="lab_mate":

        cambiar_musica("sonidos.musica/gym.mp3")
        paredes_actuales = paredes_matematicas
        mover_jugador()
        screen.blit(mapa_matematicas, (0,0))

        boss = pygame.transform.scale(boss_matematicas, (63, 96))
        screen.blit(boss, (boss_x, boss_y))

        current_sprite = pygame.transform.scale(current_sprite, (64, 73))
        screen.blit(current_sprite, (player_x, player_y))
        screen.blit(triangulo, (triangulo_x, triangulo_y))

        #puerta de salidas

        puerta_salida = pygame.Rect(365, 540, 70, 30)
        puerta_salida.x -= 20
        puerta_salida.y -= 20
        if abs(player_x - puerta_salida.x) < 50 and abs(player_y - puerta_salida.y) < 50:
            font = pygame.font.Font("PokemonGb-Raeo.ttf", 30)
            msg_negro = font.render("salir", True, (0,0,0))
            msg_blanco = font.render("salir", True, (255,255,255))
            x, y = 100,510
            # outline negro
            screen.blit(msg_negro, (x-2, y))
            screen.blit(msg_negro, (x+2, y))
            screen.blit(msg_negro, (x, y-2))
            screen.blit(msg_negro, (x, y+2))

            # texto principal
            screen.blit(msg_blanco, (x, y))

            if keys[pygame.K_e] and time.time() - ultimo_uso_e > 0.5:
                cartel_activo = True
                tiempo_cartel = time.time()
                ultimo_uso_e = time.time()
                puerta.play()
                player_x = 500
                player_y = 310

                estado = "exploracion"

        # detectar cercanía

        if abs(player_x - boss_x) < 50 and abs(player_y - boss_y) < 50:
            font = pygame.font.Font("PokemonGb-Raeo.ttf", 30)
            msg_negro = font.render("Hablar con pitagoras", True, (0,0,0))
            msg_blanco = font.render("Hablar con pitagoras", True, (255,255,255))
            x, y = 100,510
            # outline negro
            screen.blit(msg_negro, (x-2, y))
            screen.blit(msg_negro, (x+2, y))
            screen.blit(msg_negro, (x, y-2))
            screen.blit(msg_negro, (x, y+2))

            # texto principal
            screen.blit(msg_blanco, (x, y))

            if keys[pygame.K_e] and time.time() - ultimo_uso_e > 0.5:
                ultimo_uso_e = time.time()
                
                dialogo_pitagoras = True
                siguiente.play()
            if dialogo_pitagoras:
                    
                    pygame.draw.rect(screen, (20,20,20), (40, 440, 720, 130))
                    pygame.draw.rect(screen, (255,255,255), (40, 440, 720, 130), 4)

                    font = pygame.font.Font("PokemonGb-Raeo.ttf", 15)
                    texto = font.render("corbalan: asi que eres bueno en matematicas?", True, (255,255,255))
                    screen.blit(texto, (70, 480))

                    aviso = font.render("ESPACIO", True, (255,255,255))
                    screen.blit(aviso, (610, 530))

                    if keys[pygame.K_SPACE]:
                        transicion_batalla()
                        estado = "combate_matematicas"

        paredes_actuales = paredes_pueblo

    elif estado=="lab_geo":

        cambiar_musica("sonidos.musica/gym.mp3")
        paredes_actuales = paredes_geografia
        mover_jugador()
        screen.blit(mapa_geografia, (0,0))
        boss_x, boss_y = 367, 78
        boss = pygame.transform.scale(boss_geografia, (70, 110))
        screen.blit(boss, (boss_x, boss_y))
        current_sprite = pygame.transform.scale(current_sprite, (64, 73))
        screen.blit(current_sprite, (player_x, player_y))
        screen.blit(globo, (globo_x, globo_y))  

        puerta_salida = pygame.Rect(365, 540, 70, 30)
        puerta_salida.x -= 20
        puerta_salida.y -= 20
        if abs(player_x - puerta_salida.x) < 50 and abs(player_y - puerta_salida.y) < 50:
            font = pygame.font.Font("PokemonGb-Raeo.ttf", 30)
            msg_negro = font.render("salir", True, (0,0,0))
            msg_blanco = font.render("salir", True, (255,255,255))
            x, y = 100,510
            # outline negro
            screen.blit(msg_negro, (x-2, y))
            screen.blit(msg_negro, (x+2, y))
            screen.blit(msg_negro, (x, y-2))
            screen.blit(msg_negro, (x, y+2))

            # texto principal
            screen.blit(msg_blanco, (x, y))

            if keys[pygame.K_e] and time.time() - ultimo_uso_e > 0.5:
                cartel_activo = True
                tiempo_cartel = time.time()
                ultimo_uso_e = time.time()
                puerta.play()
                player_x = 440
                player_y = 860

                estado = "exploracion"
        
        # detectar cercanía
        if abs(player_x - boss_x) < 50 and abs(player_y - boss_y) < 50:
            font = pygame.font.Font("PokemonGb-Raeo.ttf", 30)
            msg_negro = font.render("Hablar con mainini", True, (0,0,0))
            msg_blanco = font.render("Hablar con mainini", True, (255,255,255))
            x, y = 100,510
            # outline negro
            screen.blit(msg_negro, (x-2, y))
            screen.blit(msg_negro, (x+2, y))
            screen.blit(msg_negro, (x, y-2))
            screen.blit(msg_negro, (x, y+2))

            # texto principal
            screen.blit(msg_blanco, (x, y))

            if keys[pygame.K_e] and time.time() - ultimo_uso_e > 0.5:
                ultimo_uso_e = time.time()
                dialogo_mainini = True
                siguiente.play()
            if dialogo_mainini:
                    
                    pygame.draw.rect(screen, (20,20,20), (40, 440, 720, 130))
                    pygame.draw.rect(screen, (255,255,255), (40, 440, 720, 130), 4)

                    font = pygame.font.Font("PokemonGb-Raeo.ttf", 15)
                    texto = font.render("Mainini: Veamos cuanto sabes de geografia...", True, (255,255,255))
                    screen.blit(texto, (70, 480))

                    aviso = font.render("ESPACIO", True, (255,255,255))
                    screen.blit(aviso, (610, 530))

                    if keys[pygame.K_SPACE]:
                        transicion_batalla()
                        estado = "combate_geografia"
        paredes_actuales = paredes_pueblo
    elif estado=="lab_lengua":

        cambiar_musica("sonidos.musica/gym.mp3")
        paredes_actuales = paredes_lengua
        mover_jugador()
        screen.blit(mapa_lengua, (0,0))
        boss_x, boss_y = 367, 100
        boss = pygame.transform.scale(boss_lengua, (70, 110))
        screen.blit(boss, (boss_x, boss_y))
        current_sprite = pygame.transform.scale(current_sprite, (64, 73))
        screen.blit(current_sprite, (player_x, player_y))
        screen.blit(mesa1, (mesa1_x, mesa1_y))
        screen.blit(mesa2, (mesa2_x, mesa2_y))
        puerta_salida = pygame.Rect(365, 520, 70, 30)
        puerta_salida.x -= 20
        puerta_salida.y -= 20
        if abs(player_x - puerta_salida.x) < 50 and abs(player_y - puerta_salida.y) < 50:
            font = pygame.font.Font("PokemonGb-Raeo.ttf", 30)
            msg_negro = font.render("salir", True, (0,0,0))
            msg_blanco = font.render("salir", True, (255,255,255))
            x, y = 100,510
            # outline negro
            screen.blit(msg_negro, (x-2, y))
            screen.blit(msg_negro, (x+2, y))
            screen.blit(msg_negro, (x, y-2))
            screen.blit(msg_negro, (x, y+2))

            # texto principal
            screen.blit(msg_blanco, (x, y))

            if keys[pygame.K_e] and time.time() - ultimo_uso_e > 0.5:
                cartel_activo = True
                tiempo_cartel = time.time()
                ultimo_uso_e = time.time()
                puerta.play()
                player_x = 1030
                player_y = 330

                estado = "exploracion"
        
        # detectar cercanía
        if abs(player_x - boss_x) < 50 and abs(player_y - boss_y) < 50:
            font = pygame.font.Font("PokemonGb-Raeo.ttf", 30)
            msg_negro = font.render("Hablar con barassi", True, (0,0,0))
            msg_blanco = font.render("Hablar con barassi", True, (255,255,255))
            x, y = 100,510
            # outline negro
            screen.blit(msg_negro, (x-2, y))
            screen.blit(msg_negro, (x+2, y))
            screen.blit(msg_negro, (x, y-2))
            screen.blit(msg_negro, (x, y+2))

            # texto principal
            screen.blit(msg_blanco, (x, y))

            if keys[pygame.K_e] and time.time() - ultimo_uso_e > 0.5:
                ultimo_uso_e = time.time()
                dialogo_mainini = True
                siguiente.play()
            if dialogo_mainini:
                    
                    pygame.draw.rect(screen, (20,20,20), (40, 440, 720, 130))
                    pygame.draw.rect(screen, (255,255,255), (40, 440, 720, 130), 4)

                    font = pygame.font.Font("PokemonGb-Raeo.ttf", 15)
                    texto = font.render("barassi: JAJAJAJAJJAJA... prueba sorpresa.", True, (255,255,255))
                    screen.blit(texto, (70, 480))

                    aviso = font.render("ESPACIO", True, (255,255,255))
                    screen.blit(aviso, (610, 530))

                    if keys[pygame.K_SPACE]:
                        transicion_batalla()
                        estado = "combate_lengua"
        paredes_actuales = paredes_pueblo 

    elif estado == "lab_his":

        cambiar_musica("sonidos.musica/gym.mp3")
        paredes_actuales = paredes_historia
        mover_jugador()
        screen.blit(mapa_historia, (0,0))
        boss_x, boss_y = 367, 120
        boss = pygame.transform.scale(boss_historia, (70, 110))
        screen.blit(boss, (boss_x, boss_y))
        current_sprite = pygame.transform.scale(current_sprite, (64, 73))
        screen.blit(current_sprite, (player_x, player_y))
        screen.blit(mesahis1, (mesahis1_x, mesahis1_y))
        screen.blit(mesahis2, (mesahis2_x, mesahis2_y))
        screen.blit(mesahis3, (mesahis3_x, mesahis3_y))
        puerta_salida = pygame.Rect(365, 520, 70, 30)
        puerta_salida.x -= 20
        puerta_salida.y -= 20
        if abs(player_x - puerta_salida.x) < 50 and abs(player_y - puerta_salida.y) < 50:
            font = pygame.font.Font("PokemonGb-Raeo.ttf", 30)
            msg_negro = font.render("salir", True, (0,0,0))
            msg_blanco = font.render("salir", True, (255,255,255))
            x, y = 100,510
            # outline negro
            screen.blit(msg_negro, (x-2, y))
            screen.blit(msg_negro, (x+2, y))
            screen.blit(msg_negro, (x, y-2))
            screen.blit(msg_negro, (x, y+2))

            # texto principal
            screen.blit(msg_blanco, (x, y))

            if keys[pygame.K_e] and time.time() - ultimo_uso_e > 0.5:
                cartel_activo = True
                tiempo_cartel = time.time()
                ultimo_uso_e = time.time()
                puerta.play()
                player_x = 1080
                player_y = 900

                estado = "exploracion"
        
        # detectar cercanía
        if abs(player_x - boss_x) < 50 and abs(player_y - boss_y) < 50:
            font = pygame.font.Font("PokemonGb-Raeo.ttf", 20)
            msg_negro = font.render("Hablar con calzoski(historia)", True, (0,0,0))
            msg_blanco = font.render("Hablar con calzoski(historia)", True, (255,255,255))
            x, y = 100,510
            # outline negro
            screen.blit(msg_negro, (x-2, y))
            screen.blit(msg_negro, (x+2, y))
            screen.blit(msg_negro, (x, y-2))
            screen.blit(msg_negro, (x, y+2))

            # texto principal
            screen.blit(msg_blanco, (x, y))

            if keys[pygame.K_e] and time.time() - ultimo_uso_e > 0.5:
                adriana_salte.play()
                ultimo_uso_e = time.time()
                dialogo_mainini = True
                siguiente.play()
            if dialogo_mainini:
                    
                    pygame.draw.rect(screen, (20,20,20), (40, 440, 720, 130))
                    pygame.draw.rect(screen, (255,255,255), (40, 440, 720, 130), 4)

                    font = pygame.font.Font("PokemonGb-Raeo.ttf", 15)
                    texto = font.render("calzoski: ADRIANA SALTE ewe (historia)", True, (255,255,255))
                    screen.blit(texto, (70, 480))

                    aviso = font.render("ESPACIO", True, (255,255,255))
                    screen.blit(aviso, (610, 530))

                    if keys[pygame.K_SPACE]:
                        transicion_batalla()
                        estado = "combate_lengua"
        paredes_actuales = paredes_pueblo 

    elif estado == "lab_prog":

        cambiar_musica("sonidos.musica/gym.mp3")
        paredes_actuales = paredes_programacion
        mover_jugador()
        screen.blit(mapa_programacion, (0,0))
        boss_x, boss_y = 340, 120
        boss = pygame.transform.scale(boss_programacion, (140, 90))
        screen.blit(boss, (boss_x, boss_y))
        current_sprite = pygame.transform.scale(current_sprite, (64, 73))
        screen.blit(current_sprite, (player_x, player_y))
        screen.blit(mesahis1, (mesahis1_x, mesahis1_y))
        screen.blit(mesahis2, (mesahis2_x, mesahis2_y))
        screen.blit(mesahis3, (mesahis3_x, mesahis3_y))
        puerta_salida = pygame.Rect(365, 520, 70, 30)
        puerta_salida.x -= 20
        puerta_salida.y -= 20
        if abs(player_x - puerta_salida.x) < 50 and abs(player_y - puerta_salida.y) < 50:
            font = pygame.font.Font("PokemonGb-Raeo.ttf", 30)
            msg_negro = font.render("salir", True, (0,0,0))
            msg_blanco = font.render("salir", True, (255,255,255))
            x, y = 100,510
            # outline negro
            screen.blit(msg_negro, (x-2, y))
            screen.blit(msg_negro, (x+2, y))
            screen.blit(msg_negro, (x, y-2))
            screen.blit(msg_negro, (x, y+2))

            # texto principal
            screen.blit(msg_blanco, (x, y))

            if keys[pygame.K_e] and time.time() - ultimo_uso_e > 0.5:
                cartel_activo = True
                tiempo_cartel = time.time()
                ultimo_uso_e = time.time()
                puerta.play()
                player_x = 493
                player_y = 380

                estado = "exploracion_2"
        
        # detectar cercanía
        if abs(player_x - boss_x) < 50 and abs(player_y - boss_y) < 50:
            font = pygame.font.Font("PokemonGb-Raeo.ttf", 20)
            msg_negro = font.render("Hablar con calzoski(historia)", True, (0,0,0))
            msg_blanco = font.render("Hablar con calzoski(historia)", True, (255,255,255))
            x, y = 100,510
            # outline negro
            screen.blit(msg_negro, (x-2, y))
            screen.blit(msg_negro, (x+2, y))
            screen.blit(msg_negro, (x, y-2))
            screen.blit(msg_negro, (x, y+2))

            # texto principal
            screen.blit(msg_blanco, (x, y))

            if keys[pygame.K_e] and time.time() - ultimo_uso_e > 0.5:
                adriana_salte.play()
                ultimo_uso_e = time.time()
                dialogo_mainini = True
                siguiente.play()
            if dialogo_mainini:
                    
                    pygame.draw.rect(screen, (20,20,20), (40, 440, 720, 130))
                    pygame.draw.rect(screen, (255,255,255), (40, 440, 720, 130), 4)

                    font = pygame.font.Font("PokemonGb-Raeo.ttf", 15)
                    texto = font.render("calzoski: ADRIANA SALTE ewe (historia)", True, (255,255,255))
                    screen.blit(texto, (70, 480))

                    aviso = font.render("ESPACIO", True, (255,255,255))
                    screen.blit(aviso, (610, 530))

                    if keys[pygame.K_SPACE]:
                        transicion_batalla()
                        estado = "combate_lengua"
        paredes_actuales = paredes_pueblo 

    # COMBATE
    elif estado == "combate_matematicas":
        
        resultado = combate_mate.iniciar_combate(screen)
        print(resultado)
        if resultado == "menu":
            estado = "lab_mate"
            indice_historia = 0
            dialogo_pitagoras = False
            player_x, player_y = 365, 430
           
        
    elif estado == "combate_geografia":
        resultado = combate_geo.iniciar_combate(screen)
        print(resultado)
        if resultado == "menu":
            estado = "lab_geo"
            indice_historia = 0
            dialogo_pitagoras = False
            player_x, player_y = 365, 430
           

    elif estado == "combate_lengua":
        resultado = combate_lengua.iniciar_combate(screen)
        print(resultado)
        if resultado == "menu":
            estado = "lab_lengua"
            indice_historia = 0
            dialogo_pitagoras = False
            player_x, player_y = 365, 430
           

    elif estado == "combate_logica":
        combate_logica.iniciar_combate(screen)
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()