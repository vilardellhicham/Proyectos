import time
# funcion para el calefactor
def calefactor():
    print("\nSISTEMA DE CALEFACCION AUTOMATICO")
    min_temp = float(input("Temperatura minima: "))
    max_temp = float(input("Temperatura maxima: "))
    temp_actual = float(input("Temperatura actual: "))
    
    if temp_actual <= min_temp or temp_actual >= max_temp:
        print ("La temperatura esta fuera de los rangos")
        while temp_actual <= min_temp:
            print (f"La calefaccion se ha encendido, la temperatura es de {temp_actual}")
            temp_actual += 1
            time.sleep (0.5)
        while temp_actual >= max_temp:
            print (f"La calefaccion se ha se ha apagado, la temperatura es de {temp_actual}")
            temp_actual -= 0.5
            time.sleep (0.5)
    else:
        print ("La temperatura esta dentro del rango")
# funcion para la alarma de co2
def alarma_co2():
    print("\nSISTEMA DE ALARMA DE CO2")
    limite_co2 = int(input("Nivel maximo de CO2 permitido: "))
    nivel_actual = int(input("Nivel actual de CO2: "))

    if nivel_actual > limite_co2:
        print("La alarma esta sonando, mucho CO2.")
    else:
        print("Todo normal, no hay problema.")

# funcion para la puerta con face id
def puerta_faceid():
    Cara1 = ("Izan")
    Cara2 = ("Oleguer")
    Cara3 = ("Adria")
    Cara4 = ("Daniel")
    print("\nSISTEMA DE PUERTA CON FACE ID")
    print(f"Personas autorizadas:, {Cara1}, {Cara2}, {Cara3}, {Cara4}")

    nombre = input("Ingrese el nombre detectado: ")

    if nombre in {Cara1} or {Cara2} or {Cara3} or {Cara4}:
        print("Acceso permitido a", nombre)
    else:
        print("Acceso denegado, no estas en la lista.")

# funcion para el aspersor automatico
def aspersor():
    print("\nSISTEMA DE REGADO AUTOMATICO")
    hora_activacion = input("Hora de activacion (HH:MM): ")
    duracion = int(input("Duracion del riego (minutos): "))

    print("Riego programado a las", hora_activacion, "por", duracion, "minutos.")

    hora_actual = input("Hora actual (HH:MM): ")

    if hora_actual == hora_activacion:
        print("El aspersor esta encendido.")
    else:
        print("Todavia no es la hora.")

# menu principal (solo se muestra una vez)
def menu_principal():
    print("\n--- DOMOTIC HOUSE ---")
    print("1. Calefactor automatico")
    print("2. Alarma de CO2")
    print("3. Puerta con Face ID")
    print("4. Aspersor automatico")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        calefactor()
    elif opcion == "2":
        alarma_co2()
    elif opcion == "3":
        puerta_faceid()
    elif opcion == "4":
        aspersor()
    elif opcion == "5":
        print("Saliendo del programa...")
    else:
        print("Opcion incorrecta.")

# llamo al menu principal
menu_principal()