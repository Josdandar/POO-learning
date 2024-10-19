class Animal:
    def comer(self):
        print("El animal esta comiendo")

class Ave(Animal):
    def volar(self):
        print("El animal esta voland")

class Mamifero(Animal):
    def amamantar(self):
        print("El animal esta amamantando")

class Murcielado(Mamifero, Ave):
    pass

murcielago = Murcielado()

murcielago.comer()
murcielago.volar()
murcielago.amamantar()