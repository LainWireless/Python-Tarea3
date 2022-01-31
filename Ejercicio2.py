num = int(input("Introduce un número entero positivo: "))
while num < 0:
    print("Error. Has introducido un número negativo. Introduce uno positivo.")
    num = int(input("Introduce un número entero positivo: "))
valor = 0
cont = 1
menor = 0
mayor = 0
valor = valor+int(num)
mayor = mayor+int(num)
menor = menor+int(num)
while num!= 0:
    while num < 0:
        print("Error. Has introducido un número negativo. Introduce uno positivo.")
        num = int(input("Introduce un número entero positivo o 0 para terminar: "))
        if num > 0:
            valor = valor+int(num)    
            cont = cont+1
        elif num > mayor:
            mayor = num
        elif num < menor and num > 0:
            menor = num
    while num > 0:
        num = int(input("Introduce otro número entero positivo o 0 para terminar: "))
        if num > 0:
            valor = valor+int(num)    
            cont = cont+1
        elif num > mayor:
            mayor = num
        elif num < menor and num > 0:
            menor = num
media = valor/cont
print("Se han introducido",cont,"números.")
print("El mayor número introducido ha sido",mayor)
print("El menor número introducido ha sido",menor)
print("La media de todos los números es",media)