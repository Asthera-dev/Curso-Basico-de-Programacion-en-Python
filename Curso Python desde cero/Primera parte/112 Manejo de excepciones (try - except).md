# Manejo de excepciones

El manejo de excepciones en Python es una técnica fundamental que permite a los programadores controlar y gestionar situaciones imprevistas o errores durante la ejecución de un programa.

Las excepciones son eventos que interrumpen el flujo normal del programa.

El manejo de excepciones proporciona una forma elegante de anticipar, detectar y responder a estos eventos de manera controlada.

## ¿Cómo se ve una excepción?

Veámoslo con el siguiente programa:

```python
numero = int(input("ingresa un número: "))
resultado = 50 // numero

print(f"50 / {numero} = {resultado}")
```

Cuando el usuario ingresa un dato valido (un número), el programa funciona sin correctamente. Pero, ¿Qué pasa si ingresa un dato invalido como un String?:

```python
# Ejemplo de ejecución del programa:

# ingresa un número: hola
# Traceback (most recent call last):
#   File "<python-input-0>", line 1, in <module>
#     numero = int(input("ingresa un número: "))
#              ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'hola'
```

Como se observa, Python nos lanza un 'error', la excepción del inicio: 'ValueError' y, además, nuestro programa se detiene completamente.

Para encapsular y manejar errores, tenemos el conjunto de palabras reservadas **'try'**, **'except'**, **'else'** & **'finally'** con la siguiente sintaxis:

## Sintaxis (try - except)

```python
try:
	numero = int(input("ingresa un número: "))
	resultado = 50 // numero

	print(f"50 / {numero} = {resultado}")
except ValueError:
	print("Debes ingresar un número entero")
```

La palabra try debe ir al inicio de la parte del código que queremos encapsular y el código que queremos ejecutar va después de esta palabra, manteniendo la tabulación.

A continuación, viene la palabra except sin tabulación y con la excepción que queremos tratar (en este caso, ValueError) inmediatamente después de la palabra y con un espacio en blanco.

Después de esta segunda palabra reservada se coloca el código que se ejecutará si ocurre dicho tipo de excepción.

```python
# Ejemplo de ejecución del programa:

# ingresa un número: hola
# Debes ingresar un número entero
```

Se observa que el error ha sido controlado y nuestro código seguirá funcionando sin detenerse debido a las excepciones.

___

Cuando programamos, puede ocurrir que necesitemos incluir el error en nuestro programa sin que este mismo falle y se detenga, por lo tanto, podemos hacer lo siguiente:

```python
try:
	numero = int(input("ingresa un número: "))
	resultado = 50 // numero
	print(f"50 / {numero} = {resultado}")
	
except ValueError as ve:
	print(f"Debes ingresar un número entero. ValueError: {ve}")

# Ejemplo de ejecución del programa:

# ingresa un número: hola
# Debes ingresar un número entero. ValueError: invalid literal for int() with base 10: 'hola'
```

Como se observa, nuestra excepción fue contenida de manera correcta y, además, se mostró dentro de la impresión. Esto se logra con la secuencia de palabras:

```python
except excepción as variable:
```

Donde la 'excepción' puede ser de diferentes tipos como:
* ValueError
* KeyError
* ZeroDivisionError
* FileNotFoundError
* KeyboardInterrupt
* SystemExit
* etc.

Nosotros al colocar 'as' le indicamos al programa que almacene el error en la 'variable' que nosotros colocamos enseguida. Por buenas practicas, es recomendable que la variable se llame o posea un nombre que haga referencia a la excepción.

Esto es útil cuando se trabaja en equipo y se necesita depurar líneas de código u optimizarlo.

___

Es importante mencionar que en, un mismo bloque de código, podemos tener más de una excepción:

```python
try:
	numero = int(input("ingresa un número: "))
	resultado = 50 // numero

	print(f"50 / {numero} = {resultado}")
except ValueError as ve:
	print(f"Debes ingresar un número entero. ValueError: {ve}")

# Ejemplo de ejecución del programa:

# ingresa un número: 0
# Traceback (most recent call last):
#   File "<python-input-3>", line 3, in <module>
#     resultado = 50 // numero
#                 ~~~^^~~~~~~~
#ZeroDivisionError: integer division or modulo by zero
```

Se observa que ahora Python nos ha marcado un erro por dividir un número entre cero.
Para corregir más de una excepción a la vez, podemos escribir la cantidad de 'except' que necesitemos: 

