user = str("root")
passwd = str("1234")
intentos=2
usuario = (input("Usuario: "))
contraseña = (input("Contraseña: "))
while intentos>0 and user!=usuario and passwd!=contraseña:
    print ("El usuario y/o contraseña no coinciden. Le quedan",intentos,"intentos.")
    usuario = (str(input("Usuario: ")))
    contraseña = str(input("Contraseña: "))
    intentos=intentos-1
if user==usuario and passwd==contraseña:
    print("Bienvenido al sistema.")
else:
    print("Se ha superado el número de intentos permitido.")