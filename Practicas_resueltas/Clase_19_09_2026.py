print("""***************************************
* Sistema de Control Vacacional Rappi *
***************************************""")
cliente = input("Ingrese su nombre: ")
departamento = int(input("Ingrese el numero de su departamento: "))
años = int(input("Ingrese la cantidad de años que lleva trabajando en la empresa: "))

if departamento == 1:
    if años <1:
        print("Usted no tiene derecho a vacaciones.")
    if años == 1:
        print(cliente, "Usted tiene derecho a 6 días de vacaciones y pertenece al departamento de: Atención al cliente" )
    if años > 2 and años <7:
        print(cliente,"Usted tiene derecho a 14 días de vacaciones y pertenece al departamento de: Atención al cliente")
    if años > 7:
        print(cliente,"Usted tiene derecho a 20 días de vacaciones y pertenece al departamento de: Atención al cliente")

if departamento == 2:
    if años <1:
        print("Usted no tiene derecho a vacaciones.")
    if años == 1:
        print(cliente, "Usted tiene derecho a 7 días de vacaciones y pertenece al departamento de: Logistica" )
    if años > 2 and años <7:
        print(cliente,"Usted tiene derecho a 15 días de vacaciones y pertenece al departamento de: Logistica")
    if años > 7:
        print(cliente,"Usted tiene derecho a 22 días de vacaciones y pertenece al departamento de: Logistica")

if departamento == 3:
    if años <1:
        print("Usted no tiene derecho a vacaciones.")
    if años == 1:
        print(cliente, "Usted tiene derecho a 10 días de vacaciones y pertenece al departamento de: Gerencia" )
    if años > 2 and años <7:
        print(cliente,"Usted tiene derecho a 20 días de vacaciones y pertenece al departamento de: Gerencia")
    if años > 7:
        print(cliente,"Usted tiene derecho a 30 días de vacaciones y pertenece al departamento de: Gerencia")

else:
    print("El departamento ingresado no es valido, por favor ingrese un numero de departamento valido.")