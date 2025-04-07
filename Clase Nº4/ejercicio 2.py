numeros = []
num = 0
while num >= 0:
    num = int(input("Ingresa un número: "))
    if num >= 0:
        numeros =  numeros +[num]  
print("numeros positivos :", numeros)

sum = 0 
for i in range(5):
    numero = float(input("Ingresa un número: "))  
    sum = sum + numero 
promedio = sum / 5 
print("Suma:", sum)  
print("Promedio:", promedio)  

def veri(num):
    if num <= 1:
        return False 
    i = 2
    while i * i <= num: 
        if num % i == 0:
            return False  
        i += 1 
    return True  
num = int(input("Ingresa un número: "))
if veri(num):
    print( "es primo" ,num )
else:
    print(" no es primo" ,num )