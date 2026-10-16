from os import system

system("cls")
menu = ("""******************************************************
* Programa que determina si un número es par o impar *
******************************************************
""")
print(menu)
while True:
    try:
        numero = int(input(">> Ingrese un número entero: "))
        break
    except ValueError:
        system("cls")
        print(f"\n>> ERROR: El valor ingresado no es un número entero. Intente nuevamente. << \n")
        print(menu)

if numero % 2 == 0:
    print(f"\n>> El número {numero} es par. <<\n")
else:
    print(f"\n>> El número {numero} es impar. <<\n")
