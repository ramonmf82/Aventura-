from Habitacion import *
from Funciones import *
from Arma import *
from Enemigo import *
from Elementos import *
import json

indice_habitacion = 0

while True:

    h[indice_habitacion].mostrar_habitacion()
    accion = input(">>> ").lower()
    
    if accion in frases_validas:

        if accion == "dir":

            print("\nDirectorio de frases válidas: ")
            print(json.dumps(frases_validas, sort_keys=False, indent=4))

        elif accion == "inv":

            print("\nInventario:")
            print(json.dumps(inventario, sort_keys=False, indent=4))  

        elif accion == "coger":

            if h[indice_habitacion].arma != None:

                coger_arma(h[indice_habitacion].arma)
                h[indice_habitacion].arma = None

            if h[indice_habitacion].escudo != None:

                coger_escudo(h[indice_habitacion].escudo)
                h[indice_habitacion].escudo = None

            if h[indice_habitacion].pocion != None:

                coger_pocion(h[indice_habitacion].pocion)
                h[indice_habitacion].pocion = None

        elif accion == "tirar arma":

            tirar_arma()

        elif accion == "tirar escudo":

            tirar_escudo()

        elif accion == "tirar pocion":

            tirar_pocion()

        else:    

            indice_habitacion = h[indice_habitacion].moverse_a(accion)

            if indice_habitacion == 5:

                break
    
    else:
        
        print("Acción inválida")
        h[indice_habitacion].mostrar_habitacion()

print("\nLlegaste a la habitación 5 ¡¡¡¡GANASTE!!!!\n")
