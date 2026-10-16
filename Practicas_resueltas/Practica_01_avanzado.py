import os

os.system("cls")

reglamento = {
"Departamento": [1,2,3],
            1: {1: "6 días de vacaciones", 
                2: "14 días de vacaciones",
                3: "20 días de vacaciones"},

            2: {1: "7 días de vacaciones", 
                2: "15 días de vacaciones",
                3: "22 días de vacaciones"},

            3: {1: "10 días de vacaciones",
                2: "20 días de vacaciones",
                3: "30 días de vacaciones"}
}

años_clave = 0

menu = ("""***************************************
* Sistema de Control Vacacional Rappi *
***************************************""")

print(menu)


nombre = input(">> Ingrese su nombre: ")

while True:
    try:
        departamento = int(input(">> Ingrese la clave de su departamento: "))
        if departamento not in reglamento["Departamento"]:
            os.system("cls")
            print(f">> Departamento '{departamento}' invalido. Solo existen [1, 2 y 3] <<\n")
            continue

        años = float(input(">> Ingrese sus años de servicio: "))
        if años < 1:
            os.system("cls")
            años_clave = 4
            print(menu)
            print(f"\n>> El empleado {nombre} del departamento |{'Atención al Cliente' if departamento == 1 else 'Logística' if departamento == 2 else 'Gerencia'}| con  |{int(años)} años| de servicio aun NO CUENTA con derecho a vacaciones. <<\n")
            break
        break
    except ValueError:
        os.system("cls")
        print("=== Error: Ingrese un número válido. ===\n")

if años_clave !=4:
    if años == 1:
        años_clave = 1
    elif 2 <= años < 7:
        años_clave = 2
    else:
        años_clave = 3

    os.system("cls")
    print(menu)
    print(f"\n>> El empleado {nombre} del departamento |{'Atención al Cliente' if departamento == 1 else 'Logística' if departamento == 2 else 'Gerencia'}| con  |{int(años)} años| de servicio tiene derecho a |{reglamento[departamento][años_clave]}| <<\n")