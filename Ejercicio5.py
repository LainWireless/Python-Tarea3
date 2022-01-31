cant = int(input("Introduzca cantidad de unidades vendidas: "))
if cant > 0:
    precio = float(input("Introduzca precio unitario del producto: "))
    while cant < 0 or precio < 0:
        print("Error. Has introducido un número negativo. Introduce uno positivo.")
        cant = int(input("Introduzca cantidad de unidades vendidas: "))
        precio = float(input("Introduzca precio unitario del producto: "))
    facturatotal = 0
    factura = cant * precio
    facturatotal = facturatotal + factura
    while cant!= 0:
        while cant < 0 or precio < 0:
            print("Error. Has introducido un número negativo. Introduce uno positivo.")
            cant = int(input("Introduzca cantidad de unidades vendidas del siguiente producto o 0 para finalizar: "))
            if cant > 0:
                precio = float(input("Introduzca precio unitario del nuevo producto: "))
                if cant > 0 and precio > 0:
                    factura = cant * precio
                    facturatotal = facturatotal + factura
        while cant > 0 and precio > 0:
            cant = int(input("Introduzca cantidad de unidades vendidas del siguiente producto o 0 para finalizar: "))
            if cant > 0:
                precio = float(input("Introduzca precio unitario del nuevo producto: "))
                if cant > 0 and precio > 0:
                    factura = cant * precio
                    facturatotal = facturatotal + factura
    print("El importe de su factura total es de",facturatotal,"€.")
