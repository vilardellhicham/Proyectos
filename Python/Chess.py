COLUMNAS = "abcdefgh"
VACIO = "[.]"


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
        ["[t]","[c]","[a]","[q]","[k]","[a]","[c]","[t]"],  # 8 (negras)
        ["[p]","[p]","[p]","[p]","[p]","[p]","[p]","[p]"],  # 7
        [VACIO,VACIO,VACIO,VACIO,VACIO,VACIO,VACIO,VACIO],  # 6
        [VACIO,VACIO,VACIO,VACIO,VACIO,VACIO,VACIO,VACIO],  # 5
        [VACIO,VACIO,VACIO,VACIO,VACIO,VACIO,VACIO,VACIO],  # 4
        [VACIO,VACIO,VACIO,VACIO,VACIO,VACIO,VACIO,VACIO],  # 3
        ["[P]","[P]","[P]","[P]","[P]","[P]","[P]","[P]"],  # 2
        ["[T]","[C]","[A]","[K]","[Q]","[A]","[C]","[T]"],  # 1 (blancas)
    ]
    return tablero


def imprimir_tablero(tablero):
    print(" A   B   C   D   E   F   G   H")
    fila_num = 8
    for fila in tablero:
        for pieza in fila:
            print(pieza, end=" ")
        print(fila_num)
        fila_num -= 1


def casilla_valida(c):
    c = c.strip().lower()
    return len(c) == 2 and c[0] in COLUMNAS and c[1] in "12345678"


def convertir(casilla):
    col = COLUMNAS.index(casilla[0].lower())
    fila = 8 - int(casilla[1])
    return fila, col


def pedir_jugada_una_linea(mensaje="Jugada (ej: e2 e4): "):
    valido = False
    while not valido:
        j = input(mensaje).strip().lower()
        partes = j.split()

        if len(partes) != 2:
            print("Formato invalido. Usa: e2 e4")
            continue

        origen, destino = partes[0], partes[1]

        if not casilla_valida(origen) or not casilla_valida(destino):
            print("Casillas invalidas. Usa letras a-h y números 1-8 (ej: e2 e4).")
            continue

        valido = True
        return origen, destino


def es_blanca(pieza):
    return pieza != VACIO and pieza[1].isupper()


def es_negra(pieza):
    return pieza != VACIO and pieza[1].islower()


def mov_peon_hacia_delante(tablero, origen, destino):
    f1, c1 = convertir(origen)
    f2, c2 = convertir(destino)

    pieza = tablero[f1][c1]
    if pieza not in ("[P]", "[p]"):
        return False

    if c1 != c2:
        return False

    dir = -1 if pieza == "[P]" else 1
    fila_inicial = 6 if pieza == "[P]" else 1

    if f2 == f1 + dir and tablero[f2][c2] == VACIO:
        tablero[f2][c2] = pieza
        tablero[f1][c1] = VACIO
        return True

    if f1 == fila_inicial and f2 == f1 + 2 * dir:
        if tablero[f1 + dir][c1] == VACIO and tablero[f2][c2] == VACIO:
            tablero[f2][c2] = pieza
            tablero[f1][c1] = VACIO
            return True

    return False


def camino_libre_recto(tablero, f1, c1, f2, c2):
    if f1 != f2 and c1 != c2:
        return False

    df = 0 if f1 == f2 else (1 if f2 > f1 else -1)
    dc = 0 if c1 == c2 else (1 if c2 > c1 else -1)

    f, c = f1 + df, c1 + dc
    while (f, c) != (f2, c2):
        if tablero[f][c] != VACIO:
            return False
        f += df
        c += dc
    return True


def mov_torre(tablero, origen, destino):
    f1, c1 = convertir(origen)
    f2, c2 = convertir(destino)

    pieza = tablero[f1][c1]
    if pieza not in ("[T]", "[t]"):
        return False

    if not camino_libre_recto(tablero, f1, c1, f2, c2):
        return False

    destino_pieza = tablero[f2][c2]
    if destino_pieza != VACIO:
        if (es_blanca(pieza) and es_blanca(destino_pieza)) or (es_negra(pieza) and es_negra(destino_pieza)):
            return False

    tablero[f2][c2] = pieza
    tablero[f1][c1] = VACIO
    return True


def mov_rey(tablero, origen, destino):
    f1, c1 = convertir(origen)
    f2, c2 = convertir(destino)

    pieza = tablero[f1][c1]
    if pieza not in ("[K]", "[k]"):  # rey blanco y rey negro
        return False

    df = abs(f2 - f1)
    dc = abs(c2 - c1)

    # Solo se mueve 1 casilla en cualquier dirección
    if df > 1 or dc > 1 or (df == 0 and dc == 0):
        return False

    destino_pieza = tablero[f2][c2]
    if destino_pieza != VACIO:
        # No puede capturar pieza del mismo color
        if (es_blanca(pieza) and es_blanca(destino_pieza)) or (es_negra(pieza) and es_negra(destino_pieza)):
            return False

    tablero[f2][c2] = pieza
    tablero[f1][c1] = VACIO
    return True


def mover(tablero, origen, destino):
    if mov_peon_hacia_delante(tablero, origen, destino):
        return True
    if mov_torre(tablero, origen, destino):
        return True
    if mov_rey(tablero, origen, destino):
        return True
    return False


def turno(tablero):
    movido = False
    while not movido:
        origen, destino = pedir_jugada_una_linea("Jugada (ej: e2 e4): ")

        try:
            movido = mover(tablero, origen, destino)
        except (ValueError, IndexError):
            movido = False

        if not movido:
            print("Movimiento invalido. Intenta otra vez.")


def main():
    jugador1 = pedir_no_vacio("Introduce el nombre del primer jugador: ")
    jugador2 = pedir_no_vacio("Introduce el nombre del segundo jugador: ")

    color_j1 = pedir_color(f"{jugador1}, ¿qué color quieres jugar? (b=blancas / n=negras): ")
    color_j2 = "negras" if color_j1 == "blancas" else "blancas"

    print(f"{jugador1} jugará la partida con el equipo de las {color_j1}.")
    print(f"{jugador2} jugará la partida con el equipo de las {color_j2}.")

    tablero = crear_tablero_inicial()
    imprimir_tablero(tablero)

    turno(tablero)
    imprimir_tablero(tablero)


if __name__ == "__main__":
    main()
