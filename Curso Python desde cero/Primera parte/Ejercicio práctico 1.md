# Práctica propuesta #1

La compañía multinacional Rappi solicita un sistema que determine los días de vacaciones a los que tiene derecho un trabajador, tomando en cuenta las siguientes características:

## Departamentos:

> Existen **tres departamentos** dentro de la compañía con sus respectivas claves:
> 	1. Departamento de Atención al cliente. (Clave 1)
> 	2. Departamento de Logística. (Clave 2)
> 	3. Gerencia. (Clave 3)

### Trabajadores con Clave 1 (Atención al cliente):

* Con 1 año de servicio, reciben 6 días de vacaciones.
* Con 2 a 6 años de servicio, reciben 14 días de vacaciones.
* A partir de 7 años de servicio, reciben 20 días de vacaciones.

### Trabajadores con Clave 2 (Logística):

* Con 1 año de servicio, reciben 7 días de vacaciones.
* Con 2 a 6 años de servicio, reciben 15 días de vacaciones.
* A partir de 7 años de servicio, reciben 22 días de vacaciones.

### Trabajadores con Clave 3 (Gerencia):

* Con 1 año de servicio, reciben 10 días de vacaciones.
* Con 2 a 6 años de servicio, reciben 20 días de vacaciones.
* A partir de 7 años de servicio, reciben 30 días de vacaciones.

## Requerimientos indispensables:

* El sistema debe de solicitar el **Nombre, Clave del Departamento y Antigüedad** del trabajador desde teclado.
* Posteriormente el programa debe mostrar un mensaje en pantalla que contenga **el nombre del trabajador y los días de vacaciones a los que tiene derecho.**
* Debe contar con sistema de validación para datos no contemplados: **claves inexistentes** y **años de servicio no suficientes** 

## Ejemplo del programa con Diagrama de Flujo.

```mermaid
graph TD
    %% Inicio y Entradas
    Inicio([Inicio]) --> Titulo[Se imprime en pantalla el titulo del programa]
    Titulo --> Nom[/Solicita Nombre/]
    Nom --> Clave[/Solicita clave/]
    Clave --> Años[/Solicita años/]

    %% Validaciones Clave Principal
    Años --> C1{Clave 1}

    %% Lógica para Clave 1
    C1 -- Si --> C1_1{1 año}
    C1_1 -- Si --> V1_1[6 días de vacaciones.]
    C1_1 -- No --> C1_2{2 a 6 años}
    C1_2 -- Si --> V1_2[14 días de vacaciones.]
    C1_2 -- No --> C1_3{7 años o más}
    C1_3 -- Si --> V1_3[20 días de vacaciones.]
    C1_3 -- No --> SD1[Sin derecho a vacaciones]

    %% Lógica para Clave 2
    C1 -- No --> C2{Clave 2}
    C2 -- Si --> C2_1{1 año}
    C2_1 -- Si --> V2_1[7 días de vacaciones.]
    C2_1 -- No --> C2_2{2 a 6 años}
    C2_2 -- Si --> V2_2[15 días de vacaciones.]
    C2_2 -- No --> C2_3{7 años o más}
    C2_3 -- Si --> V2_3[22 días de vacaciones.]
    C2_3 -- No --> SD2[Sin derecho a vacaciones]

    %% Lógica para Clave 3
    C2 -- No --> C3{Clave 3}
    C3 -- Si --> C3_1{1 año}
    C3_1 -- Si --> V3_1[10 días de vacaciones.]
    C3_1 -- No --> C3_2{2 a 6 años}
    C3_2 -- Si --> V3_2[20 días de vacaciones.]
    C3_2 -- No --> C3_3{7 años o más}
    C3_3 -- Si --> V3_3[30 días de vacaciones.]
    C3_3 -- No --> SD3[Sin derecho a vacaciones]

    %% Clave Inexistente
    C3 -- No --> Error[La clave no existe]

    %% Cierre y Fin del Programa
    Fin([FIN])

    V1_1 --> Fin
    V1_2 --> Fin
    V1_3 --> Fin
    SD1 --> Fin
    
    V2_1 --> Fin
    V2_2 --> Fin
    V2_3 --> Fin
    SD2 --> Fin
    
    V3_1 --> Fin
    V3_2 --> Fin
    V3_3 --> Fin
    SD3 --> Fin
    
    Error --> Fin
```

