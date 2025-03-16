# PEDIR NUMEROS HASTA QUE SE INGRESE UN NUMERO NEGATIVO
def main():
    while True:
        try:
            number = float(input("Ingrese un número (negativo para salir): "))
            if number < 0:
                print("Número negativo ingresado. Saliendo...")
                break
            else:
                print(f"Número ingresado: {number}")
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()