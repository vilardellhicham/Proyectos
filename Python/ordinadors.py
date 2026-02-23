class Portatil:

    def __init__(self, marca, model, mida_pantalla, te_ssd, ram):
        self.marca = marca
        self.model = model
        self.mida_pantalla = mida_pantalla
        self.te_ssd = te_ssd
        self.ram = ram

    def __str__(self):
        return f"Marca: {self.marca}, Model: {self.model}, Pantalla: {self.mida_pantalla}\", SSD: {self.te_ssd}, RAM: {self.ram}GB"


portatils = []
sortir = False

while not sortir:

    print("\n--- MENÚ ---")
    print("1. Donar alta portàtil")
    print("2. Mostrar Portàtils")
    print("3. Sortir")

    opcio = input("Escull una opció: ")

    match opcio:

        case "1":
            marca = input("Marca: ")
            model = input("Model: ")
            mida = float(input("Mida pantalla: "))
            ssd = input("Té SSD? (si/no): ")
            ram = int(input("RAM (GB): "))

            nou = Portatil(marca, model, mida, ssd, ram)
            portatils.append(nou)

            print("Portàtil afegit.")

        case "2":
            if len(portatils) == 0:
                print("No hi ha portàtils.")
            else:
                for p in portatils:
                    print(p)

        case "3":
            print("Sortint del programa...")
            sortir = True

        case _:
            print("Opció incorrecta.")