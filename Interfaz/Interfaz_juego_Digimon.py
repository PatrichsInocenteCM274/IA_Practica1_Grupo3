#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ---------------------------
# Importacion de los módulos
# ---------------------------

import pygame, random, os, sys
from pygame.locals import *
from random import choice
# -----------
# Constantes
# -----------
main_dir = os.path.split(os.path.abspath(__file__))[0]
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
Nombres_digimones = []
archivo = open('digimon_lista.txt', 'r')
for linea in archivo:
    print (linea)
    Nombres_digimones.append(linea.strip())
archivo.close()
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------


class Carta(pygame.sprite.Sprite):
    
    def __init__(self,x,y,jugador):
        pygame.sprite.Sprite.__init__(self)
        nombre_carta=choice(Nombres_digimones)
        if jugador=='jugador1':
            image_carta = pygame.transform.rotate(pygame.image.load(os.path.join(main_dir, 'Imagenes', str(nombre_carta)+'.png')).convert_alpha(),-90)
            image_posterior=pygame.transform.rotate(pygame.image.load(os.path.join(main_dir, 'Imagenes', 'reverso.jpg')).convert_alpha(),-90)
        if jugador=='jugador2':
            image_carta = pygame.transform.rotate(pygame.image.load(os.path.join(main_dir, 'Imagenes', str(nombre_carta)+'.png')).convert_alpha(),90)
            image_posterior=pygame.transform.rotate(pygame.image.load(os.path.join(main_dir, 'Imagenes', 'reverso.jpg')).convert_alpha(),90)
        self.image = pygame.transform.scale(image_carta, (160,100 ))
        self.posterior=pygame.transform.scale(image_posterior, (160,100 ))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed=[0,0]
    def mover(self,x,y):
           if self.rect.centerx >= x:
              self.speed[0] = -3
              if self.rect.centerx-x<5: self.speed[0] = 0
           if self.rect.centerx <= x:
              self.speed[0] = 3
              if x-self.rect.centerx<5: self.speed[0] = 0
           if self.rect.centery >= y :
              self.speed[1] = -3
              if self.rect.centery-y<5: self.speed[1] = 0
           if self.rect.centery <= y :
              self.speed[1] = 3
              if y-self.rect.centery<5: self.speed[1] = 0
           self.rect.move_ip((self.speed[0], self.speed[1]))
           print ("hola")
    def rotar(self,arco):
           self.image = pygame.transform.rotate(self.image,arco)
           self.posterior = pygame.transform.rotate(self.posterior,arco)
           self.rect.centerx+=40
           self.rect.centery-=40

# ------------------------------
# Funcion principal del juego
# ------------------------------


def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("DIGIMON TCG")
    tablero1 = pygame.image.load(os.path.join(main_dir, 'Imagenes', "tablero.jpeg")).convert_alpha()
    image_tablero1 = pygame.transform.rotate(tablero1,90)
    tablero1 = pygame.transform.scale(image_tablero1, (500, 700))
    intermedio= pygame.transform.scale(pygame.image.load(os.path.join(main_dir, 'Imagenes', "fondo.jpg")).convert_alpha(), (200, 700))
    tablero2 = pygame.image.load(os.path.join(main_dir, 'Imagenes', "tablero.jpeg")).convert_alpha()
    image_tablero2 = pygame.transform.rotate(tablero2,-90)
    tablero2 = pygame.transform.scale(image_tablero2, (500, 700))
    carta_jugador1=list()
    carta_jugador2=list()
    #cartas de la mano del jugador1
    for i in range(5):
       carta_jugador1.append(Carta(100,500-30*i,'jugador1'))
    #cartas de seguridad del jugador 1
    for i in range(5,10):
       carta_jugador1.append(Carta(400+20*(5-i),80,'jugador1'))
    #cartas de digihuevo del jugador 1
    for i in range(10,14):
       carta_jugador1.append(Carta(100,100-5*(10-i),'jugador1'))
    #cartas del deck del jugador1
    for i in range(14,50):
       carta_jugador1.append(Carta(400+0.5*(14-i),620+0.5*(14-i),'jugador1'))

    #cartas de la mano del jugador2
    for i in range(5):
       carta_jugador2.append(Carta(1100,350-30*i,'jugador2'))
    #cartas de seguridad del jugador2
    for i in range(5,10):
       carta_jugador2.append(Carta(800-20*(5-i),620,'jugador2'))
    #cartas de digihuevo del jugador2
    for i in range(10,14):
       carta_jugador2.append(Carta(1100,600+5*(10-i),'jugador2'))
    #cartas del deck del jugador2
    for i in range(14,50):
       carta_jugador2.append(Carta(800-0.5*(14-i),80-0.5*(14-i),'jugador2'))

    clock = pygame.time.Clock()
    #Indicamos el fondo
    pygame.display.flip() 
    mover=0
    rotar=0
    angulo=-90
    # el bucle principal del juego
    while True:
	#60FPS
        clock.tick(60)
        if mover==1:
           carta_jugador1[0].mover(400,200)
        if rotar==1:
           carta_jugador1[0].rotar(angulo)
           angulo=angulo*-1
           rotar=0
        #Movemos la carta
        screen.blit(tablero1, (SCREEN_WIDTH/2+100, 0))
        screen.blit(intermedio, (500, 0))
        screen.blit(tablero2, (0, 0))
        for i in range(5):	
           screen.blit(carta_jugador1[i].image, carta_jugador1[i].rect)
        for i in range(5,50):	
           screen.blit(carta_jugador1[i].posterior, carta_jugador1[i].rect)
        for i in range(5):	
           screen.blit(carta_jugador2[i].image, carta_jugador2[i].rect) 
        for i in range(5,50):	
           screen.blit(carta_jugador2[i].posterior, carta_jugador2[i].rect)  
        pygame.display.flip()   
        # Posibles entradas del teclado y mouse	
       	for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                   mover=1
                elif event.button == 3:
                   rotar=1         


if __name__ == "__main__":
    main()
