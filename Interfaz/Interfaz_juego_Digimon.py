#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ---------------------------
# Importacion de los módulos
# ---------------------------
from rdflib import URIRef, BNode, Literal
from rdflib import Namespace
from rdflib.namespace import RDF, RDFS, OWL
from rdflib import ConjunctiveGraph
import pygame, random, os, sys
from pygame.locals import *
from random import choice
import time
# Creacion del Grafo
grafomon = ConjunctiveGraph()

#Ingreso de URIRef
Gigimon_BT2_001 = URIRef('https://example.org/Card/BT2-001')
DemiVeemon_BT2_002 = URIRef('https://example.org/Card/BT2-002')
Nyaromon_BT2_003 = URIRef('https://example.org/Card/BT2-003')
Argomon_BT2_004 = URIRef('https://example.org/Card/BT2-004')
Poromon_BT3_001 = URIRef('https://example.org/Card/BT3-001')
DemiVeemon_BT3_002 = URIRef('https://example.org/Card/BT3-002')
Upamon_BT3_003 = URIRef('https://example.org/Card/BT3-003')
Minomon_BT3_004 = URIRef('https://example.org/Card/BT3-004')
Kakkinmon_BT3_005 = URIRef('https://example.org/Card/BT3-005')
DemiMeramon_BT3_006 = URIRef('https://example.org/Card/BT3-006')
GranKuwagamon_BT1_083 = URIRef('https://example.org/Card/BT1-083')
Biyomon_BT2_010 = URIRef('https://example.org/Card/BT2-010')
Vorvomon_BT2_011 = URIRef('https://example.org/Card/BT2-011')
Birdramon_BT2_012 = URIRef('https://example.org/Card/BT2-012')
Lavorvomon_BT2_014 = URIRef('https://example.org/Card/BT2-014')
Garudamon_BT2_015 = URIRef('https://example.org/Card/BT2-015')
Lavogaritamon_BT2_016 = URIRef('https://example.org/Card/BT2-016')
Phoenixmon_BT2_019 = URIRef('https://example.org/Card/BT2-019')
Veemon_BT2_021 = URIRef('https://example.org/Card/BT2-021')
Betamon_BT2_022 = URIRef('https://example.org/Card/BT2-022')
Gomamon_BT2_023 = URIRef('https://example.org/Card/BT2-023')
Seadramon_BT2_024 = URIRef('https://example.org/Card/BT2-024')
Ikkakumon_BT2_025 = URIRef('https://example.org/Card/BT2-025')
Veedramon_BT2_026 = URIRef('https://example.org/Card/BT2-026')
Zudomon_BT2_027 = URIRef('https://example.org/Card/BT2-027')
AeroVeedramon_BT2_028 = URIRef('https://example.org/Card/BT2-028')
MegaSeadramon_BT2_029 = URIRef('https://example.org/Card/BT2-029')
Vikemon_BT2_031 = URIRef('https://example.org/Card/BT2-031')
UlforceVeedramon_BT2_032 = URIRef('https://example.org/Card/BT2-032')
Agumon_BT2_033 = URIRef('https://example.org/Card/BT2-033')
Salamon_BT2_034 = URIRef('https://example.org/Card/BT2-034')
GeoGreymon_BT2_035 = URIRef('https://example.org/Card/BT2-035')
Gatomon_BT2_036 = URIRef('https://example.org/Card/BT2-036')
Angewomon_BT2_037 = URIRef('https://example.org/Card/BT2-037')
RizeGreymon_BT2_038 = URIRef('https://example.org/Card/BT2-038')
Ophanimon_BT2_040 = URIRef('https://example.org/Card/BT2-040')
ShineGreymon_BT2_041 = URIRef('https://example.org/Card/BT2-041')
GloriousBurst_BT2_099 = URIRef('https://example.org/Card/BT2-099')
PuppetPummel_BT2_100 = URIRef('https://example.org/Card/BT2-100')
CherryBlast_BT2_101 = URIRef('https://example.org/Card/BT2-101')
ADelicatePlan_BT3_097 = URIRef('https://example.org/Card/BT3-097')
PlasmaStake_BT3_098 = URIRef('https://example.org/Card/BT3-098')
WeHavetoStopFighting_BT3_099 = URIRef('https://example.org/Card/BT3-099')
DeathParadeBlaster_BT3_100 = URIRef('https://example.org/Card/BT3-100')
Bifrost_BT3_101 = URIRef('https://example.org/Card/BT3-101')
CodeCracking_BT3_102 = URIRef('https://example.org/Card/BT3-102')
HiddenPotentialDiscovered_BT3_103 = URIRef('https://example.org/Card/BT3-103')
PositronLaser_BT3_104 = URIRef('https://example.org/Card/BT3-104')
BreathOfTheGods_BT3_105 = URIRef('https://example.org/Card/BT3-105')
BeastCyclone_BT3_106 = URIRef('https://example.org/Card/BT3-106')
DarkDespair_BT3_108 = URIRef('https://example.org/Card/BT3-108')
Necrophobia_BT3_110 = URIRef('https://example.org/Card/BT3-110')
Craniamon_BT3_075 = URIRef('https://example.org/Card/BT3-075')
Candlemon_BT3_076 = URIRef('https://example.org/Card/BT3-076')
Gazimon_BT3_077 = URIRef('https://example.org/Card/BT3-077')
Shamanmon_BT3_078 = URIRef('https://example.org/Card/BT3-078')
Saberdramon_BT3_080 = URIRef('https://example.org/Card/BT3-080')
BlackGatomon_BT3_082 = URIRef('https://example.org/Card/BT3-082')
Meramon_BT3_083 = URIRef('https://example.org/Card/BT3-083')
SkullMeramon_BT3_085 = URIRef('https://example.org/Card/BT3-085')
Arukenimon_BT3_086 = URIRef('https://example.org/Card/BT3-086')
Mummymon_BT3_087 = URIRef('https://example.org/Card/BT3-087')
LadyDevimon_BT3_088 = URIRef('https://example.org/Card/BT3-088')
Mastemon_BT3_090 = URIRef('https://example.org/Card/BT3-090')
MaloMyotismon_BT3_092 = URIRef('https://example.org/Card/BT3-092')
ImperialdramonDragonMode_BT3_111 = URIRef('https://example.org/Card/BT3-111')
OmnimonAlter_S_BT3_112 = URIRef('https://example.org/Card/BT3-112')
RinaShinomiya_BT2_086= URIRef('https://example.org/Card/BT2-086')
DavisMotomiya_BT3_093 = URIRef('https://example.org/Card/BT3-093')
KenIchijoji_BT3_094 = URIRef('https://example.org/Card/BT3-094')
JoeKido_BT3_095 = URIRef('https://example.org/Card/BT3-095')
MimiTachikawa_BT3_096 = URIRef('https://example.org/Card/BT3-096')
ScrapClaw_BT1_091 = URIRef('https://example.org/Card/BT1-091')
BraveShield_BT1_095 = URIRef('https://example.org/Card/BT1-095')
Argomon_BT2_042 = URIRef('https://example.org/Card/BT2-042')
Argomon_BT2_045 = URIRef('https://example.org/Card/BT2-045')
Argomon_BT2_047 = URIRef('https://example.org/Card/BT2-047')
Argomon_BT2_050 = URIRef('https://example.org/Card/BT2-050')
BlackWarGreymon_BT2_112 = URIRef('https://example.org/Card/BT2-112')
Agumon_BT3_007 = URIRef('https://example.org/Card/BT3-007')
Zubamon_BT3_008 = URIRef('https://example.org/Card/BT3-008')
Hawkmon_BT3_009 = URIRef('https://example.org/Card/BT3-009')
ZubaEagermon_BT3_010 = URIRef('https://example.org/Card/BT3-010')
Greymon_BT3_011 = URIRef('https://example.org/Card/BT3-011')
Aquilamon_BT3_012 = URIRef('https://example.org/Card/BT3-012')
Duramon_BT3_013 = URIRef('https://example.org/Card/BT3-013')
Silphymon_BT3_014 = URIRef('https://example.org/Card/BT3-014')
MetalGreymon_BT3_015 = URIRef('https://example.org/Card/BT3-015')
Durandamon_BT3_016 = URIRef('https://example.org/Card/BT3-016')
Valkyrimon_BT3_017 = URIRef('https://example.org/Card/BT3-017')
BlitzGreymon_BT3_018 = URIRef('https://example.org/Card/BT3-018')
RagnaLoardmon_BT3_019 = URIRef('https://example.org/Card/BT3-019')
Patamon_BT3_020 = URIRef('https://example.org/Card/BT3-020')
Veemon_BT3_021 = URIRef('https://example.org/Card/BT3-021')
Penguinmon_BT3_022 = URIRef('https://example.org/Card/BT3-022')
Angemon_BT3_023 = URIRef('https://example.org/Card/BT3-023')
Airdramon_BT3_024 = URIRef('https://example.org/Card/BT3-024')
ExVeemon_BT3_025 = URIRef('https://example.org/Card/BT3-025')
MagnaAngemon_BT3_026 = URIRef('https://example.org/Card/BT3-026')
Paildramon_BT3_027 = URIRef('https://example.org/Card/BT3-027')
Bastemon_BT3_028 = URIRef('https://example.org/Card/BT3-028')
Goldramon_BT3_029 = URIRef('https://example.org/Card/BT3-029')
Imperialdramon_Dragon_Mode_BT3_031 = URIRef('https://example.org/Card/BT3-031')
Armadillomon_BT3_032 = URIRef('https://example.org/Card/BT3-032')
Salamon_BT3_033 = URIRef('https://example.org/Card/BT3-033')
Lopmon_BT3_034 = URIRef('https://example.org/Card/BT3-034')
Gatomon_BT3_035 = URIRef('https://example.org/Card/BT3-035')
Goldramon_BT3_029 = URIRef('https://example.org/Card/BT3-029')
Goldramon_BT3_029 = URIRef('https://example.org/Card/BT3-029')
Goldramon_BT3_029 = URIRef('https://example.org/Card/BT3-029')
Ankylomon_BT3_036 = URIRef('https://example.org/Card/BT3-036')
Turuiemon_BT3_037 = URIRef('https://example.org/Card/BT3-037')
Antylamon_BT3_038 = URIRef('https://example.org/Card/BT3-038')
Angewomon_BT3_039 = URIRef('https://example.org/Card/BT3-039')
Shakkoumon_BT3_040 = URIRef('https://example.org/Card/BT3-040')
Cherubimon_BT3_041 = URIRef('https://example.org/Card/BT3-041')
ClavisAngemon_BT3_042 = URIRef('https://example.org/Card/BT3-042')
Aruraumon_BT3_044 = URIRef('https://example.org/Card/BT3-044')
Kunemon_BT3_045 = URIRef('https://example.org/Card/BT3-045')
Terriermon_BT3_046 = URIRef('https://example.org/Card/BT3-046')
Wormmon_BT3_047 = URIRef('https://example.org/Card/BT3-047')
Gargomon_BT3_048 = URIRef('https://example.org/Card/BT3-048')
Flymon_BT3_049 = URIRef('https://example.org/Card/BT3-049')
Stingmon_BT3_050 = URIRef('https://example.org/Card/BT3-050')
Dokugumon_BT3_051 = URIRef('https://example.org/Card/BT3-051')
Rapidmon_BT3_052 = URIRef('https://example.org/Card/BT3-052')
JewelBeemon_BT3_053 = URIRef('https://example.org/Card/BT3-053')
Blossomon_BT3_054 = URIRef('https://example.org/Card/BT3-054')
Dinobeemon_BT3_055 = URIRef('https://example.org/Card/BT3-055')
Ceresmon_BT3_056 = URIRef('https://example.org/Card/BT3-056')
MegaGargomon_BT3_057 = URIRef('https://example.org/Card/BT3-057')
BanchoStingmon_BT3_058 = URIRef('https://example.org/Card/BT3-058')
Commandramon_BT3_059 = URIRef('https://example.org/Card/BT3-059')
Psychemon_BT3_060 = URIRef('https://example.org/Card/BT3-060')
Ludomon_BT3_062 = URIRef('https://example.org/Card/BT3-062')
Sukamon_BT3_063 = URIRef('https://example.org/Card/BT3-063')
TiaLudomon_BT3_064 = URIRef('https://example.org/Card/BT3-064')
Gururumon_BT3_065 = URIRef('https://example.org/Card/BT3-065')
Clockmon_BT3_066 = URIRef('https://example.org/Card/BT3-066')
Tankmon_BT3_067 = URIRef('https://example.org/Card/BT3-067')
Giromon_BT3_068 = URIRef('https://example.org/Card/BT3-068')
RaijiLudomon_BT3_069 = URIRef('https://example.org/Card/BT3-069')
Etemon_BT3_070 = URIRef('https://example.org/Card/BT3-070')
MetalMamemon_BT3_071 = URIRef('https://example.org/Card/BT3-071')
BryweLudramon_BT3_072 = URIRef('https://example.org/Card/BT3-072')
CresGarurumon_BT3_073 = URIRef('https://example.org/Card/BT3-073')
GraceCrossFreezer_BT1_100 = URIRef('https://example.org/Card/BT1-100')
HowlingCrusher_BT1_101 = URIRef('https://example.org/Card/BT1-101')
TiaLudomon_BT1_102 = URIRef('https://example.org/Card/BT1-102')
Testament_BT1_103 = URIRef('https://example.org/Card/BT1-103')
HolyWave_BT1_107 = URIRef('https://example.org/Card/BT1-107')
VolcanicFlare_BT2_091 = URIRef('https://example.org/Card/BT2-091')
ArcticBlizzard_BT2_094 = URIRef('https://example.org/Card/BT2-094')
TheRayOfVictory_BT2_096 = URIRef('https://example.org/Card/BT2-096')
LightningPaw_BT2_097 = URIRef('https://example.org/Card/BT2-097')
EDENsJavelin_BT2_098 = URIRef('https://example.org/Card/BT2-098')

