dia = int(input("digite su fecha de nacimiento :"))
mes = int(input("digite su mes de nacimiento :"))

if mes > 12 or mes < 1  or dia < 1 or dia > 31:
    print("mes non valido")
elif (dia >=21 and mes ==3) or (dia <= 19 and mes == 4 ):
    print("aries")

else:
    print("no eres aries")
