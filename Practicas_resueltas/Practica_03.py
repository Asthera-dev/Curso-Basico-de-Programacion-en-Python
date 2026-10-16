from os import system

system("cls")
menu = """*******************************************************************************
* Programa para determinar ¿Cual es el número más grande de los tres números? *
*******************************************************************************
"""
print (menu)

while True:
    try:
        num1 = float(input(">> Ingrese el número 1: "))
        num2 = float(input(">> Ingrese el número 2: "))
        num3 = float(input(">> Ingrese el número 3: "))
        break
    except ValueError:
        print("Error: Por favor ingrese solo números")

if num1 > num2:
#    print(f"\n>> El número '{num1}' es el más grande de los tres <<\n" if num1 > num3 else f"\n>> El número '{num3}' es el más grande de los tres <<\n")
    if num1 > num3:
        print(f"\n>> El número '{num1}' es el más grande de los tres <<\n")
    else:
        print(f"\n>> El número '{num3}' es el más grande de los tres <<\n")
else:
#    print(f"\n>> El número '{num2}' es el más grande de los tres <<\n" if num2 > num3 else f"\n>> El número '{num3}' es el más grande de los tres <<\n")
    if num2 > num3:
        print(f"\n>> El número '{num2}' es el más grande de los tres <<\n")
    else:
        print(f"\n>> El número '{num3}' es el más grande de los tres <<\n")
