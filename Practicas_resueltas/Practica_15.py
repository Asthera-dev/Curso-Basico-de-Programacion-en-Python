frase =input(">> Ingrese un texto: ")

ocurrencia = {}

for i in frase:
    if i in ocurrencia:
        ocurrencia[i] +=1
    else:
        ocurrencia[i] = 1

print(ocurrencia)



