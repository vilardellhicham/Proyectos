from Arma import *
from Personaje import *

Personaje1 = Personaje()
Personaje2 = Personaje()
def main(self):
        opcio = ""
        while opcio != "4":
            print("\n========= JOC RPG =========")
            print("1. Crear personatge")
            print("2. Mostrar personatges")
            print("3. Jugar combat simple (1vs1)")
            print("4. Sortir")

            opcio = input("Tria una opció: ")

            match opcio:
                case "1":
                    print("Jugador 1 - Crear personaje tu mismo o automaticamente")
                    print("1. Crear personaje tu mismo")
                    print("2. Crear personaje automáticamente")
                    opcio_creacio = input("Tria una opció: ")
                    if opcio_creacio == "1":
                        Personaje1.crearpersonaje()
                    elif opcio_creacio == "2":
                        Personaje1.Personajeautomatico()
                    else:
                        print("Opció no vàlida.")
                    
                    print("Jugador 2 - Crear personaje tu mismo o automaticamente")
                    print("1. Crear personaje tu mismo")
                    print("2. Crear personaje automáticamente")
                    opcio_creacio = input("Tria una opció: ")
                    if opcio_creacio == "1":
                        Personaje2.crearpersonaje()
                    elif opcio_creacio == "2":
                        Personaje2.Personajeautomatico()
                    else:
                        print("Opció no vàlida.")
                case "2":
                    print("\nJugador 1:")
                    print(Personaje1)
                    print("\nJugador 2:")
                    print(Personaje2)
                case "3":
                    self.combatsimple()
                case "4":
                    print("Sortint del joc...")
                case _:
                    print("Opció no vàlida.")


def combatsimple(self):
        print("\nComença el combat simple entre Jugador 1 i Jugador 2!")
        while Personaje1.Salud > 0 and Personaje2.Salud > 0:
            print("Jugador 1 que accion quieres hacer")
            print("1. Atacar")
            print("2. Lanzar hechizo")
            print("3. Defender")
            opcio_accio = input("Tria una opció: ")
            if opcio_accio == "1":
                print(f"{Personaje2.Nombre} quiere defenderse?")
                print("1. Sí")
                print("2. No")
                opcio_defensa = input("Tria una opció: ")
                if opcio_defensa == "1":
                    Personaje2.defender()
                    print(f"{Personaje2.Nombre} se está defendiendo.")
                elif opcio_defensa == "2":
                    Personaje2.defendiendo = False
                else:
                    print("Opció no vàlida.")
                Personaje1.atacar(Personaje2)
            elif opcio_accio == "2":
                print(f"{Personaje2.Nombre} quiere defenderse?")
                print("1. Sí")
                print("2. No")
                opcio_defensa = input("Tria una opció: ")
                if opcio_defensa == "1":
                    Personaje2.defender()
                    print(f"{Personaje2.Nombre} se está defendiendo.")
                Personaje1.Hechizo(Personaje2)
            elif opcio_accio == "3":
                Personaje1.defender()
                print(f"{Personaje1.Nombre} se está defendiendo.")
            else:
                print("Opció no vàlida.")
            if Personaje2.Salud <= 0:
                print(f"{Personaje2.Nombre} ha sido derrotado. ¡{Personaje1.Nombre} gana el combate!")
            
            print("Jugador 2 que accion quieres hacer")
            print("1. Atacar")      
            print("2. Lanzar hechizo")
            print("3. Defender")
            opcio_accio = input("Tria una opció: ")
            if opcio_accio == "1":
                print(f"{Personaje1.Nombre} quiere defenderse?")
                print("1. Sí")
                print("2. No")
                opcio_defensa = input("Tria una opció: ")
                if opcio_defensa == "1":
                    Personaje1.defender()
                    print(f"{Personaje1.Nombre} se está defendiendo.")
                elif opcio_defensa == "2":
                    Personaje1.defendiendo = False
                else:
                    print("Opció no vàlida.")
                Personaje2.atacar(Personaje1)
            elif opcio_accio == "2":
                print(f"{Personaje1.Nombre} quiere defenderse?")
                print("1. Sí")
                print("2. No")
                opcio_defensa = input("Tria una opció: ")
                if opcio_defensa == "1":
                    Personaje1.defender()
                    print(f"{Personaje1.Nombre} se está defendiendo.")
                elif opcio_defensa == "2":
                    Personaje1.defendiendo = False
                else:
                    print("Opció no vàlida.")
                Personaje2.Hechizo(Personaje1)
            elif opcio_accio == "3":    
                Personaje2.defender()
                print(f"{Personaje2.Nombre} se está defendiendo.")

            if Personaje1.Salud <= 0:
                print(f"{Personaje1.Nombre} ha sido derrotado. ¡{Personaje2.Nombre} gana el combate!")
            elif Personaje2.Salud <= 0:
                print(f"{Personaje2.Nombre} ha sido derrotado. ¡{Personaje1.Nombre} gana el combate!")

            break

