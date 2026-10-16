# La instrucción import

La instrucción import es esencial para incorporar módulos y bibliotecas en un programa, permitiendo la reutilización y organización eficiente del código.

Esto posibilita aprovechar las numerosas funcionalidades que Python ofrece, ampliando las capacidades del programa de manera modular.

En Python, un módulo es simplemente un archivo que contiene definiciones, como funciones, clases y variables

Los módulos facilitan la organización y reutilización del código, dividiendo un programa en partes más manejables.

Por otro lado, una biblioteca es un conjunto de módulos organizados de manera especifica para abordar un propósito en común y proporcionar funcionalidades más amplias y especificas.

La función import contribuye a la modularidad del código, permitiendo la división de programas extensos en módulos más pequeños y manejables.

Esto facilita el mantenimiento y la compresión del código, mejorando la eficiencia y la escalabilidad del desarrollo,

Python cuenta con una amplia variedad de bibliotecas y módulos que podemos utilizar mediante la instrucción import.

Por ejemplo:

\>> Tiempos y Fechas:
	1. **datetime:** Funciones para trabajar con fechas y horas.
	2. **time:** Funciones relacionadas con el tiempo y el reloj.

\>> Procesamiento de Texto:
	1. **re:** Expresiones regulares para el procesamiento de texto.
	2. **string:** Funciones y constantes relacionadas con cadenas.

\>> Manejo de Datos:
	1. **pandas:** Estructuras de datos y el análisis de datos.
	2. **json:** Manipulación de datos en formato JSON.

\>> Matemáticas y Ciencia:
	1. **math:** Funciones matemáticas estándar.
	2. **numpy:** Operaciones numéricas avanzadas

Para esta nota, trabajaremos con la librería **math**:

```python
# Importar un módulo completo
print ("Importar un modulo completo")

import math
print (math.sqrt(25))
print (math.sin(30))

# Importar un modulo con un alias
print ("\nImportar un modulo con un alias")

import math as m
print (m.sqrt(25))
print (m.tan(30))

# Importar solo lo necesario de un modulo
print ("\nImportar solo lo necesario de un modulo")

from math import sqrt, sin
print (sqrt(25))
print (sin(30))

# Importar todo de un modulo (evitar en general)
print ("\nImportar todo de un modulo (evitar en general) ")

from math import *
print (tan (30))
print (sin(30))
print (sqrt (25))

# Salida:

# Importar un modulo completo
# 5.0
# -0.9880316240928618
#
# Importar un modulo con un alias
# 5.0
# -6.405331196646276
#
# Importar solo lo necesario de un modulo
# 5.0
# -0.9880316240928618
#
# Importar todo de un modulo (evitar en general)
# -6.405331196646276
# -0.9880316240928618
# 5.0
```

Las diferencias entre estos métodos se comentarán en clase.

Finalmente:

> Se recomienda practicar este tema modificando los ejercicios anteriores y creando sus propios programas. Esto con el objetivo de lograr una compresión más profunda del tema.