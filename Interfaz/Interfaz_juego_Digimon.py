#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ---------------------------
# Importacion de los módulos
# ---------------------------

import pygame, random, os, sys
from pygame.locals import *

# -----------
# Constantes
# -----------
main_dir = os.path.split(os.path.abspath(__file__))[0]
SCREEN_WIDTH = 977
SCREEN_HEIGHT = 589

# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
class Carta(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(main_dir, 'Imagenes', "ADelicatePlan_BT3_097.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.centery = SCREEN_HEIGHT / 2
        self.speed = [3, 3]
    def update(self):
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed[1] = -self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1]))

# ------------------------------
# Funcion principal del juego
# ------------------------------


def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("DIGIMON TCG")
    tablero = pygame.image.load(os.path.join(main_dir, 'Imagenes', "tablero.jpg")).convert_alpha()
    carta=Carta()
    clock = pygame.time.Clock()
    #Indicamos el fondo
    screen.blit(tablero, (0, 0))
    pygame.display.flip() 
    # el bucle principal del juego
    while True:
	#60FPS
        clock.tick(60)
        carta.update()
        #Movemos la carta
        screen.blit(tablero, (0, 0))	
        screen.blit(carta.image, carta.rect)
        pygame.display.flip()   
        # Posibles entradas del teclado y mouse	
       	for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()
