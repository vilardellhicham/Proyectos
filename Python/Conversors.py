def detectar_base(texto):
    if texto.startswith("0b"): return 2
    if texto.startswith("0o"): return 8
    if texto.startswith("0x"): return 16
    return 10

def validar(texto, base):
    validos = "0123456789ABCDEF"
    limpio = texto[2:] if base != 10 else texto
    
    if not limpio:
        return False
    
    for c in limpio.upper():
        if c not in validos[:base]:
            return False
    return True

def a_decimal(texto, base):
    if base != 10:
        texto = texto[2:]
    
    letras = "0123456789ABCDEF"
    total = 0
    
    for c in texto.upper()[::-1]:
        total = total * base + letras.index(c)
    
    return total

def de_decimal(num, base):
    if num == 0: return "0"
    
    letras = "0123456789ABCDEF"
    resultado = ""
    
    while num > 0:
        resultado = letras[num % base] + resultado
        num //= base
    
    return resultado

print("1. Decimal")
print("2. Binari")
print("3. Octal")
print("4. Hexadecimal")
opcion = input("Escull la base d'entrada (1-4): ")

bases = {"1": 10, "2": 2, "3": 8, "4": 16}
prefixos = {10: "", 2: "0b", 8: "0o", 16: "0x"}

if opcion not in bases:
    print("Opcio no valida.")
else:
    base_entrada = bases[opcion]
    entrada = input("Introdueix un número: ")
    
    if validar(entrada, base_entrada):
        dec = a_decimal(entrada, base_entrada)
        
        print(f"Decimal: {dec}")
        print(f"Binari: 0b{de_decimal(dec, 2)}")
        print(f"Octal: 0o{de_decimal(dec, 8)}")
        print(f"Hexadecimal: 0x{de_decimal(dec, 16)}")
    else:
        print("Error: Numero no valid.")
