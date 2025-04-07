class Animal:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre 
        self.especie = especie  
        self.edad = edad  

    def hacer_sonido(self):
        return f"{self.nombre} hace un sonido."

if __name__ == "__main__":
    perro = Animal("Rex", "Perro", "5 anios")
    print(perro.hacer_sonido()) 
    print(f"Nombre: {perro.nombre}, Especie: {perro.especie}, Edad: {perro.edad}")