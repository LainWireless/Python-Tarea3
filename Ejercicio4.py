cont = 1
suma = 0
num = float(input("Introduce un número: "))
suma = suma + num
while cont<10 and suma<=100:
    num = float(input("Introduce otro número: "))
    cont = cont+1
    suma = suma + num
if cont == 10:
    print("Se paró el programa porque introduciste el máximo de cifras permitidas.")
elif suma > 100:
    print("Se paró el programa porque la suma de todas las cifras es mayor que 100.")
print("Se han introducido",cont,"cifras y la suma total es de",suma)
