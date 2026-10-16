"""# Sintaxis para ciclo while con break

x = 0
while x < 10:
    print(x)
    x += 1

    if x == 5:
        break

# Sintaxis para ciclo while con continue

num = 0
while num < 15:
    num+=1
    if num == 10:
        continue
    print("El valor es",num)


num = 0"""


"""num = 0
while num <13 :
    num += 1

    if num % 2 == 0:
        continue

    print("El valor es:", num)


"""
"""numero = "40.5" 
print(numero.isdigit())"""

saludo = "Hola mundo"
print(saludo if saludo.istitle() else saludo.title())