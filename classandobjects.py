class Celular:
    def __init__(self, marca, modelo, camara): ###Metodo constructor de la clase 
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f'Estas haciendo un llamado desde un: {self.modelo}')

    def cortar(self):
        print(f'Cortaste la llamada desde tu: {self.modelo}')

    


iphone = Celular("Iphone", "15 Pro", "19MP") ###Atributos de instancia, se los pasamos cuando creamos el objeto

iphone.llamar()
    
###Las clases se nombran utilizando pascal case por buenas practicas