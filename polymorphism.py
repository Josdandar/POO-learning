class Animal:
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "Guau guauu"

class Gato(Animal):
    def sonido(self):
        return "Miauuu"

def hacer_sonido(animal):
    print(animal.sonido())

# Crear instancias de Perro y Gato
dog = Perro()
cat = Gato()
