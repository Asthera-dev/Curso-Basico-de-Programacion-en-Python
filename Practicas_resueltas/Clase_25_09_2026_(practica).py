print("=== INICIO DEL SISTEMA ===")

# 1. Bucle infinito
while True:
    
    # Pedir datos al usuario
    entrada = input("\nIngresa un número (o escribe 'salir' para abandonar): ")
    
    # 4. Salir si el usuario escribe 'salir'
    if entrada.lower() == "salir":
        print("Apagando el sistema...")
        break  
        
    # Validar que la entrada sea un número para evitar que el programa colapse
    if entrada.isdigit():
        numero = int(entrada)
        
        # 2. Menú interno anidado (if / elif)
        if numero % 2 == 0:
            # 3. Ignorar números pares
            continue  
            
        elif numero % 2 != 0:
            # 5. Imprimir los resultados en una sola línea elegante
            print("Procesando", numero, "Impar validado", sep=" - ", end=" [OPERACIÓN EXITOSA]\n")
            
    else:
        print("Entrada no reconocida. Por favor, intenta de nuevo.")