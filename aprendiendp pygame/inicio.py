import pygame, sys
from pygame.locals import *

pygame.init()

PANTALLA = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Primer Jueguito')

BLANCOSITO = (236, 244, 234)
ROJITO = (240, 114, 113)
NEGRO = (0, 0, 0)
AZULITO = (193, 223, 227)

OTRO_COLOR = (216, 200, 250)
OTRO_COLOR2 = (113, 240, 158)

PANTALLA.fill(BLANCOSITO)

rectangulo1 = pygame.draw.rect(PANTALLA, ROJITO, (100, 50, 100, 50))
print(rectangulo1)
linea1 = pygame.draw.line(PANTALLA, OTRO_COLOR, (100,104), (199,104),10)

circulo1 = pygame.draw.circle(PANTALLA, AZULITO, (122,250), 20,19)

elipse = pygame.draw.ellipse(PANTALLA, OTRO_COLOR2, (100,200,40,80),10)

puntos = [(123,300), (100,100), (150,200) ]

poligono = pygame.draw.polygon(PANTALLA,AZULITO, puntos, 8)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
