"""
Proyecto #5 - Conversor de romano a entero

Crear un programa que permita convertir un número romano a su equivalente en números enteros, con las siguiente especificación:

* El programa deberá solicitar al usuario que ingrese un número romano.

"""

# Creamos el diccionario que contendra la equivalencia por simbolo:

valores_romanos = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

# Tabla para convertir de entero a romano (de mayor a menor).
# Incluye las "restas" validas (CM, CD, XC, XL, IX, IV), que son las
# UNICAS combinaciones de resta permitidas en la notacion romana.
tabla_entero_a_romano = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
    (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"),
    (1, "I")
]


def romano_a_entero(romano):
    """Convierte un texto romano a entero SIN validar si esta bien formado.
    (Ej: 'IIIX' daria 7, aunque no sea un romano valido)."""
    resultado = 0  # Variable que guarda el resultado
    anterior = 0   # Variable que guarda el valor del simbolo anterior

    # Recorremos el numero de derecha a izquierda
    for caracter in romano[::-1]:
        actual = valores_romanos[caracter]

        # Si el simbolo es menor que el de su derecha, se resta (ej: IV)
        # en caso contrario, se suma (ej: VI)
        if actual < anterior:
            resultado -= actual
        else:
            resultado += actual

        anterior = actual

    return resultado


def entero_a_romano(numero):
    """Convierte un entero (1 a 3999) a su forma romana correcta."""
    romano = ""
    # Vamos tomando el valor mas grande posible de la tabla tantas
    # veces como quepa en el numero, y lo restamos.
    for valor, simbolo in tabla_entero_a_romano:
        while numero >= valor:
            romano += simbolo
            numero -= valor
    return romano


def validar_romano(romano):
    """Revisa que el texto sea un numero romano valido.
    Devuelve un mensaje de error (str) o None si todo esta bien."""

    # 1) Entrada vacia
    if romano == "":
        return "No ingresaste ningun valor."

    # 2) Caracteres que no son simbolos romanos (ej: '5', 'A', espacios...)
    invalidos = [c for c in romano if c not in valores_romanos]
    if invalidos:
        # dict.fromkeys elimina repetidos conservando el orden
        lista = ", ".join(f"'{c}'" for c in dict.fromkeys(invalidos))
        return f"Los caracteres {lista} no son digitos romanos validos."

    # 3) Estructura del numero (ej: 'IIIII', 'IIIX', 'VV', 'IC'...)
    #    Truco: convertimos a entero y de vuelta a romano. Si el romano
    #    "correcto" no coincide con lo que escribio el usuario, entonces
    #    la entrada no respeta las reglas de la numeracion romana.
    valor = romano_a_entero(romano)
    if valor < 1 or valor > 3999:
        return "El numero esta fuera del rango permitido (1 a 3999)."

    forma_correcta = entero_a_romano(valor)
    if forma_correcta != romano:
        return (f"'{romano}' no es un numero romano bien formado "
                f"(revisa repeticiones o restas invalidas).")

    # Si paso todas las validaciones, no hay error
    return None


# Solicitamos al usuario su número romano hasta que ingrese uno valido

while True:
    # strip() quita espacios al inicio/final; upper() acepta minusculas
    numero_romano = input("\n\n>>> Ingresa un número romano para convertirlo a entero: ").strip().upper()

    error = validar_romano(numero_romano)

    if error is None:
        break  # Entrada valida: salimos del ciclo

    # Entrada invalida: mostramos el motivo y volvemos a pedir
    print(f"\nError: {error}\nIntentalo de nuevo.")

# Realizamos la conversion (ya sabemos que la entrada es valida)
resultado = romano_a_entero(numero_romano)

print(f"\nEl número {numero_romano} convertido a entero es: {resultado}\n")