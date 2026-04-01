from Arma import *
import random

class Personaje:

    def __init__(self, Raza, Nombre, Edad, Encargo, força, destresa, constitucio, intell, saviesa, carisma):
        self.Raza = Raza
        self.Nombre = Nombre
        self.Edad = Edad
        self.Encargo = Encargo

        self.força = força
        self.destresa = destresa
        self.constitucio = constitucio
        self.intell = intell
        self.saviesa = saviesa
        self.carisma = carisma

        self.aplicar_modificadores()

        self.saludmax = self.constitucio * 50
        self.manamax = self.intell * 30
        self.salud = self.saludmax
        self.mana = self.manamax

        self.Inventario = []
        self.arma_equipada = None
        self.nivell = 1
        self.defendiendo = False

    def aplicar_modificadores(self):
        pass

    def limitar_maxim(self):
        if self.força > 20:
            self.força = 20
        if self.destresa > 20:
            self.destresa = 20
        if self.constitucio > 20:
            self.constitucio = 20
        if self.intell > 20:
            self.intell = 20
        if self.saviesa > 20:
            self.saviesa = 20
        if self.carisma > 20:
            self.carisma = 20

    def recoger_arma(self, arma):
        self.Inventario.append(arma)
        print(f"{self.Nombre} ha recogido {arma.Tipo}.")

    def puede_equipar_arma(self, arma):
        if arma.TipoDano == "Mágico" and self.intell < 10:
            return False
        return True

    def equipar_arma(self):
        if not self.Inventario:
            print(f"{self.Nombre} no tiene armas para equipar.")
            return

        print(f"\nArmas de {self.Nombre}:")
        for i in range(len(self.Inventario)):
            print(str(i + 1) + ". " + str(self.Inventario[i]))

        opcio = input("Elige arma: ")
        if opcio.isdigit():
            pos = int(opcio) - 1
            if pos >= 0 and pos < len(self.Inventario):
                arma = self.Inventario[pos]
                if self.puede_equipar_arma(arma):
                    self.arma_equipada = arma
                    print(f"{self.Nombre} ha equipado {self.arma_equipada.Tipo}.")
                else:
                    print(f"{self.Nombre} no puede equipar esa arma.")
            else:
                print("Opción no válida.")
        else:
            print("Opción no válida.")

    def defender(self):
        self.defendiendo = True
        print(f"{self.Nombre} se está defendiendo.")

    def multiplicador_ataque(self):
        return 1

    def reduccion_defensa(self):
        return 0.5

    def atacar(self, objetivo):
        if self.arma_equipada is None or self.arma_equipada.TipoDano == "Fisico":
            if self.arma_equipada is None:
                daño = self.força
            else:
                daño = self.força * (1 + self.arma_equipada.Dano / 100)
        else:
            daño = self.arma_equipada.Dano * self.intell / 100

        daño = daño * self.multiplicador_ataque()

        if objetivo.esquivar() == True:
            print(f"{objetivo.Nombre} ha esquivado el ataque de {self.Nombre}.")
            return

        objetivo.recibir_dano(daño)
        print(f"{self.Nombre} ataca a {objetivo.Nombre} causando {daño:.2f} de daño.")

    def recibir_dano(self, daño):
        if self.defendiendo:
            daño = daño * self.reduccion_defensa()
        self.salud = self.salud - daño
        if self.salud < 0:
            self.salud = 0
        self.defendiendo = False

    def regenerarvida(self):
        self.salud = self.salud + self.constitucio * 3
        if self.salud > self.saludmax:
            self.salud = self.saludmax
        print(f"{self.Nombre} ha regenerado vida. Salud actual: {self.salud}")

    def regenerarmana(self):
        self.mana = self.mana + self.intell * 2
        if self.mana > self.manamax:
            self.mana = self.manamax
        print(f"{self.Nombre} ha regenerado mana. Mana actual: {self.mana}")

    def esquivar(self):
        prob = (self.destresa - 5) * 3.33
        if random.randint(1, 100) <= prob:
            print(f"{self.Nombre} ha esquivado el ataque.")
            return True
        else:
            print(f"{self.Nombre} no ha podido esquivar el ataque.")
            return False

    def Hechizo(self, objetivo):
        if self.mana >= 10:
            daño = self.intell * 2
            if objetivo.esquivar() == True:
                print(f"{objetivo.Nombre} ha esquivado el hechizo de {self.Nombre}.")
                return
            objetivo.recibir_dano(daño)
            self.mana = self.mana - 10
            print(f"{self.Nombre} lanza un hechizo a {objetivo.Nombre} causando {daño:.2f} de daño.")
        else:
            print(f"{self.Nombre} no tiene suficiente mana para lanzar un hechizo.")

    def subir_nivel(self):
        self.nivell = self.nivell + 1
        print(f"{self.Nombre} ha subido al nivel {self.nivell}.")

    def __str__(self):
        texto = "Raza: " + self.Raza + "\n"
        texto = texto + "Nombre: " + self.Nombre + "\n"
        texto = texto + "Edad: " + str(self.Edad) + "\n"
        texto = texto + "Encargo: " + self.Encargo + "\n"
        texto = texto + "Força: " + str(self.força) + "\n"
        texto = texto + "Destresa: " + str(self.destresa) + "\n"
        texto = texto + "Constitució: " + str(self.constitucio) + "\n"
        texto = texto + "Intel·ligència: " + str(self.intell) + "\n"
        texto = texto + "Saviesa: " + str(self.saviesa) + "\n"
        texto = texto + "Carisma: " + str(self.carisma) + "\n"
        texto = texto + "Salud: " + str(self.salud) + "\n"
        texto = texto + "Mana: " + str(self.mana) + "\n"
        texto = texto + "Nivel: " + str(self.nivell)
        return texto


