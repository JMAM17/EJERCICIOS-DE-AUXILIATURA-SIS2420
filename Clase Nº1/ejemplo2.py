# VERIFICAR SI ES PAR O IMPAR
def is_Par_or_Impar(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Impar"

if __name__ == "__main__":
    try:
        number = int(input("Ingrese un número: "))
        result = is_Par_or_Impar(number)
        print(f"{number} es {result}.")
    except ValueError:
        print("Por favor, ingrese un número válido.")