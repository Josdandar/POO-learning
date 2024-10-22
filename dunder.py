class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        # Constructor que inicializa los atributos de nombre, fuerza y velocidad del personaje
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        # Método especial que define la representación del objeto para la depuración
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"

    def __add__(self, otro_pj):
        # Sobrecarga del operador + para fusionar dos personajes y crear uno nuevo
        # Combina los nombres
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        # Calcula la nueva fuerza como el promedio de las fuerzas de ambos personajes al cuadrado
        nueva_fuerza = ((self.fuerza + otro_pj.fuerza) / 2) ** 2
        # Calcula la nueva velocidad como el promedio de las velocidades de ambos personajes al cuadrado
        nueva_velocidad = ((self.velocidad + otro_pj.velocidad) / 2) ** 2
        # Retorna un nuevo objeto Personaje con el nombre fusionado, la nueva fuerza y velocidad
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

# Crear dos instancias de la clase Personaje
goku = Personaje("Goku", 100, 100)
vegeta = Personaje("Vegeta", 99, 99)

# Fusionar los personajes Goku y Vegeta utilizando la sobrecarga del operador +
gogeta = goku + vegeta

# Imprimir la representación de Gogeta
print(gogeta)
