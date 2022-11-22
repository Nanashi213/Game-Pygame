import pygame



class Enemigo():
    '''
    Nombre Clase: Enemigo

    Descripcion: Representar un enemigo.

    Llamado:Enemigo(ventana,pos_x,pos_y,velo,sprit).

    Atributos: 
                ventana:ventana en donde se usa el enemigo.
                pos_x:posicion en x inicial.
                pos_y:posicion en y inicial.
                velocidad: velocidad con la que se mueve.
                cuentaPasose: Variable que recorre la lista de sprites.


    '''

    def __init__(self,ventana,pos_x,pos_y,velo,sprit) -> None:
        self.ventana=ventana
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.velo = velo
        self.cuentaPasose =0
        self.anim_caminar = sprit 
    
    def movimiento(self,final,inicio):

        '''
        Metodo: movimiento
        Descripcion: Realiza la animacion de caminar del enemigo 
        Parametros: 
                    final:Indica las coordenada donde va desaparecer el enemigo.
                    inicio:Indica las coordenadas donde comienza el enemigo.
                    
        '''
        self.ventana.blit(pygame.transform.flip(self.anim_caminar[self.cuentaPasose//1],True,False), (self.pos_x, self.pos_y))
        self.pos_x -= self.velo-1
        self.cuentaPasose = self.cuentaPasose + 1

        if self.cuentaPasose > len(self.anim_caminar)-1:
            self.cuentaPasose = 0
        if self.pos_x < -final:
            self.pos_x = inicio

    

    def choque(self,cir_per):
        '''
        Metodo: choque
        Descripcion: Revisa el choque entre la figura que representa el enemigo y la que representa un personaje
        Parametros: 
                    cir_per: figura que representa a un personje.  
        '''
        self.cir_z = pygame.draw.circle(self.ventana,(0,0,255),(self.pos_x+40,self.pos_y+50),20)
        if cir_per.colliderect(self.cir_z):
            return True
