def transponer_matriz(M):
   
    return [list(fila) for fila in zip(*M)]

if __name__ == "__main__":
    matriz_ejemplo = [[1, 2, 3], [4, 5, 6]]
    print(f"Matriz original: {matriz_ejemplo}")
    print(f"Matriz transpuesta: {transponer_matriz(matriz_ejemplo)}")
