import pygame
import numpy as np
from PIL import Image
from enemigos import Enemigo
from jugador import Jugador
import random


''' CARGA DE LOS SPRITES'''

sprit_zombi = [pygame.transform.scale(pygame.image.load('recursos/sprites/female_ene/Walk (1).png'),(100,100)),
pygame.transform.scale(pygame.image.load('recursos/sprites/female_ene/Walk (2).png'),(100,100)),
pygame.transform.scale(pygame.image.load('recursos/sprites/female_ene/Walk (3).png'),(100,100)),
pygame.transform.scale(pygame.image.load('recursos/sprites/female_ene/Walk (4).png'),(100,100)),
pygame.transform.scale(pygame.image.load('recursos/sprites/female_ene/Walk (5).png'),(100,100)),
pygame.transform.scale(pygame.image.load('recursos/sprites/female_ene/Walk (6).png'),(100,100)),
pygame.transform.scale(pygame.image.load('recursos/sprites/female_ene/Walk (7).png'),(100,100)),
pygame.transform.scale(pygame.image.load('recursos/sprites/female_ene/Walk (8).png'),(100,100)),
pygame.transform.scale(pygame.image.load('recursos/sprites/female_ene/Walk (9).png'),(100,100)),
pygame.transform.scale(pygame.image.load('recursos/sprites/female_ene/Walk (10).png'),(100,100))]

sprit_zombi2 = [pygame.transform.scale(pygame.image.load('recursos/sprites/male_ene/Walk (1).png'),(100,100)),
pygame.transform.scale(pygame.image.load('recursos/sprites/male_ene/Walk (2).png'),(100,100)),
pygame.transform.scale(pygame.image.load('recursos/sprites/male_ene/Walk (3).png'),(100,100)),
pygame.transform.scale(pygame.image.load('recursos/sprites/male_ene/Walk (4).png'),(100,100)),
pygame.transform.scale(pygame.image.load('recursos/sprites/male_ene/Walk (5).png'),(100,100)),
pygame.transform.scale(pygame.image.load('recursos/sprites/male_ene/Walk (6).png'),(100,100)),
pygame.transform.scale(pygame.image.load('recursos/sprites/male_ene/Walk (7).png'),(100,100)),
pygame.transform.scale(pygame.image.load('recursos/sprites/male_ene/Walk (8).png'),(100,100)),
pygame.transform.scale(pygame.image.load('recursos/sprites/male_ene/Walk (9).png'),(100,100)),
pygame.transform.scale(pygame.image.load('recursos/sprites/male_ene/Walk (10).png'),(100,100))]


sprit_avion = [pygame.transform.scale(pygame.image.load('recursos/sprites/aereo/Fly (1).png'),(80,80)),
pygame.transform.scale(pygame.image.load('recursos/sprites/aereo/Fly (2).png'),(80,80)),
pygame.transform.scale(pygame.image.load('recursos/sprites/aereo/Shoot (1).png'),(80,80)),
pygame.transform.scale(pygame.image.load('recursos/sprites/aereo/Shoot (2).png'),(80,80)),
pygame.transform.scale(pygame.image.load('recursos/sprites/aereo/Shoot (3).png'),(80,80)),
pygame.transform.scale(pygame.image.load('recursos/sprites/aereo/Shoot (4).png'),(80,80)),
pygame.transform.scale(pygame.image.load('recursos/sprites/aereo/Shoot (5).png'),(80,80))]




def game():
    '''
    Nombre Funcion : game
    Llamado: game().
    Descripcion
        -Crea la ventana del juego y pone la imagen inicial de presionar espacio para jugar
        -Crea los objetos relacionados con el personaje y sus enemigos
        -Mantiene el juego en funcionamiento mientras no este en game over generando el movimiento del fondo y 
        llamando a las funciones correspondientes del personaje y enemigos para su movimiento 
        -imprime el puntaje actual
        -Carga musica del fondo durante el juego
        
    '''
    I = Image.open("recursos/fondos/Jugar/jugarP.png")
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()

    fuenteletra = pygame.font.SysFont('Eras Bold ITC',45)

    pygame.mixer.music.load('recursos/musica/airship.flac') #Fuente: https://opengameart.org/content/airship-song-orchestral-remix
    
    principal_img = pygame.image.load("recursos/fondos/Jugar/jugarP.png")
    fondo = pygame.image.load("recursos/fondos/Jugar/jugar.png")
    ventana = pygame.display.set_mode(I.size)
    ventana.blit(principal_img,(0,0))
    pygame.display.set_caption('Play')
    pygame.display.update()
    inicia=True
    game_over=True
    clock=pygame.time.Clock()


    #Imagen inicial de presicion espacio para empezar
    while inicia:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inicia=False
            if event.type == pygame.KEYDOWN:
                if  event.key == pygame.K_SPACE:
                    pos_pantalla=0
                    game_over=False
                    inicia=False
                    game_over=False
                    pygame.mixer.music.play(-1)


    pygame.display.update()
    pygame.display.flip()

    jugador = Jugador(ventana,94,335,5)
    zombi = Enemigo(ventana,900,340,5,sprit_zombi) 
    avion = Enemigo(ventana,1500,178,5,sprit_avion) 
    zombi2 = Enemigo(ventana,1250,340,5,sprit_zombi2) 

    pos_pantalla=0
    velocidad_de_fondo=2

    puntaje=0


    while not game_over:
         
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over=True  
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    game_over=True  
                
        if jugador.pos_x <0:
            game_over=True

        #Movimiento de la pantalla
        x_relativa = pos_pantalla % fondo.get_rect().width
        ventana.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
        if x_relativa < 999:
            ventana.blit(fondo, (x_relativa, 0))
        pos_pantalla -= velocidad_de_fondo

        #Animacion de los enemigos
        final =random.randint(100, 300)
        inicio =random.randint(1030,1150 )
        zombi.movimiento(final,inicio)
        zombi2.movimiento(final,inicio)
        avion.movimiento(final,inicio)
        

        #Revisa si los enemigo estan muy juntos
        if abs(zombi.pos_x - avion.pos_x)<80:
            avion.pos_x-=80
        if abs(zombi2.pos_x - avion.pos_x)<80:
            avion.pos_x-=80
        if abs(zombi.pos_x - zombi2.pos_x)<80:
            avion.pos_x-=80
        
        jugador.movimiento()        


        texto_puntajea=fuenteletra.render(str(int(puntaje*10)),1,(255,255,255)) 
        ventana.blit(texto_puntajea,(480,540))  
        puntaje+=0.1           

        pygame.display.update()
        pygame.display.flip()   

        clock.tick(20)  
        
        #Revision de choque del jugador con un enemigo
        cir_per = pygame.draw.circle(ventana,(0,0,255),(jugador.pos_x+40,jugador.pos_y+50),20)
        if zombi.choque(cir_per) == True:
            game_over = True
        if avion.choque(cir_per) == True:
            game_over = True

        jugador.pos_x += jugador.velocidad

    #Imprime texto de game over
    texto=fuenteletra.render(str("Game Over"),2,(255,0,0)) 
    ventana.blit(texto,(450,240))
    pygame.display.update() 
    for i in range(100):
        clock.tick(20)

     
    
    pygame.quit()