#URIRef de Características Generales
name = URIRef('https://example.org/characteristic/name')
costo_entrada = URIRef('https://example.org/characteristic/costo_entrada')
numero_carta = URIRef('https://example.org/characteristic/numero_carta')
poder_digimon = URIRef('https://example.org/characteristic/poder_digimon')
requerimiento_evolucion_nivel = URIRef('https://example.org/characteristic/requerimiento_evolucion_nivel')
requerimiento_evolucion_costo = URIRef('https://example.org/characteristic/requerimiento_evolucion_costo')
efecto = URIRef('https://example.org/characteristic/efecto')
efecto_seguridad = URIRef('https://example.org/characteristic/efecto_seguridad')
efecto_digievolucion = URIRef('https://example.org/characteristic/efecto_digievolucion')
nivel = URIRef('https://example.org/characteristic/nivel')
tipo=URIRef('https://example.org/characteristic/tipo')

# -----------
# Constantes
# -----------
main_dir = os.path.split(os.path.abspath(__file__))[0]
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
Nombres_digimones = []
archivo = open('digimon_lista.txt', 'r')
for linea in archivo:
    #print (linea)
    Nombres_digimones.append(linea.strip())
archivo.close()

#-----------------------------------------
# Creación de Funciones Propias del Grafo
#-----------------------------------------

