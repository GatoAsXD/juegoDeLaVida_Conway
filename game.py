#Librerias necesarias
import numpy as np
import pygame
import time
#Inicializamos pygame
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
nxC,nyC = 50,50
#Dimensiones de la celda
dimCW = width  / nxC
dimCH = height / nyC
#Estado de las celdas. Viva = 1; Muerta = 0;
gameState = np.zeros((nxC,nyC))
#Control de ejecucion del juego
pauseExect = False

#Bucle de ejecucion (infinito)
while True:
    #Copia estado actual juego en cada iteracion
    newGameState = np.copy(gameState)
    #Limpiar la pantalla
    screen.fill(bg)
    #Darle al sistema un respiro
    time.sleep(0.1)
    #Registrar eventos de teclado y raton
    ev = pygame.event.get()
    
    for event in ev:
        #Se detecta si se presiona una tecla
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
        #Se detecta si se presiona el raton
        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX,posY = pygame.mouse.get_pos()
            celX,celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX,celY] = not mouseClick[2]
    for y in  range(0,nxC):
        for x in range(0,nyC):
            #Estado de pausa
            if not pauseExect:
                #Calculamos el numero de vecinos cercanos
                n_neigh =   gameState[(x-1)%nxC,(y-1)%nyC] + \
                            gameState[(x)  %nxC,(y-1)%nyC] + \
                            gameState[(x+1)%nxC,(y-1)%nyC] + \
                            gameState[(x-1)%nxC,(y)  %nyC] + \
                            gameState[(x+1)%nxC,(y)  %nyC] + \
                            gameState[(x-1)%nxC,(y+1)%nyC] + \
                            gameState[(x)  %nxC,(y+1)%nyC] + \
                            gameState[(x+1)%nxC,(y+1)%nyC]
                # Regla 1: Una celula muerta con exactamente 3 vecinas vivas, "revive".
                if gameState[x,y] == 0 and n_neigh == 3:
                    newGameState[x,y] = 1
                # Regla 2: Una celula viva con menos de 2 o mas de 3 vecinas vivas, "Muere"
                elif gameState[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x,y] = 0                           
            #Poligono de cada celda a dibujar
            poly = [((x)   * dimCW,  y    * dimCH),
                    ((x+1) * dimCW,  y    * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x)   * dimCW, (y+1) * dimCH)]
            #Dibujamos la celda para cada par de X e Y.
            if newGameState[x,y] == 0:
                pygame.draw.polygon(screen, (128,128,128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255,255,255), poly, 0)
    #Actualizamos estado de juego
    gameState = np.copy(newGameState)    
    #Actualizamos pantalla
    pygame.display.flip()