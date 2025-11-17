# la constante del iva
IVA_PERCENTATGE = 0.21

def imprimir_tiquet(nom, items_str, total_base):
    
    print(f"Client: {nom}\n")
    # Pongo la cabecera
    print("Producte         Quantitat       Preu unit.      Subtotal")
    print("------------------------------------------------------")
    
    # pongo todos los productos que me llegan en 'items_str'
    # el end="" es para que no haga un salto de linea de mas
    print(items_str, end="")
    print("------------------------------------------------------")

    # calculo el iva y el total
    iva = total_base * IVA_PERCENTATGE
    total_amb_iva = total_base + iva

    # pongo los totales
    print(f"Total sense IVA:                 {total_base:>20.2f} €")
    print(f"IVA (21%):                       {iva:>20.2f} €")
    print(f"TOTAL A PAGAR:                   {total_amb_iva:>20.2f} €")
    print("======================================================")

def gestionar_productes(comanda_actual_str, total_actual_base):

    # variables para guardar las cosas
    nova_comanda_str = comanda_actual_str
    nou_total_base = total_actual_base
    
    # bucle para añadir productos
    continuar_afegint = True
    while continuar_afegint:
        try:
            # 1. pido los datos
            producte_nom = input("> Introdueix el producte: ")
            preu_unitari = float(input("> Preu unitari (€): "))
            quantitat = int(input("> Quantitat: "))

            # que no pongan numeros raros
            if preu_unitari < 0 or quantitat <= 0:
                print("Error: El preu i la quantitat han de ser valors positius.")
                continue # vuelve al principio del while

            # 2. calculo el subtotal
            subtotal_item = preu_unitari * quantitat
            nou_total_base = nou_total_base + subtotal_item

            # 3. preparo la linea para el ticket
            preu_text = f"{preu_unitari:>8.2f} €"
            subtotal_text = f"{subtotal_item:>7.2f} €"
            linia_producte = f"{producte_nom:<15} {quantitat:<13} {preu_text:<14} {subtotal_text}\n"

            # 4. añado la linea al string grande
            nova_comanda_str = nova_comanda_str + linia_producte

        except ValueError:
            # por si meten letras en vez de numeros
            print("Error: El preu i la quantitat han de ser números vàlids.")
            print("Torna a introduir el producte.")
            continue
        except Exception as e:
            print(f"Error inesperat: {e}")
            continue

        # 5. pregunto si quiere mas productos
        resposta_valida = False
        while not resposta_valida:
            resposta = input("> Vols afegir un altre producte? (s/n): ").lower()
            
            # miro si ha puesto 's' o 'n'
            if resposta == 's' or resposta == 'n':
                resposta_valida = True  # si esta bien, salgo del bucle peq
            
        # si dice 'n', paro el bucle grande
        if resposta == 'n':
            continuar_afegint = False
            
    # devuelvo las dos cosas actualizadas
    return nova_comanda_str, nou_total_base

def main():
    
    # variables para guardar la comanda
    nom_client_guardat = ""
    comanda_string_guardada = ""
    total_sense_iva_guardat = 0.0

    # el bucle principal del menu
    sortir = False
    while not sortir:
        
        # pongo el menu
        print("______________________________________")
        print("===== GESTIÓ COMANDES RESTAURANT =====")
        print("______________________________________")
        print("1. Crear nova comanda")
        print("2. Actualitzar comanda anterior")
        print("3. Visualitzar últim tiquet")
        print("4. Sortir")
        
        # pido la opcion
        opcio = input("> Tria una opció: ")

        # menu con match
        match opcio:
            case '1':
                # Opcion 1: nueva
                print("______________________________________")
                print("============ NOVA COMANDA ============")
                print("______________________________________")
                nom_client_guardat = input("> Introdueix el nom del client: ")
                
                # llamo a la funcion de meter productos (pongo "" y 0.0 pq es nueva)
                comanda_string_guardada, total_sense_iva_guardat = gestionar_productes("", 0.0)
                
                print("\n S'està generant el tiquet…")
                print("______________________________________")
                print("=============== TIQUET ===============")
                print("______________________________________")
                
                # llamo a la funcion de imprimir
                imprimir_tiquet(nom_client_guardat, comanda_string_guardada, total_sense_iva_guardat)
                print("\nComanda enregistrada correctament.")

            case '2':
                # Opcion 2: actualizar
                
                # miro si hay algo guardado
                if nom_client_guardat == "":
                    print(">>> Avís: No hi ha cap comanda enregistrada. <<<")
                else:
                    print("______________________________________")
                    print("======= ACTUALITZAR COMANDA ========")
                    print("______________________________________")
                    
                    # llamo a meter productos (paso lo que ya tenia)
                    comanda_string_guardada, total_sense_iva_guardat = gestionar_productes(comanda_string_guardada, total_sense_iva_guardat)
                    
                    print("\nS'està actualitzant la comanda…")
                    print("\n========= TIQUET ACTUALITZAT =========")
                    print("______________________________________")
                    
                    # imprimo el tiquet actualizado
                    imprimir_tiquet(nom_client_guardat, comanda_string_guardada, total_sense_iva_guardat)
                    print("\nComanda actualitzada correctament.")

            case '3':
                # Opcion 3: ver
                
                # si no hay nada, aviso
                if nom_client_guardat == "":
                    print(">>> Avís: No hi ha cap comanda enregistrada. <<<")
                else:
                    print("______________________________________")
                    print("============ ÚLTIM TIQUET ============")
                    print("______________________________________")
                    
                    # llamo a imprimir
                    imprimir_tiquet(nom_client_guardat, comanda_string_guardada, total_sense_iva_guardat)

            case '4':
                # Opcion 4: salir 
                sortir = True
                print("______________________________________")
                print("========== FINS LA PROPERA! ==========")
                print("______________________________________")
                
            case _:
                # si pone otra cosa
                print(">>> Error: Opcio invalida. Tria entre 1 i 4. <<<")

# para arrancar el programa
if __name__ == "__main__":
    main()