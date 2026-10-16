# Nota de tutor: En esta nota se inducira a los alumnos a la declaración de variables en una sola linea.

# Secuencia de Fibonacci

# Ejemplo 1:

x, y = 0, 1

print("\nFinobacci, ejemplo 1:")
while x <= 1597:
    print (x, end = " ")
    x, y = y, x + y

# Ejemplo 2:

x, y = 0, 1

print("\n\nFinobacci, ejemplo 2:")
while y <= 1597:
    print (x, y, end = " ")
    x += y
    y += x

