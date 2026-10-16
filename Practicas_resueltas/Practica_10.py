ciclos = int(input(">> ¿Cuantos números enteros contendrá la lista?: "))
lista = []

for _ in range(ciclos):
    numero = int(input(">> Introduce un número entero: "))
    lista.append(numero)

print(f"Lista: {lista}")
print(f"La suma total es: {sum(lista)}")



