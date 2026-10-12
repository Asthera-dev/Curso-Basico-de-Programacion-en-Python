
# Practica propuesta #3

Desarrollar un programa que solicite tres números enteros desde teclado al usuario, posteriormente, el programa deberá determinar e indicar a través de un mensaje en pantalla cual de los tres números es el más grande.

## Requerimientos indispensables:

El mensaje en pantalla deberá mostrar el número que resulto ser el más grande de los tres.

Por ejemplo:

* "El número 10 es el número más grande de los tres." 

> Se recomienda realizar el ejercicio por cuenta propia, sin el uso de la Inteligencia Artificial y con todo el conocimiento adquirido hasta el momento.
> 
> Sin embargo, si lo considera necesario, puede guiarse del siguiente diagrama de flujo para resolver el ejercicio:

```mermaid
graph TD
    %% Inicio y título
    Inicio([Inicio]) --> Titulo[Se imprime en pantalla el titulo del programa]

    %% Entrada de datos
    Titulo --> Num1[/Solicita 1.er número/]
    Num1 --> Num2[/Solicita 2.do número/]
    Num2 --> Num3[/Solicita 3.er número/]

    %% Primera evaluación (¿Es el primero el mayor?)
    Num3 --> Cond1{"nu>nd<br>Y<br>nu>nt"}
    
    Cond1 -- Si --> ResNu[El número nu es el más grande.]
    ResNu --> Fin1([FIN])
    
    %% Segunda evaluación (¿Es el segundo el mayor?)
    Cond1 -- No --> Cond2{nd>nt}
    
    Cond2 -- Si --> ResNd[El número nd es el más grande.]
    ResNd --> Fin2([FIN])
    
    Cond2 -- No --> ResNt[El número nt es el más grande.]
    ResNt --> Fin3([FIN])
```

Donde:
* **nu**: Corresponde al primer número
* **nd**: Corresponde al segundo número
* **nt**:  Corresponde al tercer número 

