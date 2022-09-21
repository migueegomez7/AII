class Personaje:
    def __init__ (self,vida,posicion,velocidad):
        self.vida = vida
        self.posicion = posicion
        self.velocidad = velocidad


    def recibir_ataque(self,fuerza_ataque): #self se pone si vas a usar uno de los atributos de la clase
        self.vida -= fuerza_ataque
        if self.vida <= 0:
            print("ª")        


    def mover(self, direccion):
        if direccion == "Derecha":
            self.posicion += self.velocidad
        elif direccion == "Izquierda":
            self.posicion -= self.velocidad
        else:
            raise Exception("La direccion tiene que ser 'Derecha' o 'Izquierda'")
            