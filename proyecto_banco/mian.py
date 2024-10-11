
usuarios = {
    "usuarios":{"contrasenia":"1234","salfdo":10000},
    "usuarios2":{"contrasenia":"1264","salfdo":10000},
    "usuarios3":{"contrasenia":"1274","salfdo":10000},
    "usuarios4":{"contrasenia":"1238","salfdo":10000},
    "usuarios5":{"contrasenia":"1235","salfdo":10000},
}
def autenticarUsuario(nombre,contrasenia):
    usuario = usuarios.get(nombre)
    if usuario and usuario.get("contrasenia") == contrasenia:
        return usuario
    return False

def consultarSaldo(usuario):
    return usuario.get("saldo")
def retirarDinero(usuario, cantidad):   
    if cantidad > 0:
        if usuario.get("salfdo") >= cantidad:
            usuario["saldo"] -= cantidad
            return f"Se ha retirado ${cantidad} de tu cuenta"
        return "Fondos insuficientes"
    return "saldo insufiente"

def depositarDinero(usuario, cantidad):
    if cantidad > 0:
        usuario["salfdo"] += cantidad
        return f"Se ha depositado ${cantidad} en tu cuenta"
    return "La cantidad a depositar debe ser mayor a 0"

#funcion para cambiar la contrasenia
def cambiarContrasenia(usuario):
    cantraseñaActual = input("Ingresa tu contrasenia actual")
    if cantraseñaActual == usuario.get("contrasenia"):
        nuevaContrasenia = input("Ingresa tu nueva contrasenia")
        usuario["contrasenia"] = nuevaContrasenia
        return ()
    return False
# creacios de menu que va permitir auntentificar si el usuario esta creado y luego de auntentificar me va permirir revisar las opciones de cajero
def menu():
    while True:
        nombre = input("Ingresa tu nombre de usuario :")
        if nombre.lower == "exit":
            break
        contrasenia = input("Ingresa tu contrasenia")
        auntentificado = autenticarUsuario(nombre,contrasenia)
        if  not auntentificado:
            print("Usuario no auntentificado")
            continue
        print("Bienvenido al cajero")
        while True:
            print("-----Menu-----")
            print("1. Consultar saldo")
            print("2. Retirar")
            print("3. Depositar")
            print("4. cambiaer contrasenia")
            print("5. Salir")
            print("-------------")
            try:
                op = int(input("Ingresa una opcion: "))
                if op == 1:
                    print(f"Tu saldo es de ${consultarSaldo(auntentificado)}")
                elif op == 2:
                    cantidad = float(input("Ingresa la cantidad a retirar"))
                    print(retirarDinero(auntentificado,cantidad))
                elif op == 3:
                    cantidad = float(input("Ingresa la cantidad a depositar"))
                    print(depositarDinero(auntentificado,cantidad))
                elif op == 4:
                    print(cambiarContrasenia(auntentificado))
                elif op == 5:
                    break
            except as e:
                print("Opcion no valida")    
                print(e)       
menu()
