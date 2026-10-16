cadena = input(">>> Ingrese una cadena de texto: ")
eliminar = input(">>> Ingrese la cadena a eliminar: ").lower()

indice = cadena.find(eliminar)
salida = cadena[0:indice]+ cadena[indice+len(eliminar): ]

print(salida)