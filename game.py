import numpy as np
import pygame

pygame.init()
#Parametros ancho y alto de la pantalla
width,height = 1000, 1000
#Creacion pantalla
screen = pygame.display.set_mode((height,width))
#Parametros color fondo
bg = 25, 25, 25
#Implementacion color en pantalla
screen.fill(bg)
#Celdas a crear
nxC,nyC = 25,25
#Dimensiones de la celda
dimCW = width  / nxC
dimCH = height / nyC

#Bucle de ejecucion (infinito)
while True:
    for y in  range(0,nxC):
        for x in range(0,nyC):
            poly = [((x)   * dimCW,  y    * dimCH),
                    ((x+1) * dimCW,  y    * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x)   * dimCW, (y+1) * dimCH)]
            pygame.draw.polygon(screen, (128,128,128), poly, 1)
        
        pygame.display.flip()