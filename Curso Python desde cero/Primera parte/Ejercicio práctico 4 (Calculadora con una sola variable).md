# Practica Propuesta #4:

Desarrollar una calculadora con las siguientes características:

1. La calculadora deberá ser capaz de calcular las operaciones de **suma, resta, multiplicación, división, división entera, exponente y módulo o resto.**
2. La calculadora deberá de tener un menú de opciones donde el usuario pueda elegir cual es la operación que desea ejecutar.
3. La calculadora deberá solicitar únicamente dos valores por cada operación.

## Requerimientos indispensables:

> El código de este programa deberá funcionar con una única variable que se llamara **numero**, es decir, no se permite la implementación de otra variable.

Puede guiarse con el siguiente ejemplo:

```python
# Calculadora con una sola variable

# Ejemplo de menú:

'********************'
'* Menú de opciones *'
'********************'
'1. Suma'
'2. Resta'
'3. Multiplicación'
'4. División'
'5. División entera'
'6. Exponente'
'7. Modulo o resto'

# Ejemplo de funcionamiento:

'Introduce la opción deseada: '
# Ingresamos 2 (Que corresponde a la resta)

'Introduce el primer número: '
# Ingresamos 10

'Introduce el segundo número: '
# Ingresamos 5

# Salida: El resultado de la resta es: 5


# Recordemos que, para esto, solo utilizamos una variable llamada 'numero'. El uso de mas variables esta prohibido.
```

> Se recomienda realizar el ejercicio por cuenta propia, sin el uso de la Inteligencia Artificial y con todo el conocimiento adquirido hasta el momento.
> 
> Sin embargo, si lo considera necesario, puede guiarse del siguiente diagrama de flujo para resolver el ejercicio:

```mermaid
flowchart TD
    %% Nodos iniciales
    Inicio([Inicio]) --> Titulo[Se imprime en pantalla el titulo del programa]
    Titulo --> Menu[Se muestra el menú de opciones]
    Menu --> Opcion[/Solicitar la opción/]

    %% Cascada de decisiones
    Opcion --> D1{1 suma}
    
    D1 -- No --> D2{2 Resta}
    D2 -- No --> D3{3 Multip}
    D3 -- No --> D4{4 Divisi}
    D4 -- No --> D5{5 Div. Entera}
    D5 -- No --> D6{6 Expon}
    D6 -- No --> D7{7 Resto}
    D7 -- No --> Error[Esta opción no existe]
    Error --> FinError([FIN])

    %% Columna 1: Suma
    D1 -- Si --> S_V1[/Solicita 1. er valor/]
    S_V1 --> S_V2[/Solicita 2. do valor/]
    S_V2 --> S_Op[Suma]
    S_Op --> S_Res[Se imprime en pantalla el resultado]
    S_Res --> S_Fin([FIN])

    %% Columna 2: Resta
    D2 -- Si --> R_V1[/Solicita 1. er valor/]
    R_V1 --> R_V2[/Solicita 2. do valor/]
    R_V2 --> R_Op[Resta]
    R_Op --> R_Res[Se imprime en pantalla el resultado]
    R_Res --> R_Fin([FIN])

    %% Columna 3: Multiplicación
    D3 -- Si --> M_V1[/Solicita 1. er valor/]
    M_V1 --> M_V2[/Solicita 2. do valor/]
    M_V2 --> M_Op[Multiplicación]
    M_Op --> M_Res[Se imprime en pantalla el resultado]
    M_Res --> M_Fin([FIN])

    %% Columna 4: División
    D4 -- Si --> D_V1[/Solicita 1. er valor/]
    D_V1 --> D_V2[/Solicita 2. do valor/]
    D_V2 --> D_Op[División]
    D_Op --> D_Res[Se imprime en pantalla el resultado]
    D_Res --> D_Fin([FIN])

    %% Columna 5: División Entera
    D5 -- Si --> DE_V1[/Solicita 1. er valor/]
    DE_V1 --> DE_V2[/Solicita 2. do valor/]
    DE_V2 --> DE_Op[División entera]
    DE_Op --> DE_Res[Se imprime en pantalla el resultado]
    DE_Res --> DE_Fin([FIN])

    %% Columna 6: Exponente
    D6 -- Si --> E_V1[/Solicita 1. er valor/]
    E_V1 --> E_V2[/Solicita 2. do valor/]
    E_V2 --> E_Op[Exponente]
    E_Op --> E_Res[Se imprime en pantalla el resultado]
    E_Res --> E_Fin([FIN])

    %% Columna 7: Módulo o resto
    D7 -- Si --> Mo_V1[/Solicita 1. er valor/]
    Mo_V1 --> Mo_V2[/Solicita 2. do valor/]
    Mo_V2 --> Mo_Op[Módulo o resto]
    Mo_Op --> Mo_Res[Se imprime en pantalla el resultado]
    Mo_Res --> Mo_Fin([FIN])
```

