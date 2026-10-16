# Proyecto #3 - Tienda virtual

Crea un programa que simule una tienda virtual simple, con las siguientes especificaciones:

* Muestra un catálogo de productos disponibles con sus nombres y precios.
* El usuario deberá tener la opción de agregar productos al carrito.
* El usuario deberá tener la opción de ver lo que hay en el carrito.
* El usuario deberá tener la opción de realizar el pago y salir

Ejemplo de funcionamiento:

```python
"""
== Bienvenido a la Tienda Virtual ==

============  Menú  ============
1. Agregar productos al carrito
2. Ver carrito de compras
3. Pagar y salir
4. Salir

>> Seleccione una opción: 0

¡Opción invalida!

============  Menú  ============
1. Agregar productos al carrito
2. Ver carrito de compras
3. Pagar y salir
4. Salir

>> Seleccione una opción: 1

====== AGREGAR PRODUCTOS ======

Productos disponibles:
* Camiseta: $20
* Jeans: $40
* Zapatos: $50
* Sombrero: $10

>> Ingrese el nombre del producto que desea agregar: compu

¡Producto no encontrado!

============  Menú  ============
1. Agregar productos al carrito
2. Ver carrito de compras
3. Pagar y salir
4. Salir

>> Seleccione una opción: 2

====== CARRITO DE COMPRAS ======

El carrito está vacío.

============  Menú  ============
1. Agregar productos al carrito
2. Ver carrito de compras
3. Pagar y salir
4. Salir

>> Seleccione una opción: 3

====== PAGO ======

No se puede pagar, el carrito está vacío.

============  Menú  ============
1. Agregar productos al carrito
2. Ver carrito de compras
3. Pagar y salir
4. Salir

>> Seleccione una opción: 4

¡Hasta luego!
"""
```

```python
"""
== Bienvenido a la Tienda Virtual ==

============  Menú  ============
1. Agregar productos al carrito
2. Ver carrito de compras
3. Pagar y salir
4. Salir

>> Seleccione una opción: 1

====== AGREGAR PRODUCTOS ======

Productos disponibles:
* Camiseta: $20
* Jeans: $40
* Zapatos: $50
* Sombrero: $10

>> Ingrese el nombre del producto que desea agregar: zapatos 

¡Zapatos agregado al carrito!

============  Menú  ============
1. Agregar productos al carrito
2. Ver carrito de compras
3. Pagar y salir
4. Salir

>> Seleccione una opción: 1

====== AGREGAR PRODUCTOS ======

Productos disponibles:
* Camiseta: $20
* Jeans: $40
* Zapatos: $50
* Sombrero: $10

>> Ingrese el nombre del producto que desea agregar: camiseta

¡Camiseta agregado al carrito!

============  Menú  ============
1. Agregar productos al carrito
2. Ver carrito de compras
3. Pagar y salir
4. Salir

>> Seleccione una opción: 1

====== AGREGAR PRODUCTOS ======

Productos disponibles:
* Camiseta: $20
* Jeans: $40
* Zapatos: $50
* Sombrero: $10

>> Ingrese el nombre del producto que desea agregar: camiseta

¡Camiseta agregado al carrito!

============  Menú  ============
1. Agregar productos al carrito
2. Ver carrito de compras
3. Pagar y salir
4. Salir

>> Seleccione una opción: 2

====== CARRITO DE COMPRAS ======
* 1 - Zapatos: $50 c/u
* 2 - Camiseta: $20 c/u

Total a pagar: $90

============  Menú  ============
1. Agregar productos al carrito
2. Ver carrito de compras
3. Pagar y salir
4. Salir

>> Seleccione una opción: 4

¿Esta seguro que desea salir? Tiene objetos en su carrito

>> Confirme la acción (Si/No): no

============  Menú  ============
1. Agregar productos al carrito
2. Ver carrito de compras
3. Pagar y salir
4. Salir

>> Seleccione una opción: 3

====== PAGO ======

Total a pagar: $90

>> Ingrese el monto a pagar: 80

¡Monto insuficiente!

============  Menú  ============
1. Agregar productos al carrito
2. Ver carrito de compras
3. Pagar y salir
4. Salir

>> Seleccione una opción: 3

====== PAGO ======

Total a pagar: $90

>> Ingrese el monto a pagar: 90 

¡Gracias por su compra!
"""
```

```python
"""
== Bienvenido a la Tienda Virtual ==

============  Menú  ============
1. Agregar productos al carrito
2. Ver carrito de compras
3. Pagar y salir
4. Salir

>> Seleccione una opción: 1

====== AGREGAR PRODUCTOS ======

Productos disponibles:
* Camiseta: $20
* Jeans: $40
* Zapatos: $50
* Sombrero: $10

>> Ingrese el nombre del producto que desea agregar: zapatos

¡Zapatos agregado al carrito!

============  Menú  ============
1. Agregar productos al carrito
2. Ver carrito de compras
3. Pagar y salir
4. Salir

>> Seleccione una opción: 3

====== PAGO ======

Total a pagar: $50

>> Ingrese el monto a pagar: 2000


¡Vaya! Ha pagado demasiado. Por favor intente con una cantidad menor.

============  Menú  ============
1. Agregar productos al carrito
2. Ver carrito de compras
3. Pagar y salir
4. Salir

>> Seleccione una opción: 3

====== PAGO ======

Total a pagar: $50

>> Ingrese el monto a pagar: 100

Su cambio es: $50.0

¡Gracias por su compra!
"""
```

> Se recomienda realizar el ejercicio por cuenta propia, sin el uso de la Inteligencia Artificial y con todo el conocimiento adquirido hasta el momento.
> 
> La respuesta a este ejercicio se tratara en la clase presencial.

