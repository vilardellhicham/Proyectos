from Tiempo import parse_hhmm
from Tiempo import siguiente_minuto
def calefactor ():
    def reloj_calefactor():
        print("\nSISTEMA DE CALEFACCIÓN AUTOMÁTICO CON RELOJ")
    # Entradas
        min_temp = float(input("Temperatura mínima: "))
        max_temp = float(input("Temperatura máxima: "))
        temp_actual = float(input("Temperatura actual: "))
        hora_on_str = input("Hora de encendido (HH:MM): ")
        hora_off_str = input("Hora de apagado (HH:MM): ")

        h_on, m_on = parse_hhmm(hora_on_str)
        h_off, m_off = parse_hhmm(hora_off_str)

    # Estado del reloj y del calefactor
        h, m = 0, 0
        permitido_por_horario = False
        calefaccion_encendida = False

    # Simulacion de 24 horas
        for t in range(24 * 60):
            # Eventos de horario
            if h == h_on and m == m_on:
                permitido_por_horario = True
                print(f"[{h}:{m}] Encendido por horario. Temp={temp_actual} C")
            if h == h_off and m == m_off:
                permitido_por_horario = False
                calefaccion_encendida = False
                print(f"[{h}:{m}] Apagado por horario. Temp={temp_actual} C")

            # si el horario esta permitido y la temperatura actual es menor a la minima, se sube
            if permitido_por_horario and temp_actual < min_temp:
                if not calefaccion_encendida:
                    print(f"[{h}:{m}] Calefacción ON (bajo mínimo). Temp={temp_actual} C")
                    calefaccion_encendida = True
                temp_actual += 0.5  # ritmo de subida por minuto simulado
                print(f"[{h}:{m}] Sube a {temp_actual} C")
            else:
                # Si está fuera de horario o ya por encima del maximo, apagar
                if calefaccion_encendida and (not permitido_por_horario or temp_actual >= max_temp):
                    print(f"[{h}:{m}] Calefacción OFF. Temp={temp_actual} C")
                    calefaccion_encendida = False
                # Enfriamiento si se ha pasado del máximo
                if temp_actual > max_temp:
                    temp_actual -= 0.5
                    print(f"[{h}:{m}] Baja a {temp_actual} C")

            # Avanza el reloj
            h, m = siguiente_minuto(h, m)
    reloj_calefactor()

# funcion para la alarma de co2
def alarma_co2():
    print("\nSISTEMA DE ALARMA DE CO2")
    limite_co2 = int(input("Nivel máximo de CO2 permitido (ppm): "))
    n_lecturas = int(input("¿Cuántas lecturas quieres comprobar?: "))

    for i in range(1, n_lecturas + 1):
        nivel_actual = int(input(f"Lectura {i} - Nivel actual de CO2 (ppm): "))
        if nivel_actual > limite_co2:
            print("La alarma está sonando, demasiado CO2.")
        else:
            print("Todo normal, niveles dentro del límite.")

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
    hora_activacion = input("Hora de activación (HH:MM): ")
    duracion = int(input("Duración del regado (minutos): "))
    hora_actual = input("Hora actual (HH:MM): ").strip()

    h_act, m_act = parse_hhmm(hora_activacion)
    h, m = parse_hhmm(hora_actual)

    encendido = False
    restante = 0

    # Simulación de 24 horas (minuto a minuto)
    for _ in range(24 * 60):
        # Evento de encendido
        if (h, m) == (h_act, m_act) and not encendido and restante == 0:
            encendido = True
            restante = duracion
            print(f"[{h:02d}:{m:02d}] Aspersor encendido por {duracion} min.")

        # Funcionamiento y apagado cuando termina la duración
        if encendido:
            restante -= 1
            if restante > 0:
                print(f"[{h:02d}:{m:02d}] Regando... quedan {restante} min.")
            else:
                encendido = False
                print(f"[{h:02d}:{m:02d}] Aspersor apagado")

        # Avanza 1 minuto
        h, m = siguiente_minuto(h, m)
