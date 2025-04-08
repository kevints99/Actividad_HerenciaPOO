# Clase base Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

# Clase derivada Estudiante
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)  # Reutiliza el constructor de Persona
        self.grado = grado

    def imprimir_grado(self):
        print(f"Grado: {self.grado}")

# Crear una instancia de Estudiante
estudiante1 = Estudiante("Kevin Tapia", 20, "11°")

# Imprimir atributos y métodos
estudiante1.imprimir_info()
estudiante1.imprimir_grado()
