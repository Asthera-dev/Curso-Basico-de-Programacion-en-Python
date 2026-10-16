"""
Proyecto #4 - Conversor de entero a romano

Crea un programa que permita convertir un número entero a su equivalente en números romanos, con las siguientes especificaciones:

* El programa deberá solicitar al usuario que ingrese un número entero.
* El programa solo aceptara números enteros en un rango entre 1 y 3999.
"""

# Solicitamos al usuario que ingrese un número valido

while True:
    try:
        numero = int(input(">> Ingrese un numero entero entre 1 y 3999: "))
        # Verificamos que el número este dentro del rango establecido
        if numero < 1 or numero > 3999:
            print("\n¡Error! El numero debe estar entre 1 y 3999.\n")
            continue
        else:
            break
    except ValueError:
        print("\n¡Error! Debe ingresar un numero valido.")
        continue

# Creamos la logica del programa

# Creamos listas con los numeros romanos en cada posicion
M = ["", "M", "MM", "MMM"]
C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
D = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
U = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

# Utilizamos operaciones matematicas para obtener el valor en cada posicion y lo concatenamos para formar el numero romano
print(f"\n>>> El numero {numero} en numeros romanos es:\n{M[numero // 1000]}{C[(numero % 1000) // 100]}{D[(numero % 100) // 10]}{U[numero % 10]}")