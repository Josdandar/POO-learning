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

roberto = Empleado("Roberto", 43, "argentino", "SWE", 99999999999)

roberto.hablar()