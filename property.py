class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property  # Acceso como si fuera una propiedad, sin necesidad de paréntesis.
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre  # Corrección para usar la variable de instancia adecuada.

    @nombre.deleter
    def nombre(self):
        del self.__nombre

# Creación del objeto y uso de las propiedades
jose = Persona("Jose", 30)
print(jose.nombre)  # Usamos el getter de nombre.

jose.nombre = "Pepe"  # Usamos el setter de nombre.
print(jose.nombre)  # Comprobamos que el nombre ha sido cambiado.
