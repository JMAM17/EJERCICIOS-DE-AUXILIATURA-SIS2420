# CREAR UNA FUNCION QUE RECIBA UN NUMERO Y RETORNE SI ES PRIMO O NO 
def is_prime(n):
    """Return True if n is a prime number, else False."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    number = int(input("Ingrese un número: "))
    if is_prime(number):
        print(f"{number} es un número primo.")
    else:
        print(f"{number} no es un número primo.")