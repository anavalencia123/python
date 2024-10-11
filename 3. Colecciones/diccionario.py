mi_diccionario = {
    "nombre":   "ana",
    "edad":     18,
    "ciudad":   "cali",
    "idiomas":  ["ingles","espaÃ±ol","frances"],
    "civil":   "soltera",
    "GrupoSanginio": None
}

#Acceder a un valor mediante su clave
print(mi_diccionario["nombre"]) #Salida: Juan David

#Modificar un valor
mi_diccionario["edad"] = 19

#Agregar un nuevo par de clave-valor
mi_diccionario["profesion"] = "Ingeniera"

#Eliminar un par de clave-valor
del mi_diccionario["ciudad"]
print(mi_diccionario)