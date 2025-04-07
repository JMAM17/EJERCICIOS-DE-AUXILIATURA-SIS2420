def main():
    entrada = input("Ingrese números separados por comas: ")
    try:
        numeros = [float(num.strip()) for num in entrada.split(',')]
    except ValueError:
        print("Error: Ingrese solo números separados por comas.")
        return
    
    if not numeros:
        print("Error: No se ingresaron números.")
        return
    
    suma = sum(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    pares = sum(1 for num in numeros if num % 2 == 0)
    impares = len(numeros) - pares
    
    
    print("\nResultados:")
    print(f"- Suma total: {suma}")
    print(f"- Número mayor: {maximo}")
    print(f"- Número menor: {minimo}")
    print(f"- Cantidad de pares: {pares}")
    print(f"- Cantidad de impares: {impares}")

if __name__ == "__main__":
    main()