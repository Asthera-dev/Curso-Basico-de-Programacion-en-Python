# Practica 9 (String sin vocales)

# ## Requerimientos indispensables:
# * Utilizar un ciclo o bucle, ya sea while o for
# * Considerar que el usuario puede ingresar vocales en mayúsculas y/o minúsculas.
# * Usar, por el momento, solo el conocimiento adquirido hasta esta clase.
# * No utilizar funciones prediseñadas (como replace)

# Inicio del programa

txt = "Hola Mundo" # input(">> Introduce una frase: ")
stop = "Z" # input(">> ¿Con que caracter deseas terminar el bucle?: ")

# Copias para trabajar en las otras versiones sin alterar la original

txt_2 = txt 
stop_2 = stop

txt_3 = txt
stop_3 = stop

# Versión 1 (Versión simple con los conocimientos adquiridos hasta el momento):
print("# Versión 1")

for character in txt:
    if character.lower() == stop.lower():
        break
    elif character.lower() == "a":
        continue
    elif character.lower() == "e":
        continue
    elif character.lower() == "i":
        continue
    elif character.lower() == "o":
        continue
    elif character.lower() == "u":
        continue
    print(character, end="")

print(f"\n{'='*30}\n")

# Versión 2 (Versión optimizada - limpia y "Pythonic"):
print("# Versión 2")

resultado_2 = ""
for caracter in txt_2:
    if caracter.lower() == stop_2.lower():
        break
    if caracter.lower() not in "aeiou":
        resultado_2 += caracter

print(resultado_2)

print(f"\n{'='*30}\n")

# Versión 3 (Versión con el ciclo while):
print("# Versión 3")

ciclos = len(txt_3)
vuelta = -1

while ciclos != 0:
    vuelta += 1
    ciclos -= 1
    if txt_3[vuelta] == (stop_3).lower() or txt_3[vuelta] == (stop_3).upper():
        break
    elif txt_3[vuelta] in "aeiouAEIOU":
        continue

    print(txt_3[vuelta], end="")

print(f"\n{'='*30}\n")
