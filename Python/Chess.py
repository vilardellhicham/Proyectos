def pedir_no_vacio(mensaje):
    valido = False
    texto = ""
    while not valido:
        texto = input(mensaje).strip()
        if texto:
            valido = True
        else:
            print("Tienes que escribir un nombre")
    return texto

def pedir_color(mensaje):
    valido = False
    color = ""
    while not valido:
        c = input(mensaje).strip().lower()

        if c in ("b", "blanca", "blancas", "blanques"):
            color = "blancas"
            valido = True
        elif c in ("n", "negra", "negras", "negres"):
            color = "negras"
            valido = True
        else:
            print("Opción inválida. Escribe 'b' (blancas) o 'n' (negras).")
    return color

def crear_tablero_inicial():
    tablero = [
        ["t","c","a","q","k","a","c","t"],  # 8 (negras)
        ["p","p","p","p","p","p","p","p"],  # 7
        [".",".",".",".",".",".",".","."],  # 6
        [".",".",".",".",".",".",".","."],  # 5
        [".",".",".",".",".",".",".","."],  # 4
        [".",".",".",".",".",".",".","."],  # 3
        ["P","P","P","P","P","P","P","P"],  # 2
        ["T","C","A","K","Q","A","C","T"],  # 1 (blancas)
    ]
    return tablero
def imprimir_tablero(tablero):
    id = 0
    print ("A_B_C_D_E_F_G_H")
    for cas in(tablero):
        id += 1
        for col in(cas):
            print(col,end=" ")
        print (id)

jugador1 = pedir_no_vacio("Introduce el nombre del primer jugador: ")
jugador2 = pedir_no_vacio("Introduce el nombre del segundo jugador: ")

color_j1 = pedir_color(f"{jugador1}, Que color quieres jugar? (b=blancas / n=negras): ")
color_j2 = "negras" if color_j1 == "blancas" else "blancas"

print(f"{jugador1} jugara la partida con el equipo de las {color_j1}.")
print (f"{jugador2} jugara la partida con el equipo de la{color_j2}.")


tablero = crear_tablero_inicial()
imprimir_tablero(tablero)

COLUMNAS = "abcdefgh"
def convertir(casilla):
    col = COLUMNAS.index(casilla[0].lower())
    fila = 8 - int(casilla[1])
    return fila, col
