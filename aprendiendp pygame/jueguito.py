import pygame
import random

reloj = pygame.time.Clock()

# Inicializar Pygame
pygame.init()

# Definir los colores que vamos a usar
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Definir las dimensiones de la ventana
VENTANA_ANCHO = 500
VENTANA_ALTO = 500

# Crear la ventana
ventana = pygame.display.set_mode((VENTANA_ANCHO, VENTANA_ALTO))


# Definir la clase del objeto que vamos a cazar
class Punto(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(VENTANA_ANCHO - self.rect.width)
        self.rect.y = random.randrange(VENTANA_ALTO - self.rect.height)
        self.velocidad_x = random.randrange(-5, 5)
        self.velocidad_y = random.randrange(-5, 5)

    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        if self.rect.right > VENTANA_ANCHO or self.rect.left < 0:
            self.velocidad_x = -self.velocidad_x
        if self.rect.bottom > VENTANA_ALTO or self.rect.top < 0:
            self.velocidad_y = -self.velocidad_y


# Crear un grupo para los objetos
grupo_puntos = pygame.sprite.Group()

# Crear algunos objetos y añadirlos al grupo
for i in range(10):
    punto = Punto()
    grupo_puntos.add(punto)

# Definir la fuente para el texto
fuente = pygame.font.SysFont('Calibri', 25, True, False)

# Definir la puntuación inicial
puntuacion = 0

# Bucle principal del juego
hecho = False
while not hecho:
    # Gestionar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Comprobar si se ha hecho clic en un objeto
            pos = pygame.mouse.get_pos()
            punto_clic = [punto for punto in grupo_puntos if punto.rect.collidepoint(pos)]
            if punto_clic:
                grupo_puntos.remove(punto_clic[0])
                puntuacion += 1

    # Actualizar la posición de los objetos
    grupo_puntos.update()

    # Dibujar la pantalla
    ventana.fill(BLANCO)
    grupo_puntos.draw(ventana)
    texto_puntuacion = fuente.render("Puntuación: " + str(puntuacion), True, NEGRO)
    ventana.blit(texto_puntuacion, [10, 10])
    pygame.display.flip()

    # Limitar la tasa de refresco de la pantalla
    reloj.tick(60)

# Salir de Pygame
pygame.quit()