def palabraEfecto(d, x):
  data2 = [efecto,efecto_seguridad,efecto_digievolucion]
  for i in range (3):
    if (grafomon.value(d,data2[i])!=None and x in grafomon.value(d,data2[i]) and grafomon.value(d,efecto)!=None):
      return True
    else:
      return False

def ataque(x,y):
    for s,p,o in grafomon.triples((x, poder_digimon, None)): 
        name1 = grafomon.value(s,name)
        poder1 = o
    for s,p,o in grafomon.triples((y, poder_digimon, None)):
        name2 = grafomon.value(s,name)
        poder2 = o
    
    print(name1 + " ataca a " + name2)

    if  int(poder2) > int(poder1):
        if(palabraEfecto(x,'Jamming')):
            print(name2, " va a la pila de basura")
        else:
            print(name1,"y",name2, " van a la pila de basura")

    if  int(poder1) > int(poder2):
        print(name2, " va a la pila de basura")

def traeNodo(x):
    mon = x.split("_")
    stringmon = ""
    for i in range (0,len(mon)-2):
     if i==len(mon)-3 :
      stringmon = stringmon + mon[i]
     else :
      stringmon = stringmon + mon[i] + " "
    for s in grafomon.transitive_subjects(name, Literal(stringmon)):
     if (grafomon.value(s, efecto)!=None):
      return s

