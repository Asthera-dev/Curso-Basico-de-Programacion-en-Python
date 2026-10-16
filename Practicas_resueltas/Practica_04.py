from os import system

def clear():
    system("cls")

def validation():
    while True:
        try:
            numero = float(input('>> Introduce un número: '))
            return numero
        except ValueError:
            print('>> Error: Debes introducir un número. <<\n')
            continue

menu = """Calculadora con una sola variable

********************
* Menú de opciones *
********************
1. Suma
2. Resta
3. Multiplicación
4. División
5. División entera
6. Exponente
7. Modulo o resto
"""

clear()
while True:
    try:
        print(menu)
        numero = int(input('>> Introduce la opción deseada: '))
        if numero not in range(1,8):
            raise ValueError
        break
    except ValueError:
        clear()
        print('>> Error: Debes introducir un número entero dentro de las opciones. <<\n')
        continue

match numero:
    case 1:
        print("\n>> Seleccionaste Suma. <<")
        numero = validation()
        numero += validation()
        print("\n>> El resultado de la suma es: ", numero)
    case 2:
        print("\n>> Seleccionaste Resta. <<")
        numero = validation()
        numero -= validation()
        print("\n>> El resultado de la resta es: ", numero)
    case 3:
        print("\n>> Seleccionaste Multiplicación. <<")
        numero = validation()
        numero *= validation()
        print("\n>> El resultado de la multiplicación es: ", numero)
    case 4:
        print("\n>> Seleccionaste División. <<")
        numero = validation()
        numero /= validation()
        print("\n>> El resultado de la división es: ", numero)
    case 5:
        print("\n>> Seleccionaste División entera. <<")
        numero = validation()
        numero //= validation()
        print("\n>> El resultado de la división entera es: ", numero)
    case 6:
        print("\n>> Seleccionaste Exponente. <<")
        numero = validation()
        numero **= validation()
        print("\n>> El resultado del exponente es: ", numero)
    case 7:
        print("\n>> Seleccionaste Modulo o resto. <<")
        numero = validation()
        numero %= validation()
        print("\n>> El resultado del modulo es: ", numero)
