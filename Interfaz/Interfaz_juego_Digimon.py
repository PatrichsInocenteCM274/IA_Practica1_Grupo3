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
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()


class Carta(pygame.sprite.Sprite):
    
    def __init__(self,x,y,jugador):
        pygame.sprite.Sprite.__init__(self)
        self.nombre_carta=choice(Nombres_digimones)
        self.imagen_original=pygame.image.load(os.path.join(main_dir, 'Imagenes', str(self.nombre_carta)+'.png')).convert_alpha()
        self.carta_grande = pygame.transform.scale(self.imagen_original, (200, 320))
        self.jugador=jugador
        if self.jugador=='jugador1':
            image_carta = pygame.transform.rotate(self.imagen_original,-90)
            image_posterior=pygame.transform.rotate(pygame.image.load(os.path.join(main_dir, 'Imagenes', 'reverso.jpg')).convert_alpha(),-90)
        if self.jugador=='jugador2':
            image_carta = pygame.transform.rotate(self.imagen_original,90)
            image_posterior=pygame.transform.rotate(pygame.image.load(os.path.join(main_dir, 'Imagenes', 'reverso.jpg')).convert_alpha(),90)
        self.image = pygame.transform.scale(image_carta, (160,100 ))
        self.posterior=pygame.transform.scale(image_posterior, (160,100 ))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed=[1,1]
    def mover(self,x,y,cursor):
        
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
    def rotar(self,arco,cursor):
        if cursor.colliderect((self.rect.left,self.rect.centery+20,160,30)):
           self.image = pygame.transform.rotate(self.image,arco)
           self.posterior = pygame.transform.rotate(self.posterior,arco)

    def update(self,cursor,screen):
        if cursor.colliderect((self.rect.left,self.rect.centery+20,160,30)):
           screen.blit(self.carta_grande, (500,250))
           return True
        else: 
           return False
           
# ------------------------------
# Funcion principal del juego
# ------------------------------


def main():
    pygame.init()
    #creamos el cursor que es un rectangulo que sigue al puntero
    cursor1=Cursor()
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
    coordenadas_ataque_jugador1=[[400,200],[400,320],[400,440],[300,280],[300,400]]
    coordenadas_ataque_jugador2=[[800,200],[800,320],[800,440],[900,280],[900,400]]
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
    numero_carta = [False,False,False,False,False]
    carta_elegida=-1
    carta_sombreada=-1
    jugador1=False
    jugador2=False
    # el bucle principal del juego
    while True:
	#60FPS    
        clock.tick(60)
        cursor1.update()
        if mover==1:
           if(jugador1):
              carta_jugador1[carta_elegida].mover(coordenadas_ataque_jugador1[carta_elegida][0],coordenadas_ataque_jugador1[carta_elegida][1],cursor1)
           if(jugador2):
              carta_jugador2[carta_elegida].mover(coordenadas_ataque_jugador2[carta_elegida][0],coordenadas_ataque_jugador2[carta_elegida][1],cursor1)
        if rotar==1:
           for i in range(5):
              carta_jugador1[i].rotar(angulo,cursor1)
              carta_jugador2[i].rotar(angulo,cursor1)
              angulo=angulo*-1
              rotar=0
        #Movemos la carta
        screen.blit(tablero1, (SCREEN_WIDTH/2+100, 0))
        screen.blit(intermedio, (500, 0))
        screen.blit(tablero2, (0, 0))
        
        for i in range(5):
           if(carta_jugador1[i].update(cursor1,screen)): 
              carta_sombreada=i	
              jugador1=True
              jugador2=False
           screen.blit(carta_jugador1[i].image, carta_jugador1[i].rect)
        for i in range(5,50):	
           screen.blit(carta_jugador1[i].posterior, carta_jugador1[i].rect)


        for i in range(5):
           if(carta_jugador2[i].update(cursor1,screen)): 
              carta_sombreada=i
              jugador1=False
              jugador2=True	
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
                   carta_elegida=carta_sombreada
                   mover=1
                elif event.button == 3:
                   rotar=1   
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                   mover=0       


if __name__ == "__main__":
    main()
