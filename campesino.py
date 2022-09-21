from personaje import Personaje

class Campesino(Personaje):
    def __init__(self, vida, posicion, velocidad, cosecha):
        super().__init__(vida, posicion, velocidad)
        self.cosecha = cosecha
    def cosechar(self):
        return self.cosecha