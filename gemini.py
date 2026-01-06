import os
from google import genai
from google.genai import types

sets = {}

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("ERROR: No se encuentra la clave API")
    exit()

cliente = genai.Client(api_key=api_key)

def menu():
    while True:
        print("\n------------------------------")
        print("  Generador de Sets de Dades")
        print("------------------------------")
        print("1. Generar un nou set de dades")
        print("2. Visualitzar un o tots els sets de dades")
        print("3. Esborrar un o tots els sets de dades")
        print("4. Sortir")
        
        opcio = input("Tria una opció: ")
        
        match opcio:  
            case "1":
                print("\n------------------------------")
                print("    Generació d'un nou set")
                print("------------------------------")
                
                nom = input("Introdueix un nom per al set de dades: ")
                
                if nom in sets:
                    print("ERROR: Aquest nom ja existeix")
                    continue
                
                print("Quin tipus de dada vols que sigui?")
                print("1 - Enters")
                print("2 - Decimals")
                print("3 - Text")
                tipus = input("Tipus de dada: ")
                
                tipus_text = ""
                match tipus:
                    case "1": tipus_text = "números enters"
                    case "2": tipus_text = "números decimals"
                    case "3": tipus_text = "text"
                    case _: 
                        print("Opció no vàlida")
                        continue
                
                quantitat = input("Quants elements vols? ")
                
                descripcio = input("Quines dades necessites que et generi?\n> ")
                # Prompt
                prompt = f"Genera una llista de Python con {quantitat} elementos de tipo {tipus_text} sobre: {descripcio}. Retorna NOMÉS la llista, sense explicacions."
                
                print("\nGenerant dades... si us plau, espera.\n")
                
                try:
                    resposta = cliente.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=[prompt],
                        config=types.GenerateContentConfig(
                            system_instruction="Retorna NOMÉS una llista de Python vàlida. Cap text addicional.",
                            temperature=0.7
                        )
                    )
                    
                    text = resposta.text
                    text = text.replace("```python", "").replace("```", "").strip()
                    
                    lista = eval(text)
                    
                    if type(lista) == list:
                        sets[nom] = lista
                        print(f'Set "{nom}" guardat correctament!')
                    else:
                        print("ERROR: No s'ha pogut generar una llista vàlida")
                
                except:
                    print("ERROR: Hi ha hagut un problema amb la generació")

            case "2":
                if len(sets) == 0:
                    print("\nNo hi ha sets guardats")
                    continue
                
                print("\n------------------------------")
                print("  Visualitzar Sets de Dades")
                print("------------------------------")
                print("1 - Visualitzar un set concret")
                print("2 - Visualitzar tots els sets")
                opcio2 = input("Opció: ")
                
                match opcio2:
                    case "1":
                        print("\nSets disponibles: ")
                        for n in sets:
                            print(f"- {n}")
                        
                        nom_buscar = input("Quin vols visualitzar? ")
                        if nom_buscar in sets:
                            print(f"\nSet: {nom_buscar}")
                            print(f"Dades: {sets[nom_buscar]}")
                            print(f"Nombre d'elements: {len(sets[nom_buscar])}")
                        else:
                            print("Aquest set no existeix")
                    
                    case "2":
                        print()
                        for nom in sets:
                            print(f"Set: {nom}")
                            print(f"Dades: {sets[nom]}")
                            print(f"Nombre d'elements: {len(sets[nom])}")
                            print()
                    
                    case _:
                        print("Opció no vàlida")
            case "3":
                if len(sets) == 0:
                    print("\nNo hi ha res per esborrar")
                    continue
                
                print("\n------------------------------")
                print("  Esborrar Sets de Dades")
                print("------------------------------")
                print("1 - Esborrar un set concret")
                print("2 - Esborrar tots els sets")
                opcio3 = input("Opció: ")
                
                match opcio3:
                    case "1":
                        print("\nSets disponibles: ")
                        for n in sets:
                            print(f"- {n}")
                        nom_esborrar = input("Quin vols esborrar? ")
                        
                        if nom_esborrar in sets:
                            del sets[nom_esborrar]
                            print(f'Set "{nom_esborrar}" esborrat!')
                        else:
                            print("Aquest set no existeix")
                    
                    case "2":
                        confirmacio = input("Estàs segur? (s/n): ")
                        if confirmacio.lower() == "s":
                            sets.clear()
                            print("Tots els sets esborrats!")
                        else:
                            print("Cancel·lat")
                    
                    case _:
                        print("Opció no vàlida")

            case "4":
                print("\nTancant el programa. Fins aviat!")
                break
            
            case _:
                print("Opció no vàlida, torna-ho a intentar.")

menu()
