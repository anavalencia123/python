def generar_tabla_del_multiplicar(numero):
    for i in range(1,11):
        print (f"{numero}x{i}={numero*i}")

numero = int (input("ingrese el numero quedese multiplicar : "))
generar_tabla_del_multiplicar(numero)