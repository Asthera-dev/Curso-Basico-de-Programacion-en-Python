# Método capitalize()

Este método se utiliza para convertir el primer carácter de un String en una letra mayúscula, y a su vez, todas las letras restantes en minúsculas.

La sintaxis para el método capitalize() es la siguiente:

```python
nombre_variable.capitalize()# El metodo en minúsculas, sin espacios y con dos parentesis vacios.
```

Supongamos que tenemos un String con letras mayúsculas y minúsculas:

```python
string = "el VIAJE eS la RecoMpensa"
print(f"Antes de capitalize(): {string}")
string = string.capitalize()
print (f"Después de capitalize(): {string}") 

# Salida: Antes de capitalize(): el VIAJE eS la RecoMpensa
#         Después de capitalize(): El viaje es la recompensa
```

> Como podrán darse cuenta, el uso e implementación del método capitalize() es sumamente sencillo. Basta con que practiquemos un poco para dominarlo al cien por ciento.