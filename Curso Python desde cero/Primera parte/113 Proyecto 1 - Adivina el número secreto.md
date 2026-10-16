# Proyecto #1 - Adivina e número

Desarrollar un juego interactivo llamado **"Adivina el número secreto"**

El programa seleccionará aleatoriamente un número entre un rango especificado y el jugador deberá adivinar el "número secreto" en un número limitado de intentos.

Requisitos
1. Seleccionar un número aleatorio entre 1 y 100.
2. El jugador tiene 10 intentos para adivinar el número.
3. El programa debe indicar si el número introducido es mayor o menor al número secreto.
4. Mostrar cuántos intentos le quedan al jugador.
5. Al finalizar el juego, mostrar un mensaje indicando si adivinó el número o no.
6. Si adivina el número, mostrar en qué intento lo logró.
7. Si se agotan los intentos, mostrar el número secreto.
8. El programa debe permitir volver a jugar.

Requerimientos indispensables:
* El programa debe contener un manejo de expresiones que evite errores ante entradas no validas del usuario (ej: letras, números decimales, etc).
  
Extensión (Opcional)
- Guardar un registro de las mejores puntuaciones.
- Implementar diferentes niveles de dificultad con rangos de números y cantidad de intentos variables.
- Incluir un sistema de pistas.
- Permitir jugar con números negativos.

Ejemplo de salida cuando adivina el número:

```python
# ¡Bienvenido al juego Adivina el número!
# He pensado en un número entre 0 y 100. ¿Puedes adivinarlo?
# Tienes 10 intentos para adivinar el número.
#
# Intento 1/10
# Ingresa un número: 50
# El número secreto es mayor.
#
# Intento 2/10
# Ingresa un número: 75
# El número secreto es menor.
# 
# Intento 3/10
# Ingresa un número: 62
# El número secreto es menor.
# 
# Intento 4/10
# Ingresa un número: 56
# El número secreto es menor.
# 
# Intento 5/10
# Ingresa un número: 53
# El número secreto es menor.
# 
# Intento 6/10
# Ingresa un número: 52
# El número secreto es menor.
# 
# Intento 7/10
# Ingresa un número: 52
# El número secreto es menor.
# 
# Intento 8/10
# Ingresa un número: 51
# ¡Felicidades! Has adivinado el número secreto 51 en 8 intentos
```

Ejemplo de salida cuando **NO** adivina el número:

```python
# ¡Bienvenido al juego Adivina el número!
# He pensado en un número entre 0 y 100. ¿Puedes adivinarlo?
# Tienes 10 intentos para adivinar el número.
# 
# Intento 1/10
# Ingresa un número: 1
# El número secreto es mayor.
#
# Intento 2/10
# Ingresa un número: 1
# El número secreto es mayor.
#
# Intento 3/10
# Ingresa un número: 1
# El número secreto es mayor.
#
# Intento 4/10
# Ingresa un número: 1
# El número secreto es mayor.
#
# Intento 5/10
# Ingresa un número: 1
# El número secreto es mayor.
#
# Intento 6/10
# Ingresa un número: 1
# El número secreto es mayor.
#
# Intento 7/10
# Ingresa un número: 1
# El número secreto es mayor.
# 
# Intento 8/10
# Ingresa un número: 1
# El número secreto es mayor.
# 
# Intento 9/10
# Ingresa un número: 1
# El número secreto es mayor.
# 
# Intento 10/10
# Ingresa un número: 1
# El número secreto es mayor.
# 
# Lo siento, has agotado tus intentos. El número secreto era 67
```

Ejemplo de salida cuando ingresa datos no validos:

```python
# ¡Bienvenido al juego Adivina el número!
# He pensado en un número entre 0 y 100. ¿Puedes adivinarlo?
# Tienes 10 intentos para adivinar el número.
# 
# Intento 1/10
# Ingresa un número: hola
# Error: Debes ingresar un número entero.
# 
# Intento 2/10
# Ingresa un número: 50
# El número secreto es menor.
# 
# Intento 3/10
# Ingresa un número: ñ
# Error: Debes ingresar un número entero.
# 
# Intento 4/10
# Ingresa un número: 25
# El número secreto es menor.
# 
# Intento 5/10
# Ingresa un número: 12
# El número secreto es mayor.
#
# Intento 6/10
# Ingresa un número: 18
# El número secreto es mayor.
#
# Intento 7/10
# Ingresa un número: 21
# El número secreto es mayor.
#
# Intento 8/10
# Ingresa un número: gls   
# Error: Debes ingresar un número entero.
# 
# Intento 9/10
# Ingresa un número: 23
# El número secreto es mayor.
#
# Intento 10/10
# Ingresa un número: 24
# ¡Felicidades! Has adivinado el número secreto 24 en 10 intentos
```

> Se recomienda realizar el ejercicio por cuenta propia, sin el uso de la Inteligencia Artificial y con todo el conocimiento adquirido hasta el momento.
> 
> La respuesta a este ejercicio se tratara en la clase presencial.