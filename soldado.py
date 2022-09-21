from personaje import Personaje

class Soldado(Personaje):
    
    def __init__(self, vida, posicion, velocidad, ataque):
        super().__init__(vida, posicion, velocidad)
        self.ataque = ataque
    
    def atacar(self, personaje):
        personaje.recibir_ataque(self.ataque)