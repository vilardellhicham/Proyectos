from Arma import *
from Personaje import *

Personaje1 = None
Personaje2 = None


def crear_armas_base(personaje):
    personaje.recoger_arma(Arma("Espada", 30, "Fisico"))
    personaje.recoger_arma(Arma("Hacha", 40, "Fisico"))
    personaje.recoger_arma(Arma("Bastón", 35, "Mágico"))


def main():
    global Personaje1, Personaje2
    opcio = ""

    while opcio != "4":
        print("\n========= JOC RPG =========")
        print("1. Crear personatges")
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
                    Personaje1 = crearpersonaje()
                elif opcio_creacio == "2":
                    Personaje1 = Personajeautomatico()
                else:
                    print("Opció no vàlida.")

                if Personaje1 != None:
                    crear_armas_base(Personaje1)

                print("Jugador 2 - Crear personaje tu mismo o automaticamente")
                print("1. Crear personaje tu mismo")
                print("2. Crear personaje automáticamente")
                opcio_creacio = input("Tria una opció: ")
                if opcio_creacio == "1":
                    Personaje2 = crearpersonaje()
                elif opcio_creacio == "2":
                    Personaje2 = Personajeautomatico()
                else:
                    print("Opció no vàlida.")

                if Personaje2 != None:
                    crear_armas_base(Personaje2)

            case "2":
                if Personaje1 == None or Personaje2 == None:
                    print("Primero tienes que crear los personajes.")
                else:
                    print("\nJugador 1:")
                    print(Personaje1)
                    print("\nJugador 2:")
                    print(Personaje2)

            case "3":
                if Personaje1 == None or Personaje2 == None:
                    print("Primero tienes que crear los personajes.")
                else:
                    combatsimple()

            case "4":
                print("Sortint del joc...")

            case _:
                print("Opció no vàlida.")


def turno(atacante, defensor):
    print("\nTurno de " + atacante.Nombre)
    print("1. Cambiar arma")
    print("2. Atacar")
    print("3. Lanzar hechizo")
    print("4. Defender")
    opcio_accio = input("Tria una opció: ")

    if opcio_accio == "1":
        atacante.equipar_arma()
        print("1. Atacar")
        print("2. Lanzar hechizo")
        print("3. Defender")
        opcio_accio = input("Tria una opció: ")

    if opcio_accio == "1":
        atacante.atacar(defensor)
    elif opcio_accio == "2":
        atacante.Hechizo(defensor)
    elif opcio_accio == "3" or opcio_accio == "4":
        atacante.defender()
    else:
        print("Opció no vàlida.")

    atacante.regenerarvida()
    atacante.regenerarmana()


def combatsimple():
    global Personaje1, Personaje2
    print("\nComença el combat simple entre Jugador 1 i Jugador 2!")

    while Personaje1.salud > 0 and Personaje2.salud > 0:
        turno(Personaje1, Personaje2)
        if Personaje2.salud <= 0:
            print(f"{Personaje2.Nombre} ha sido derrotado. ¡{Personaje1.Nombre} gana el combate!")
            break

        turno(Personaje2, Personaje1)
        if Personaje1.salud <= 0:
            print(f"{Personaje1.Nombre} ha sido derrotado. ¡{Personaje2.Nombre} gana el combate!")
            break


main()
