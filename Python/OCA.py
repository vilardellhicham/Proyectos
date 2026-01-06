import random
def juego ():

    jugadores = int(input("¿Cuantos jugadores sois? "))
    
    if jugadores >= 2 and jugadores <= 4:
        nombres = []
        for jugador in range(jugadores):
            nombre = input(f"Digues el nom del jugador {jugador + 1}: ")
            nombres.append(nombre)
            print("Jugadores:", nombres)
        casellas = [0] * jugadores
        penalizaciones = [0] * jugadores
        turno = 0
        guanyar = False
        OCA = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59] # En caure a l'oca, s’avança fins a la següent casella on hi ha dibuixada una oca i es torna a tirar.
        PONT = [6, 12] # Si es cau a una casella de pont, es va fins a l’altra casella de pont i es torna a tirar.
        FONDA = [19] # Una jugada sense moure’s.
        POU = [31] # Dues jugades sense moure’s. Si un altre jugador hi cau, se surt al següent torn.
        LABERINT = [42] # Es torna a la casella 39.
        PRESO = [52] # El jugador no es pot moure fins que passin tres torns.
        MORT = [58] # Es torna al principi del recorregut.
        primer_turno = [True] * jugadores
        while not guanyar:
            nombre_actual = nombres[turno]
            
            if penalizaciones[turno] > 0:
                print(f"\n{nombre_actual} esta sancionado. Le quedan {penalizaciones[turno]} turnos sin jugar.")
                penalizaciones[turno] -= 1
                turno += 1
                if turno >= jugadores:
                    turno = 0
                continue 
            if casellas[turno] >= 60:
                input(f"\n{nombre_actual}, aprieta Enter para tirar el dado...")
                dado = random.randint(1, 6)
                print(f"{nombre_actual} ha sacado un {dado}")
                casellas[turno] += dado
                print(f"{nombre_actual} esta en la casilla {casellas[turno]}")
            else:
                input(f"\n{nombre_actual}, aprieta Enter para tirar el dado...")
                dado = random.randint(1, 6)
                dado2 = random.randint(1, 6)
                print(f"{nombre_actual} ha sacado un {dado} y un {dado2}")
                casellas[turno] += dado + dado2
                print(f"{nombre_actual} esta en la casilla {casellas[turno]}")

            if primer_turno == True and dado == 3 and dado2 == 6 or dado == 6 and dado2 == 3:
                casellas[turno] == 26
                print(f"Como {nombre_actual} Ha sacado un 3 y un 6, avanza a la casilla: {casellas[turno]}")

            else:
             if primer_turno == True and dado == 4 and dado2 == 5 or dado == 5 and dado2 == 4:
                casellas[turno] == 53
                print(f"Como {nombre_actual} Ha sacado un 4 y un 5, avanza a la casilla: {casellas[turno]}")

            primer_turno[turno] = False
            
            if casellas[turno] in OCA:
                indice_actual = OCA.index(casellas[turno])
                
                if indice_actual < len(OCA) - 1:

                    nueva_casilla = OCA[indice_actual + 1]
                    casellas[turno] = nueva_casilla
                    print(f"¡De Oca a Oca y tiro porque me toca! Saltas a la casilla {casellas[turno]}")
                    
                    if casellas[turno] >= 63:
                        print(f"¡{nombre_actual} ha ganado!")
                        guanyar = True
                    continue
            if casellas[turno] in PONT:
                if casellas[turno] == 6:
                    casellas[turno] = 12
                    print(f"¡De puente a puente y tiro porque me lleva la corriente! {nombre_actual} salta al 12.")
                elif casellas[turno] == 12:
                    casellas[turno] = 6
                    print(f"¡De puente a puente y tiro porque me lleva la corriente! {nombre_actual} vuelve al 6.")
                
                # Vuelve a tirar el mismo jugador
                continue

            if casellas[turno] in FONDA:
                print(f"¡{nombre_actual} ha caido en la FONDA! Pierde 1 turno.")
                penalizaciones[turno] = 1

            if casellas[turno] in POU:
                print(f"¡{nombre_actual} ha caido en el POZO! Pierde 2 turnos.")
                penalizaciones[turno] = 2

            if casellas[turno] in LABERINT:
                casellas[turno] = 39
                print(f"¡{nombre_actual} se ha perdido en el LABERINTO! Retrocede a la casilla 39.")

            if casellas[turno] in PRESO:
                print(f"¡{nombre_actual} ha ido a la PRISION! Pierde 3 turnos.")
                penalizaciones[turno] = 3

            if casellas[turno] in MORT:
                casellas[turno] = 0
                print(f"¡{nombre_actual} ha caido en la MUERTE! Vuelve a la casilla de salida.")
            
            if casellas[turno] >= 63:
                print(f"\n¡¡FELICIDADES!! {nombre_actual} ha llegado al final y GANA el juego.")
                guanyar = True
            
            #cambio el turno
            turno += 1
            if turno >= jugadores:
                turno = 0
            
    else:
        print("El número de jugadores debe estar entre 2 y 4")

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Jugar")
        print("2. Casillas especiales")
        print("3. Salir")
                
        opcion = input("\nSelecciona una opción: ")
        
        match opcion:
            case "1":
                print("Empezando..")
                juego()
            case "2":
                print("Las casillas especiales son:")
            case "3":
                print("Adios")
                break
            case _:
                print("Opción invalida")

menu()
