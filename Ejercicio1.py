num1 = int(input("Introduce un número entero: "))
num2 = int(input("Introduce un número entero mayor que el anterior: "))
while num1 > num2 or num1 == num2:
    print("Error. El primer número introducido es mayor o igual que el segundo. El segundo número siempre ha de ser mayor que el primero.")
    num1 = int(input("Introduce nuevamente un número entero: "))
    num2 = int(input("Introduce nuevamente un número entero mayor que el anterior: "))
suma = 0
for var in range(num1,num2+1):
    suma = suma + var
print("Realizando suma de todos los enteros comprendidos entre ambos números incluidos ellos.")
print("El resultado es", suma)