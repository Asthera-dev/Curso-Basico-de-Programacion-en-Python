Los operadores aritméticos son aquellos que "manipulan" datos numéricos, tanto números enteros, así como números decimales (también conocidos como reales).

Estos operadores son los más sencillos de todos, se utilizan para realizar operaciones aritméticas básicas, como son: Sumas, restas, multiplicaciones, divisiones, modulo o residuo y exponenciales .

Al igual que todos los lenguajes de programación, Python también cuenta con los siguientes operadores aritméticos:

* Suma ( + )
* Resta ( - )
* Multiplicación ( * )
* Exponente ( ** )
* Módulo ( % )
* División ( / )
* División entera ( // )

## Suma o adición

Es la reunión de dos o más conjuntos llamados "sumando" en un solo conjunto llamado " suma o total". Su signo en Python es (+) y se coloca entre los sumandos.

Realizar la suma entre dos números para observar su comportamiento:

```Python
print("suma:")
numero_uno = 5
numero_dos = 4
resultado = numero_uno + numero_dos

print("El resultado de la suma es: " + str(resultado))

# Salida: 9
```

## Resta o sustracción

Es la operación contraria a la suma, y también recibe el nombre de sustracción. La cual consiste en extraer o quitar de un número mayor otro menor. Su signo en Python es (-).

Continuando en el mismo script:

```Python
print("resta:")
numero_uno = 5
numero_dos = 4
resultado = numero_uno - numero_dos

print("El resultado de la resta es: " + str(resultado))

# Salida: 1
```

## Multiplicación

Es la operación matemática que consiste en hallar el resultado de sumar un número tantas veces como indique otro. Su signo en Python es ( * )

Continuando en el mismo script:

```Python
print("multiplicación:")
numero_uno = 5
numero_dos = 4
resultado = numero_uno * numero_dos

print("El resultado de la multiplicación es: " + str(resultado))

# Salida: 20
```

## Exponente o potencia

Es la operación matemática mediante la cual multiplicamos un número por si mismo las veces que nos indique el exponente. Su representación en Python es ( ** )

Continuando en el mismo script:

```Python
print("exponente:")
numero_uno = 2
exponente = 5
resultado = numero_uno ** exponente

print("El resultado del exponente es: " + str(resultado))

# Salida: 32
```

## División

Es una operación matemática que consiste en averiguar cuántas veces un número está contenido en otro número. Su signo en Python es ( / ).

Continuando en el mismo script:

```Python
print("división:")
numero_uno = 4
numero_dos = 2
resultado = numero_uno / numero_dos

print("El resultado de la división es: " + str(resultado))

# Salida: 2
```

## Módulo o resto

Es la cantidad que sobra después de efectuar una división, es decir, es el valor que se obtiene cuando un numero no puede ser dividido exactamente por otro. Su signo en Python es ( % )

Continuando en el mismo script:

```Python
print("modulo:")
numero_uno = 30
numero_dos = 8
resultado = numero_uno % numero_dos

print("El resultado del modulo es: " + str(resultado))

# Salida: 6
# Esto puede ser algo complicado de entender, pero veamoslo de la siguiente manera:

# Al dividir 30 entre 8 obtenemos 3.75.
# Es decir, el número 8 "cabe" 3 veces en el 30.

# Al multiplicar 8 por 3 obtenemos 24.

# El modulo son lo "números faltantes" para "llegar" a nuestro número.
# En este caso, a 24 le falta 6 para ser 30.

###################################################################################

print("modulo. Ejemplo 2:")
numero_uno = 35
numero_dos = 4
resultado = numero_uno % numero_dos

print("El resultado del modulo es: " + str(resultado))

# Salida: 3

# Debido a que:

# 35 entre 4 es: 8
# 8 por 4 son: 32

# 35 menos 32 es: 3     - Donde 3 es el modulo. -
```

## División entera

Es una operación que consiste en obtener el valor entero de un número, el cual resulte de una división entre dos números decimales o reales. Su representación en Python es ( // )

Continuando en el mismo script:

```Python
print("división entera:")
numero_uno = 4
numero_dos = 2
resultado = numero_uno // numero_dos

print("El resultado de la división entera es: " + str(resultado))

# Salida: 2

# La División entera, como su nombre indica, solo toma la parte entera de un número.

###################################################################################
print("división entera. Ejemplo 2:")
numero_uno = 35
numero_dos = 4
resultado = numero_uno // numero_dos

print("El resultado de la división entera es: " + str(resultado))

# Salida: 8

# Debido a que:

# 35 entre 4 es: 8.75

# La división entera solo toma el numero entero. Es decir, el número 8.
```

