class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print("estudiando...")

    
nombre = input("Cual es tu nombre?: ")
edad = input("Cual es tu edad?: ")
grado = input("Cual es tu grado?: ")

estudiante = Estudiante(nombre, edad, grado)
print(estudiante.nombre)
while True: 
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()