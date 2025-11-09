#Llamada a las demas funciones
from Funciones  import  calefactor
from Funciones  import  alarma_co2 
from Funciones  import  puerta_faceid
from Funciones  import  aspersor
from Tiempo import parse_hhmm
from Tiempo import siguiente_minuto
#Funcion Menu principal

print("\n--- DOMOTIC HOUSE ---")
print("1. Calefactor automatico")
print("2. Alarma de CO2")
print("3. Puerta con Face ID")
print("4. Aspersor automatico")
print("5. Salir")

opcion = input("Seleccione una opcion: ")

if opcion == "1":
    calefactor()
elif opcion == "2":
    alarma_co2()
elif opcion == "3":
    puerta_faceid()
elif opcion == "4":
    aspersor()
elif opcion == "5":
    print("Saliendo del programa...")
else:
    print("Opcion incorrecta.")