```python
try:
	numero = int(input("ingresa un número: "))
	resultado = 50 // numero

	print(f"50 / {numero} = {resultado}")
except ValueError as ve:
	print(f"Debes ingresar un número entero. ValueError: {ve}")

except ZeroDivisionError as zde:
	print(f"No puedes dividir por cero. ZeroDivisionError: {zde}")

# Ejemplo de ejecución del programa:

# ingresa un número: 0
# No puedes dividir por cero. ZeroDivisionError: integer division or modulo by zero
```

Pero, ¿Y si no conozco la excepción que pueda ocurrir?

Para esto, Python contiene la excepción 'Exception' que controla **LA MAYORIA** de las excepciones al mismo tiempo:

```python
try:
	numero = int(input("ingresa un número: "))
	resultado = 50 // numero

	print(f"50 / {numero} = {resultado}")
except Exception as e:
	print(f"Operación no valida: {e}")

# Ejemplo de ejecución del programa:

# ingresa un número: hola
# Operación no valida: invalid literal for int() with base 10: 'hola'

######################################################################

# Ejemplo de ejecución del programa:

# ingresa un número: 0
# Operación no valida: integer division or modulo by zero
```

Sin embargo,

No se recomienda usar siempre `except Exception:` de forma genérica en Python porque oculta errores imprevistos y dificulta la depuración del código.

\>> Principales razones

* Oculta errores inesperados: Al capturar la clase general `Exception`, enmascaras fallos que no sabías que podían ocurrir (como un `NameError` por una variable mal escrita o un `AttributeError`), haciendo que el programa parezca funcionar cuando en realidad está fallando silenciosamente.

* Dificulta la depuración (debugging): Si ocurre un error real que sí deberías corregir en el código, el bloque genérico lo atrapa y no te muestra el rastreo (traceback) adecuado, lo que alarga el tiempo para encontrar la causa del problema.

* Captura lo que no deseas (en algunos casos): Aunque `Exception` es mejor que un `except:` desnudo (que también atrapa señales críticas del sistema como `KeyboardInterrupt` o `SystemExit`), sigue siendo demasiado amplio y abarca cientos de problemas distintos que deberían tratarse de formas diferentes.

* Impide una respuesta adecuada: Cada error requiere una solución específica. No es lo mismo manejar un archivo que no existe (`FileNotFoundError`) que una división por cero (`ZeroDivisionError`). Usar un genérico te obliga a tratar igual problemas completamente distintos.

___

## Sintaxis (try - except - else - finally)

Ahora, además de trabajar con las dos primeras palabras reservas **(QUE SON OBLIGATORIAS)** podemos utilizar **'else'** y **'finally'** que son opcionales.

### Trabajando con else

```python
try:
	numero = int(input("ingresa un número: "))
	resultado = 50 // numero
	print(f"50 / {numero} = {resultado}")
	
except ValueError as ve:
	print(f"Debes ingresar un número entero. ValueError: {ve}")
except ZeroDivisionError as zde:
	print(f"No puedes dividir por cero. ZeroDivisionError: {zde}")
except Exception as e:
	print(f"Operación no valida: {e}")
	
else:
	print("else: - ¡Operación exitosa!")

# Ejemplo de ejecución del programa:

# ingresa un número: 10
# 50 / 10 = 5
# else: - ¡Operación exitosa!

######################################################################

# Ejemplo de ejecución del programa:

# ingresa un número: hola
# Debes ingresar un número entero. ValueError: invalid literal for int() with base 10: 'hola'
```

Como se observa, el bloque de código dentro de la palabra **'else'** solo se ejecutará si **NINGUNA** excepción se activo, es decir, si nuestro código funciono correctamente.

### Trabajando con finally

```python
try:
	numero = int(input("ingresa un número: "))
	resultado = 50 // numero
	print(f"50 / {numero} = {resultado}")
	
except ValueError as ve:
	print(f"Debes ingresar un número entero. ValueError: {ve}")
except ZeroDivisionError as zde:
	print(f"No puedes dividir por cero. ZeroDivisionError: {zde}")
except Exception as e:
	print(f"Operación no valida: {e}")
	
else:
	print("else: - ¡Operación exitosa!")
	
finally:
	print("finally: - ¡Fin del programa!")

# Ejemplo de ejecución del programa:

# ingresa un número: 10
# 50 / 10 = 5
# else: - ¡Operación exitosa!
# finally: - ¡Fin del programa!

######################################################################

# Ejemplo de ejecución del programa:

# ingresa un número: hola
# Debes ingresar un número entero. ValueError: invalid literal for int() with base 10: 'hola'
# finally: - ¡Fin del programa!
```

El código dentro de **'finally'** **SIEMPRE** se ejecutará. Lo cual es útil si se necesita realizar acciones con las variables contenidas dentro del bloque **'try'**

