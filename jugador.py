import pygame

        


class Jugador():
    '''
    Nombre Clase: Jugador

    Descripcion: Representar al jugador.

    Llamado:Jugador(ventana,pos_x,pos_y,velocidad).

    Atributos: 
                ventana:ventana en donde se usa el personake.
                pos_x:posicion en x inicial.
                pos_y:posicion en y inicial.
                velocidad: velocidad con la que se mueve.
                cuentaPasose: Variable que recorre la lista de sprites.
                salto: si esta en salto o no .
                direccion: si esta mirando hacia la derecha o izquierda
                caminar: lista de imagenes de caminar.
                salto: lista de imagenes de saltar.

    '''
    def __init__(self,ventana,pos_x,pos_y,velocidad) -> None:
        self.ventana=ventana
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.velocidad = velocidad
        self.cuentaPasos = 0
        self.salto=False #En salto True
        self.direccion = True # True - derecha, False Izquierda
        self.cuentaSalto = 10
        self.caminar = [pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (1).png'),(100,100)),
                        pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (2).png'),(100,100)),
                        pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (3).png'),(100,100)),
                        pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (4).png'),(100,100)),
                        pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (5).png'),(100,100)),
                        pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (6).png'),(100,100)),
                        pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (7).png'),(100,100)),
                        pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (8).png'),(100,100)),
                        pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (9).png'),(100,100)),
                        pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (10).png'),(100,100)),
                        pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (11).png'),(100,100)),
                        pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (12).png'),(100,100)),
                        pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (13).png'),(100,100)),
                        pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (14).png'),(100,100)),
                        pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Walk (15).png'),(100,100))]

        self.salta=[pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (1).png'),(100,100)),
                    pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (2).png'),(100,100)),
                    pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (3).png'),(100,100)),
                    pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (4).png'),(100,100)),
                    pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (5).png'),(100,100)),
                    pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (6).png'),(100,100)),
                    pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (7).png'),(100,100)),
                    pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (8).png'),(100,100)),
                    pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (9).png'),(100,100)),
                    pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (10).png'),(100,100)),
                    pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (11).png'),(100,100)),
                    pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (12).png'),(100,100)),
                    pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (13).png'),(100,100)),
                    pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (14).png'),(100,100)),
                    pygame.transform.scale(pygame.image.load('recursos/sprites/jugador/Jump (15).png'),(100,100))]



    def movimiento(self):
        '''
        Metodo: movimiento
        Descripcion:  realiza la animacion de caminar o saltar del personaje y controla la velociad  
        '''
                # Movimiento a la derecha
        if self.direccion:
            self.ventana.blit(self.caminar[self.cuentaPasos//1], (self.pos_x, self.pos_y))
        # Movimiento a la izquierda
        if not self.direccion:
            self.ventana.blit(pygame.transform.flip(self.caminar[self.cuentaPasos//1],True,False), (self.pos_x, self.pos_y))
        # Movimiento de salto
        if self.salto:
            if self.cuentaSalto >= -10:
                self.pos_y -= (self.cuentaSalto * abs(self.cuentaSalto)) * 0.5
                self.ventana.blit(self.salta[self.cuentaPasos // 1], (self.pos_x, self.pos_y))
                self.cuentaSalto -= 1
            else:
                self.cuentaSalto = 10
                self.salto = False

        # Contador de pasos
        
        # Opción tecla pulsada
        keys = pygame.key.get_pressed()

        
        # Tecla SPACE - Salto
        if not self.salto:
            if keys[pygame.K_UP]:
                self.salto = True
                self.direccion = None
                self.cuentaPasos = 0

        
        if self.cuentaPasos > len(self.caminar)-2:
            self.cuentaPasos = 0
        
        # Tecla - Moviemiento a la izquierda
        elif keys[pygame.K_LEFT] :
            self.velocidad=-7
            self.direccion = False
            self.cuentaPasos += 1

        # Tecla - Moviemiento a la derecha
        elif keys[pygame.K_RIGHT] :
            self.velocidad=4
            self.direccion = True
            self.cuentaPasos += 1
        # Personaje quieto
        else:
            self.direccion = True
            self.cuentaPasos += 1
            self.velocidad= -4



