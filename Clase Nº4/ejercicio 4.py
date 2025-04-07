class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_de_notas = []
    
    def agregar_nota(self, nota):
        self.lista_de_notas.append(nota)
    
    def promedio(self):
        if not self.lista_de_notas:
            return 0
        return sum(self.lista_de_notas) / len(self.lista_de_notas)
    
    def mostrar_informacion(self):
        print(f"Estudiante: {self.nombre}")
        print(f"Notas: {self.lista_de_notas}")
        print(f"Promedio: {self.promedio()}")

if __name__ == "__main__":
    e1 = Estudiante("Carlos")
    e1.agregar_nota(80)
    e1.agregar_nota(95)
    print(f"Promedio: {e1.promedio()}")