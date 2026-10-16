from os import ftruncate
frutas = {"manzana": 5,
          "peras": 2,
          "naranjas": 4}

# Reto 1
print(">>Reto 1")
print(f"(Imprimiendo con frutas['manzana']): Existen {frutas['manzana']} mazanas")
print(f"[Imprimiendo con .get()]             Existen {frutas.get('manzana')} mazanas")

# Reto 2
print("\n>>Reto 2")
print(f"Diccionario original: {frutas}")
frutas["bananas"] = 5
frutas.setdefault("mangos", 6)
frutas["uvas"] = 3
print("Agregando nuevos valores")
print(f"Diccionario modificado: {frutas}")

# Reto 3
frutas = {"manzana": 5,
          "peras": 2,
          "naranjas": 4}

print("\n>>Reto 3")
eliminado =frutas.pop("peras")

print(f"Dicionario original: {frutas}")
print(f"Eliminamo 'peras' con el metodo pop: {eliminado}")
print(f"Dicionario modificado: {frutas}")


frutas = {"manzana": 5,
          "peras": 2,
          "naranjas": 4}

print(f"\nDicionario original: {frutas}")
del frutas["peras"]
print(f"Dicionario modificado con 'del': {frutas}")

# Reto 4
frutas = {"manzana": 5,
          "peras": 2,
          "naranjas": 4}

print("\n>>Reto 4")

print(f"Keys con el método list(frutas.keys()): {list(frutas.keys())}")
print(f"Values con el método list(frutas.values()): {list(frutas.values())}")

# Reto 5
print("\n>>Reto 5")

frutas = {"uva": 5,
          "peras": 2,
          "naranjas": 4}

if "manzana" in frutas:
    print("True")
else:
    print("False")