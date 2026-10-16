# Programa para invertir un string

# ## Requerimientos indispensables:
# * No se permite modificar la cadena de caracteres original
# * Utilizar el ciclo o bucle for
# * No se permite el uso de slicing

string = "Estoy aprendiendo Python" # input(">> Ingrese la oración a invertir: ")
string_reversed = "" #aloH

for character in string:
    string_reversed = character + string_reversed
    # string_reversed = string_reversed + character

print(string_reversed)

# Hola 