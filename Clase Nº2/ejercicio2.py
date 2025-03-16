# PEDIR 5 NUMEROS Y GUARDARLOS EN UNA LISTA E IMPRIMIR LA SUMA Y EL PROMEDIO
def main():
    numbers = []
    
    for i in range(5):
        while True:
            try:
                number = float(input(f"Ingrese el número {i + 1}: "))
                numbers.append(number)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    
    total = sum(numbers)
    average = total / len(numbers)
    
    print(f"Suma: {total}")
    print(f"Promedio: {average}")

if __name__ == "__main__":
    main()