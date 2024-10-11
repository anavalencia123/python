numero1 = float(input("ingrese el numero 1 : "))
numero2 = float(input("ingrese el numero 2 : "))

if numero1 <numero2:
    print(f"numero {numero1} y numoro {numero2} son iguales")
elif numero1 > numero2:
    print(" numero {numero1} es amyor a {numero2} ")
else:
    print("numoro1 no es mayor que numero2")

estudiante = "ana"
nota = float(input("ingresa la nota : "))
nota = round(nota)
if nota >= 60 and nota <= 100:
    print(f"{estudiante}  aprobo ")
elif nota >= 0 and nota <= 60: 
    print("reprobo")
else: 
    print("no es valida")



