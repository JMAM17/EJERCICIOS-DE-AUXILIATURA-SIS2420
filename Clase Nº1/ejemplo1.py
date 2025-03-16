# SOLICITE DOS NUMEROS AL USUARIO Y MUESTRE SUMA,RESTA,MULTIPLICACION Y DIVISION
def main():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2 if num2 != 0 else "Error: División por cero"
        
        print(f"Suma: {suma}")
        print(f"Resta: {resta}")
        print(f"Multiplicación: {multiplicacion}")
        print(f"División: {division}")
        
    except ValueError:
        print("Por favor, ingrese números válidos.")

if __name__ == "__main__":
    main()