from personaje import Personaje
from campesino import Campesino
from soldado import Soldado

soldado1 = Soldado(100, 0, 20, 50)
campesino1 = Campesino(20, 10, 10, 50)
soldado2 = Soldado(100, -10, 20, 40)
campesino2 = Campesino(20, -20, 10, 60)


soldado1.atacar(soldado2)
soldado1.atacar(soldado2)

soldado1.mover("Derecha")
print(soldado1.posicion)

print("El campesino 1 ha cosechado:", campesino1.cosechar())
print("El campesino 2 ha cosechado:", campesino2.cosechar())