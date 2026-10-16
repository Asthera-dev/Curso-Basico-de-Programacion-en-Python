"""diccionario = {"clave":2,
                2:[1,2,3],
                3: {}
                }

print(diccionario)
diccionario[2] = 6
diccionario["2"] = 6
print(diccionario)"""

"""print(f"Diccionario original: {dict_name}")
dict_name.clear()
print(dict_name.pop("a","no existe"))

print(f"Diccionario modificado: {dict_name}")
print(dict_name.pop("a", "No existe"))

dict_name.clear()"""

"""dict_name = {"b": 2,
			 "c": 3,
             "a": 10
			 }

dict_name_2 = dict_name
dict_name_3 = dict_name.copy()

print(f"Diccionario 1: {dict_name}\nDiccionario 2: {dict_name_2}\nDiccionario 3: {dict_name_3}")"""

"""secuencia = ["d", "e", "f"]
modificado = dict.fromkeys(secuencia)
modificado_2 = {}.fromkeys(secuencia, 5)
print(modificado)
print(modificado_2)"""

""""print(secuencia.items())
print(secuencia.keys())
print(secuencia.values())

items = list(secuencia.items())
print(items[0])"""

secuencia = {"uno": 1,
             "dos": 2,
             "tres": 3}


print(secuencia)
print(secuencia.setdefault("tres",4))
print(secuencia.setdefault("cuatro",4))
print(secuencia)