def tipos(x):
  for s in grafomon.transitive_objects(x, RDF.type):
    print(grafomon.value(s, name))


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
           
    def rotar(self,arco,cursor,carta_seguridad,objeto_seguridad):
     if cursor.colliderect((self.rect.left,self.rect.centery+20,160,30)):
      ataque(traeNodo(self.nombre_carta),traeNodo(carta_seguridad))
      self.image = pygame.transform.rotate(self.image,arco)
      self.posterior = pygame.transform.rotate(self.posterior,arco)
      objeto_seguridad.voltear_carta()
      
    def update(self,cursor,screen):
        if cursor.colliderect((self.rect.left,self.rect.centery+20,160,30)):
           screen.blit(self.carta_grande, (500,200))
           return True
        else: 
           return False
    def voltear_carta(self):
       self.posterior=self.image
           
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
    image_memoria1 = pygame.image.load(os.path.join(main_dir, 'Imagenes', "memoria1.jpg")).convert_alpha()
    memoria1=pygame.transform.scale(image_memoria1, (200, 130))
    image_memoria2 = pygame.image.load(os.path.join(main_dir, 'Imagenes', "memoria2.jpg")).convert_alpha()
    image_memoria2= pygame.transform.rotate(image_memoria2,180)
    memoria2=pygame.transform.scale(image_memoria2, (200, 130))
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
        screen.blit(intermedio, (500, 0))
        screen.blit(memoria1,(500, 0))
        screen.blit(memoria2,(500,580))
        screen.blit(tablero2, (0, 0))
        screen.blit(tablero1, (SCREEN_WIDTH/2+100, 0))
        if mover==1:
           if(jugador1):
              carta_jugador1[carta_elegida].mover(coordenadas_ataque_jugador1[carta_elegida][0],coordenadas_ataque_jugador1[carta_elegida][1],cursor1)
           if(jugador2):
              carta_jugador2[carta_elegida].mover(coordenadas_ataque_jugador2[carta_elegida][0],coordenadas_ataque_jugador2[carta_elegida][1],cursor1)
        if rotar==1:
           for i in range(5):
              carta_jugador1[i].rotar(angulo,cursor1,carta_jugador2[9].nombre_carta,carta_jugador2[9])
              carta_jugador2[i].rotar(angulo,cursor1,carta_jugador1[9].nombre_carta,carta_jugador1[9])
              angulo=angulo*-1
              rotar=0
       

        
        for i in range(10):
           if(carta_jugador1[i].update(cursor1,screen)): 
              carta_sombreada=i	
              jugador1=True
              jugador2=False
           screen.blit(carta_jugador1[i].image, carta_jugador1[i].rect)
        for i in range(5,50):	
           screen.blit(carta_jugador1[i].posterior, carta_jugador1[i].rect)


        for i in range(10):
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
    grafomon.parse("digimon(4).rdf", format="xml")
    main()
