from Arma import *
import random

class Personaje:

    def __init__(self, Raza, Nombre, Edad, Encargo,força, destresa, constitucio, intell, saviesa, carisma):
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

        self.salud = self.constitucio * 50
        self.mana = self.intell * 30
        

        self.Inventario = []

        self.arma_equipada = None
        self.nivell = 1
        self.defendiendo = False

    def recoger_arma(self, Arma):
            self.Inventario.append(Arma)
            print(f"{self.Nombre} ha recogido {Arma.Tipo}.")

    def equipar_arma(self):
        
        if not self.Inventario:
            print(f"{self.Nombre} no tiene armas para equipar.")
            return
        
        self.arma_equipada = self.Inventario[0]
        print(f"{self.Nombre} ha equipado {self.arma_equipada.Tipo}.")

    def defender(self):
        self.defendiendo = True
        print(f"{self.Nombre} se está defendiendo.")

    def atacar(self, Personaje):
        if self.arma_equipada is None or self.arma_equipada.Tipo == "Fisico":
            daño = self.força * (1 + self.arma_equipada.Daño / 100) if self.arma_equipada else self.força
        elif self.arma_equipada.Tipo == "Mágico":
            daño = self.arma_equipada.Daño * (self.intell / 100)

        if Personaje.esquivar() == True:
                daño = 0
                print(f"{Personaje.Nombre} ha esquivado el ataque de {self.Nombre}.")
        elif Personaje.defendiendo:
            daño *= 0.5
            print(f"{self.Nombre} ataca a {Personaje.Nombre} causando {daño:.2f} de daño.")
        else:        
           Personaje.Salud -= daño
           print(f"{self.Nombre} ataca a {Personaje.Nombre} causando {daño:.2f} de daño.")

    def regenerarvida(self):

        self.salud = self.salud + self.constitucio * 3

        if self.salud > self.constitucio * 50:
            self.salud = self.constitucio * 50

        print(f"{self.Nombre} ha regenerado vida. Salud actual: {self.salud}") 

    def regenerarmana(self):

        self.mana = self.mana + self.intell * 2

        if self.mana > self.intell * 30:
            self.mana = self.intell * 30

        print(f"{self.Nombre} ha regenerado mana. Mana actual: {self.mana}")
       
    def esquivar(self):
        
        esquivar = (self.destresa - 5) * 3.33

        if esquivar >= random.randint(1, 100):
            print(f"{self.Nombre} ha esquivado el ataque.")
            return True
        else:
            print(f"{self.Nombre} no ha podido esquivar el ataque.")
            return False

    def Hechizo(self, Personaje):
        if self.mana >= 10:
            daño = self.intell * 2
            if Personaje.esquivar() == True:
                daño = 0
                print(f"{Personaje.Nombre} ha esquivado el ataque de {self.Nombre}.")
            elif Personaje.defendiendo:
                daño *= 0.5
            else:        
                Personaje.Salud -= daño
            self.mana -= 10
            print(f"{self.Nombre} lanza un hechizo a {Personaje.Nombre} causando {daño:.2f} de daño.")
        else:
            print(f"{self.Nombre} no tiene suficiente mana para lanzar un hechizo.")

    def Personajeautomatico(Personaje):
        Personaje.Raza = random.choice(["Humano", "Elfo", "Enano", "Orco"])
        Personaje.Nombre = random.choice(["Phoenix", "Jett", "Sage", "Yoru", "Raze", "Breach", "Omen", "Viper", "Cypher", "Killjoy"])
        Personaje.Edad = random.randint(20, 100)
        Personaje.Encargo = random.choice(["Misión de rescate", "Búsqueda de tesoro", "Defensa de la ciudad", "Exploración de mazmorras"])
        Personaje.força = random.randint(5, 20)
        Personaje.destresa = random.randint(5, 20)
        Personaje.constitucio = random.randint(5, 20)
        Personaje.intell = random.randint(5, 20)
        Personaje.saviesa = random.randint(5, 20)
        Personaje.carisma = random.randint(5, 20)
        return Personaje(Personaje.Raza, Personaje.Nombre, Personaje.Edad, Personaje.Encargo, Personaje.força, Personaje.destresa, Personaje.constitucio, Personaje.intell, Personaje.saviesa, Personaje.carisma)
    
    def crearpersonaje(Personaje):
        Raza = input("Introduce la raza del personaje: ")
        Nombre = input("Introduce el nombre del personaje: ")
        Edad = int(input("Introduce la edad del personaje: "))
        Encargo = input("Introduce el encargo del personaje: ")
        força = int(input("Introduce la força del personaje (5-20): "))
        destresa = int(input("Introduce la destresa del personaje (5-20): "))
        constitucio = int(input("Introduce la constitución del personaje (5-20): "))
        intell = int(input("Introduce la inteligencia del personaje (5-20): "))
        saviesa = int(input("Introduce la saviesa del personaje (5-20): "))
        carisma = int(input("Introduce el carisma del personaje (5-20): "))

        return Personaje(Raza, Nombre, Edad, Encargo, força, destresa, constitucio, intell, saviesa, carisma)