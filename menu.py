import pygame
import numpy as np
from PIL import Image
import sys
import os
from game import game


myDir = os.getcwd()
sys.path.append(myDir) 


def credit():
    '''
    Nombre Funcion : credit
    Llamado: credi().
    Descripcion
        -Crea la ventana y carga en esta la imagen que corresponde a los creditos
        -Tiene el boton para regresar al menu.
    '''
    I = Image.open("recursos/fondos/creditos/creditos.png")
    pygame.init()
    
    ventana = pygame.display.set_mode(I.size)
    principal_img = pygame.image.load("recursos/fondos/creditos/creditos.png")
    ventana.blit(principal_img,(0,0))
    
    pygame.display.update()

    while True:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                pygame.quit()
            if eventos.type==pygame.MOUSEBUTTONDOWN:
                (x,y) = pygame.mouse.get_pos()
                if x>=987 and y>=580 and x<=1294 and y<=734:
                    menu()



def menu():
    '''
    Nombre Funcion : menu
    Llamado: menu().
    Descripcion: 
            -Crea una ventana y carga la imagen correspondiente.
            -Controla los botones para jugar, ver los creditos o salir. 
            -Carga musica de fondo para el menu
        
    '''
    I = Image.open("recursos/fondos/principal/fondo.png")

    pygame.init()
    ventana = pygame.display.set_mode(I.size)
    principal_img = pygame.image.load("recursos/fondos/principal/fondo.png")
    ventana.blit(principal_img,(0,0))
    pygame.mixer.music.load('recursos/musica/menu.mp3')#Fuente: https://opengameart.org/content/dream-raid-cinematic-action-soundtrack

    pygame.mixer.music.play(-1)

    pygame.display.update()

    while True:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                pygame.quit()
            if eventos.type==pygame.MOUSEBUTTONDOWN:
                (x,y) = pygame.mouse.get_pos()
                if x>=987 and y>=580 and x<=1294 and y<=734:
                    sys.exit()
                if x>=558 and y>=580 and x<=867 and y<=734:
                    credit()
                if x>=104 and y>=580 and x<=408 and y<=734:
                    pygame.mixer.music.pause()
                    game()
                    menu()
if __name__ == '__main__':
    menu()