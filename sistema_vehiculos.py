# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, anio):
        self.marca = marca
        self.anio = anio

    def imprimir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Año: {self.anio}")

# Clase derivada Coche
class Coche(Vehiculo):
    def __init__(self, marca, anio, modelo):
        super().__init__(marca, anio)  # Reutiliza el constructor de Vehiculo
        self.modelo = modelo

    def imprimir_modelo(self):
        print(f"Modelo: {self.modelo}")

# Crear una instancia de Coche
coche1 = Coche("Toyota", 2021, "Corolla")

# Imprimir atributos y métodos
coche1.imprimir_info()
coche1.imprimir_modelo()
