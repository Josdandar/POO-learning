class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad

    def saludar(self):
        print(f'Mi nombre es {self.nombre} y tengo {self.edad}')


class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad) #Al usar super no se pasa self como parametro
        self.grado = grado

    def mostrar_grado(self):
        print(f'Mi grado es {self.grado}')

etudiante = Estudiante("Koku", 100, "7mo")

etudiante.saludar()
etudiante.mostrar_grado()