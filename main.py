from Habitacion import *
from Funciones import *
from Arma import *
from Enemigo import *
from Elementos import *
import json

indice_habitacion = 0

h[indice_habitacion].mostrar_habitacion()

while True:

    direccion = input("Escribe la acción: ")

    direccion = direccion.lower()
    
    if direccion in frases_validas:

        if direccion == "dir":

            print("\nDirectorio de frases válidas: ")

            print(json.dumps(frases_validas, sort_keys=False, indent=4))
            
            h[indice_habitacion].mostrar_habitacion()

        elif direccion == "inv":

            print("\nInventario:")

            print(json.dumps(inventario, sort_keys=False, indent=4))
            
            h[indice_habitacion].mostrar_habitacion()

        else:    

            indice_habitacion = h[indice_habitacion].moverse_a(direccion)

            if indice_habitacion == 5:

                break

            h[indice_habitacion].mostrar_habitacion()
    
    else:
        
        print("Acción inválida")
        h[indice_habitacion].mostrar_habitacion()

print("\nLlegaste a la habitación 5 ¡¡¡¡GANASTE!!!!\n")
