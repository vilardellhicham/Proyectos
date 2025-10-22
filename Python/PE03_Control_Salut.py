from datetime import date
#Variables principales vacias
nom = ""
edat = None
pes = None
altura = None

# Bucle principal del programa (el menú se repite hasta que el usuario quiera salir)
while True:
    # Mostramos el menú de opciones
    print("\na) Introduir dades\nb) Modificar dades\nc) Visualitzar dades\nd) Sortir\n")

    # Pedimos la opción al usuario y la convertimos a minúsculas
    eleccio = input("Escull un: ").strip().lower()

    # OPCIÓN A: INTRODUCIR DATOS NUEVOS
    if eleccio == "a":
        # PEDIR NOMBRE (bucle que repite hasta que el usuario pone algo válido)
        while True:
            temp = input("Digues el nom complert: ").strip()
            if not temp:
                print("Error: el nom no pot quedar buit. Torna-ho a provar.")
            else:
                # Pone en mayusculas todas las palabras
                nom = " ".join([x.capitalize() for x in temp.split()])
                break  # sale del bucle porque el nombre es válido

        # PEDIR EDAD (repite hasta que la edad sea válida)
        while True:
            s = input("Edat: ").strip()
            try:
                val = int(s)  # convierte el texto en número entero
                if val <= 0 or val > 120:
                    print("Error: L'edat ha de ser un enter positiu ≤ 120. Torna-ho a provar.")
                else:
                    edat = val
                    break
            except ValueError:
                # Si el usuario no pone un numero o lo pone mal
                print("Error: format numèric invàlid. Torna-ho a provar.")

        # PEDIR PESO (repite hasta que sea válido)
        while True:
            s = input("Pes (kg): ").replace(",", ".").strip()  # te deja poner o punto decimal
            try:
                val = float(s)
                if val <= 0 or val > 400:
                    print("Error: El pes ha de ser un decimal positiu raonable. Torna-ho a provar.")
                else:
                    pes = val
                    break
            except ValueError:
                print("Error: format numèric invàlid. Torna-ho a provar.")

        # PEDIR ALTURA (repite hasta que sea valida)
        while True:
            s = input("Alçada (m): ").replace(",", ".").strip()
            try:
                val = float(s)
                if val <= 0.5 or val > 2.5:
                    print("Error: L'alçada ha de ser un decimal positiu entre 0.5 i 2.5 metres. Torna-ho a provar.")
                else:
                    altura = val
                    break
            except ValueError:
                print("Error: format numèric invàlid. Torna-ho a provar.")

        print("✅ Dades introduïdes correctament.\n")

    # OPCIÓN B: MODIFICAR DATOS EXISTENTES
    elif eleccio == "b":
        # Si no se han introducido datos antes, no se puede modificar nada
        if not nom:
            print("Primer has d'introduir les dades.")
            continue  # vuelve al menú principal

        # Submenú para elegir qué dato se quiere cambiar
        while True:
            print("\nQuè vols modificar?\n1. Nom\n2. Edat\n3. Pes\n4. Alçada\n5. Tornar")
            opcio_mod = input("Escull (1-5): ").strip()

            # Modificar el nombre
            if opcio_mod == "1":
                while True:
                    temp = input("Digues el nom complert: ").strip()
                    if not temp:
                        print("Error: el nom no pot quedar buit. Torna-ho a provar.")
                    else:
                        nom = " ".join([x.capitalize() for x in temp.split()])
                        print("Nom modificat correctament.")
                        break

            # Modificar la edad
            elif opcio_mod == "2":
                while True:
                    s = input("Edat: ").strip()
                    try:
                        val = int(s)
                        if val <= 0 or val > 120:
                            print("Error: L'edat ha de ser un enter positiu ≤ 120. Torna-ho a provar.")
                        else:
                            edat = val
                            print("Edat modificada correctament.")
                            break
                    except ValueError:
                        print("Error: format numèric invàlid. Torna-ho a provar.")

            # Modificar el peso
            elif opcio_mod == "3":
                while True:
                    s = input("Pes (kg): ").replace(",", ".").strip()
                    try:
                        val = float(s)
                        if val <= 0 or val > 400:
                            print("Error: El pes ha de ser un decimal positiu raonable. Torna-ho a provar.")
                        else:
                            pes = val
                            print("Pes modificat correctament.")
                            break
                    except ValueError:
                        print("Error: format numèric invàlid. Torna-ho a provar.")

            # Modificar la altura
            elif opcio_mod == "4":
                while True:
                    s = input("Alçada (m): ").replace(",", ".").strip()
                    try:
                        val = float(s)
                        if val <= 0.5 or val > 2.5:
                            print("Error: L'alçada ha de ser un decimal positiu entre 0.5 i 2.5 metres. Torna-ho a provar.")
                        else:
                            altura = val
                            print("Alçada modificada correctament.")
                            break
                    except ValueError:
                        print("Error: format numèric invàlid. Torna-ho a provar.")

            # Opción 5: salir del submenú y volver al menú principal
            elif opcio_mod == "5":
                break
            else:
                print("Opció invàlida. Torna-ho a provar.")

    # OPCIÓN C: VISUALIZAR DATOS
    elif eleccio == "c":
        # Si faltan datos, no se puede calcular nada
        if not all([nom, edat, pes, altura]):
            print("Falten dades per visualitzar.")
            continue

        # Calculamos los resultados
        nom_norm = " ".join([x.capitalize() for x in nom.split()])
        imc = pes / (altura ** 2)

        # Clasificación del IMC segun el valor
        if imc < 18.5:
            imc_cat = "Pes baix"
        elif imc < 25:
            imc_cat = "Pes normal"
        elif imc < 30:
            imc_cat = "Sobrepès"
        else:
            imc_cat = "Obesitat"

        # Frecuencia cardíaca máxima estimada
        fc_max = 220 - edat
        fc50 = round(fc_max * 0.5)  # 50% del máximo
        fc85 = round(fc_max * 0.85) # 85% del máximo

        # Agua recomendada por día (0.035 litros por kilo)
        aigua = round(pes * 0.035, 2)

        # Año de nacimiento aproximado
        any_naix = date.today().year - edat

        # Mostramos todos los datos por pantalla
        print(f"\nHola, {nom_norm}!")
        print(f"Edat: {edat} anys | Pes: {pes:.2f} kg | Alçada: {altura:.2f} m")
        print(f"IMC: {imc:.2f} ({imc_cat})")
        print(f"FC màxima estimada: {fc_max} bpm")
        print(f"Zona FC objectiu: {fc50}-{fc85} bpm")
        print(f"Aigua recomanada: {aigua} L/dia")
        print(f"Any de naixement aproximat: {any_naix}\n")

    # OPCIÓN D: SALIR DEL PROGRAMA
    elif eleccio == "d":
        print("Sortint…")
        break  # sale del bucle principal y termina el programa

    # Si el usuario escribe algo que no es a/b/c/d
    else:
        print("Opció invàlida. Torna-ho a provar.")