class Humano(Personaje):
    def __init__(self, Nombre, Edad, Encargo, força, destresa, constitucio, intell, saviesa, carisma):
        super().__init__("Humano", Nombre, Edad, Encargo, força, destresa, constitucio, intell, saviesa, carisma)

    def aplicar_modificadores(self):
        self.força = self.força + 1
        self.destresa = self.destresa + 1
        self.constitucio = self.constitucio + 1
        self.intell = self.intell + 1
        self.saviesa = self.saviesa + 1
        self.carisma = self.carisma + 1
        self.limitar_maxim()


class Elf(Personaje):
    def __init__(self, Nombre, Edad, Encargo, força, destresa, constitucio, intell, saviesa, carisma):
        super().__init__("Elf", Nombre, Edad, Encargo, força, destresa, constitucio, intell, saviesa, carisma)

    def aplicar_modificadores(self):
        self.destresa = self.destresa + 2
        self.intell = self.intell + 2
        self.limitar_maxim()

    def regenerarmana(self):
        self.mana = self.mana + self.intell * 3
        if self.mana > self.manamax:
            self.mana = self.manamax
        print(f"{self.Nombre} ha regenerado mana. Mana actual: {self.mana}")


class Orco(Personaje):
    def __init__(self, Nombre, Edad, Encargo, força, destresa, constitucio, intell, saviesa, carisma):
        super().__init__("Orco", Nombre, Edad, Encargo, força, destresa, constitucio, intell, saviesa, carisma)

    def aplicar_modificadores(self):
        self.força = self.força + 3
        self.constitucio = self.constitucio + 1
        self.limitar_maxim()

    def puede_equipar_arma(self, arma):
        if arma.TipoDano == "Mágico":
            return False
        return True

    def multiplicador_ataque(self):
        return 1.1


class Enano(Personaje):
    def __init__(self, Nombre, Edad, Encargo, força, destresa, constitucio, intell, saviesa, carisma):
        super().__init__("Enano", Nombre, Edad, Encargo, força, destresa, constitucio, intell, saviesa, carisma)

    def aplicar_modificadores(self):
        self.constitucio = self.constitucio + 4
        self.destresa = self.destresa - 1
        self.limitar_maxim()

    def reduccion_defensa(self):
        return 0.25

    def regenerarvida(self):
        self.salud = self.salud + self.constitucio * 4
        if self.salud > self.saludmax:
            self.salud = self.saludmax
        print(f"{self.Nombre} ha regenerado vida. Salud actual: {self.salud}")


def crear_por_raza(Raza, Nombre, Edad, Encargo, força, destresa, constitucio, intell, saviesa, carisma):
    if Raza == "Humano":
        return Humano(Nombre, Edad, Encargo, força, destresa, constitucio, intell, saviesa, carisma)
    elif Raza == "Elf":
        return Elf(Nombre, Edad, Encargo, força, destresa, constitucio, intell, saviesa, carisma)
    elif Raza == "Orco":
        return Orco(Nombre, Edad, Encargo, força, destresa, constitucio, intell, saviesa, carisma)
    elif Raza == "Enano":
        return Enano(Nombre, Edad, Encargo, força, destresa, constitucio, intell, saviesa, carisma)
    else:
        return Personaje(Raza, Nombre, Edad, Encargo, força, destresa, constitucio, intell, saviesa, carisma)


def Personajeautomatico():
    raza = random.choice(["Humano", "Elf", "Enano", "Orco"])
    nombre = random.choice(["Phoenix", "Jett", "Sage", "Yoru", "Raze", "Breach", "Omen", "Viper", "Cypher", "Killjoy"])
    edad = random.randint(20, 100)
    encargo = random.choice(["Misión de rescate", "Búsqueda de tesoro", "Defensa de la ciudad", "Exploración de mazmorras"])
    força = random.randint(5, 10)
    destresa = random.randint(5, 10)
    constitucio = random.randint(5, 10)
    intell = random.randint(5, 10)
    saviesa = random.randint(5, 10)
    carisma = random.randint(5, 10)
    return crear_por_raza(raza, nombre, edad, encargo, força, destresa, constitucio, intell, saviesa, carisma)


def crearpersonaje():
    Raza = input("Introduce la raza del personaje (Humano, Elf, Orco, Enano): ")
    Nombre = input("Introduce el nombre del personaje: ")
    Edad = int(input("Introduce la edad del personaje: "))
    Encargo = input("Introduce el encargo del personaje: ")
    força = int(input("Introduce la força del personaje (5-20): "))
    destresa = int(input("Introduce la destresa del personaje (5-20): "))
    constitucio = int(input("Introduce la constitución del personaje (5-20): "))
    intell = int(input("Introduce la inteligencia del personaje (5-20): "))
    saviesa = int(input("Introduce la saviesa del personaje (5-20): "))
    carisma = int(input("Introduce el carisma del personaje (5-20): "))
    return crear_por_raza(Raza, Nombre, Edad, Encargo, força, destresa, constitucio, intell, saviesa, carisma)
