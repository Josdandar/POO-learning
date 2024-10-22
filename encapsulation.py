class Persona:
    def __init__(self, nombre,edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    

jose = Persona("Josee", 30)

nombre = jose.get_nombre()
print(nombre)
jose.set_nombre("shokocrispis")
nombre = jose.get_nombre()
print(nombre)


