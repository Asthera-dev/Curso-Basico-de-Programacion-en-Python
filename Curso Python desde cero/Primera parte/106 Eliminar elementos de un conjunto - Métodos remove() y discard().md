# Eliminar elementos de un conjunto

En Python, para eliminar elementos específicos de un conjunto, podemos apoyarnos de dos métodos de gran utilidad, los cuales son **remove()** y **discar()**.

Sin embargo, existe una diferencia fundamental entre ambos métodos.

## Método remove()

El método remove() se utiliza para eliminar un elemento especifico de un conjunto.

Si el elemento que se intenta eliminar con este método no existe en el conjunto, Python generará un error de tipo **KeyError**.

Por tal motivo, se debe tener cuidado y asegurarse de que el elemento a eliminar existe en el conjunto antes de usar **remove()**

### Sintaxis

La sintaxis para utilizar el método remove() es la siguiente:

 ```python
 # Este método nos permite trabajar con un maximo de un argumento.
 
 nombre_conjunto.remove(elemento)
 ```

## Método discar()

El método **discar()** se utiliza para eliminar un elemento en especifico de un conjunto.

Si el elemento que se intenta eliminar con este método no existe en el conjunto, no ocurrirá ningún error y el conjunto seguirá manteniendo la misma cantidad de elementos.

### Sintaxis

La sintaxis para utilizar el método discard() es la siguiente:

```python
# Este método permite trabajar con un maximo de un argumento.

nombre_conjunto.discar(elemento)
```

___

En resumen, cuando tenemos la seguridad de que el elemento que se desea eliminar esta presente en el conjunto, podemos utilizar el método remove(), aunque siempre existe la posibilidad de un error.

Y cuando no estemos seguros de que el elemento a eliminar está presente en el conjunto y deseamos evitar errores, es mejor utilizar el método **discard()**.

