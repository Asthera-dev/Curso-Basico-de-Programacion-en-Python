En programación, un comentario es una construcción de un lenguaje de programación destinada a incrustar anotaciones legibles al programador en el código fuente de un programa.

Estas anotaciones, son potencialmente significativas para los programadores, pero usualmente ignorados por los compiladores e intérpretes.

Los comentarios son añadidos usualmente con el propósito de hacer el código más fácil de entender con vista a su mantenimiento o reutilización.

La sintaxis y reglas para los comentarios varían y usualmente son definidas en la especificación del lenguaje de programación.

En Python, la forma de añadir comentarios son las siguientes:

* Con el signo de #
* Con un par de comillas (" ")
* Con comillas triples (""" """) para crear comentarios multilínea.

**Nota:**

Las comillas NO son comentarios, son Strings que, al no ser asignados a una variable, se interpretan como un valor nulo y por tal motivo el intérprete de Python no los toma en cuenta. 

Se usan formalmente al inicio de funciones, clases o módulos para documentar el código (lo que permite que herramientas y funciones como ***help ()*** lean la descripción).

Con lo cual se genera un comentario dentro del código.

Para visualizar esto, se recomienda realizar un script de Python para visualizar la salida en consola:

```Python
# Esto es un comentario

print ("Hola")

"Esto es un comentario"

"""
Esto es un
comentario
multilinea
"""
```

