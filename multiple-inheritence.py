class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Konichiwa")


class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
    def hablar(self):
        print("Tambien se puede sobreescribir a pesar de haber estado declarado antes")

class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f'Mi habilidad es {self.habilidad}' 

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa

    def mostrar_habilidad(self):
        print("No tengo lol")
              
    def presentarse(self):
        return f'{self.mostrar_habilidad()}'

roberto = EmpleadoArtista("Roberto", 43, "argentino","Cantar", "SWE", 99999999999)

roberto.presentarse()

###Como saber si una es subclase de otra, si hereda de otra 

inheritance = issubclass(EmpleadoArtista, Artista) ###Si hereda de artista
instance = isinstance(roberto, Artista) ###Si un objeto es una instancia de cierta clase
print(inheritance)
print(instance)