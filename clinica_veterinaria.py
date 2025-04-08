# Clase base Animal
class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def imprimir_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")

# Clase derivada Perro
class Perro(Animal):
    def __init__(self, nombre, especie, raza):
        super().__init__(nombre, especie)  # Llama al constructor de Animal
        self.raza = raza

    def imprimir_raza(self):
        print(f"Raza: {self.raza}")

# Crear una instancia de Perro
perro1 = Perro("Firulais", "Canino", "Labrador")

# Imprimir atributos y métodos
perro1.imprimir_info()
perro1.imprimir_raza()
