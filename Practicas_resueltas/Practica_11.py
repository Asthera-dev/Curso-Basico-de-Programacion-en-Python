lista = ["A", "B", "b", "c", "E", "E", "f"]
salida = []
print(f"Lista disponible: {lista}")
eliminar = input(">> Introduce el elemento que deseas eliminar: ").lower()
for i in lista:
    if i.lower() == eliminar:
        continue
    salida.append(i)
    
for i in lista:
    if eliminar in lista:
        lista.pop(lista.index(eliminar))
    elif eliminar.upper() in lista:
        lista.pop(lista.index(eliminar.upper()))

print(f"Lista final: {lista}")
print(f"Lista final: {salida}")

