# Proyecto #2 - Piensa en un número

Desarrollar un juego interactivo llamado "Piensa un número"

El usuario debe ser invitado a pensar en un número secreto, y el programa intentará adivinarlo haciendo preguntas astutas.

El programa debe:
- Preguntar si el número pensado es mayor, menor o correcto.
- Adivinar el número.
- Mostrar el número de intentos.

Ejemplo de salida esperada:

```python
# Usuario, piensa en un número entre 0 y 100. Yo tratare de adivinarlo.
# Para ayudarme, escribe por favor las siguientes palabras clave: ['mayor', 'menor', 'correcto'] 

# ¿Es 97 tu número?
# >> Ingresa 'mayor', 'menor' o 'correcto': menor
# 
# ¿Es 89 tu número?
# >> Ingresa 'mayor', 'menor' o 'correcto': MENOR
# 
# ¿Es 38 tu número?
# >> Ingresa 'mayor', 'menor' o 'correcto': Mayor
# 
# ¿Es 86 tu número?
# >> Ingresa 'mayor', 'menor' o 'correcto': menOR
# 
# ¿Es 56 tu número?
# >> Ingresa 'mayor', 'menor' o 'correcto': menor
# 
# ¿Es 46 tu número?
# >> Ingresa 'mayor', 'menor' o 'correcto': mayor
# 
# ¿Es 51 tu número?
# >> Ingresa 'mayor', 'menor' o 'correcto': menor
# 
# ¿Es 47 tu número?
# >> Ingresa 'mayor', 'menor' o 'correcto': mayor
# 
# ¿Es 50 tu número?
# >> Ingresa 'mayor', 'menor' o 'correcto': correcto
# 
# ¡Adiviné! Tu número es 50. Y lo hice en 9 intentos.
```

Ejemplo de manejo de errores:

```python
# Usuario, piensa en un número entre 0 y 100. Yo tratare de adivinarlo.
# Para ayudarme, escribe por favor las siguientes palabras clave: ['mayor', 'menor', 'correcto'] 
# 
# ¿Es 0 tu número?
# >> Ingresa 'mayor', 'menor' o 'correcto': no
# 
# Por favor ingresa una de las palabras clave: ['mayor', 'menor', 'correcto'].
# 
# ¿Es 0 tu número?
# >> Ingresa 'mayor', 'menor' o 'correcto': si
# 
# Por favor ingresa una de las palabras clave: ['mayor', 'menor', 'correcto'].
#
# ¿Es 0 tu número?
# >> Ingresa 'mayor', 'menor' o 'correcto': hola
# 
# Por favor ingresa una de las palabras clave: ['mayor', 'menor', 'correcto'].
# 
# ¿Es 0 tu número?
# >> Ingresa 'mayor', 'menor' o 'correcto': correcto
# 
# ¡Adiviné! Tu número es 0. Y lo hice en 1 intentos.
```

> Se recomienda realizar el ejercicio por cuenta propia, sin el uso de la Inteligencia Artificial y con todo el conocimiento adquirido hasta el momento.
> 
> La respuesta a este ejercicio se tratara en la clase presencial.