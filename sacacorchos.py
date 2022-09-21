from corcho import Corcho
from botella import Botella

class Sacacorchos:

    def __init__(self):
        self.corcho = None


    def destapar(self, botella):
        self.corcho = botella.corcho #referencia al corcho sacado
        botella.corcho = None

    def limpiar(self):
        self.corcho = None


corcho1 = Corcho("bodega_de_migue")
botella1 = Botella(corcho1)
sacacorchos1 = Sacacorchos()

print("Corcho de botella1: ", botella1.corcho)
print("Corcho de sacacorchos1: ", sacacorchos1.corcho)
print("---DESTAPAR---")
sacacorchos1.destapar(botella1)
print("Corcho de botella1: ", botella1.corcho)
print("Corcho de sacacorchos1: ", sacacorchos1.corcho)
print("---LIMPIAR---")
sacacorchos1.limpiar()
print("Corcho de botella1: ", botella1.corcho)
print("Corcho de sacacorchos1: ", sacacorchos1.corcho)