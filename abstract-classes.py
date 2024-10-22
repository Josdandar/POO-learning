from abc import ABC, abstractmethod

# Clase abstracta Persona
class Persona(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método abstracto
    @abstractmethod
    def descripcion(self):
        pass

# Clase Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    # Implementación del método abstracto
    def descripcion(self):
        return f"{self.nombre}, de {self.edad} años, es un estudiante de {self.carrera}."

# Clase Trabajador que hereda de Persona
class Trabajador(Persona):
    def __init__(self, nombre, edad, trabajo):
        super().__init__(nombre, edad)
        self.trabajo = trabajo

    # Implementación del método abstracto
    def descripcion(self):
        return f"{self.nombre}, de {self.edad} años, trabaja como {self.trabajo}."


estudiante = Estudiante("Johan", 23, "Ingeniería de Software")
trabajador = Trabajador("Gael", 20, "Desarrollador Full Stack")

print(estudiante.descripcion())  
print(trabajador.descripcion())  
