from Habitacion import *
from Arma import *
from Enemigo import *
from Elementos import *

def coger_pocion(pocion):

    if inventario["pocion"] == None:

        inventario["pocion"] == pocion

    else:

        print("No se puede coger esta poción porque ya tienes una. Deberías tirar la que tienes.")

    return inventario

def tirar_pocion():

    if inventario["pocion"] == None:

        print("No puedes tirar una poción porque no tienes ninguna")

    else:

        inventario["pocion"] == None

    return inventario

def coger_arma(arma):

    if inventario["arma"] == None:

        inventario["arma"] == arma

    else:

        print("No puedes coger este arma porque ya tienes una. Deberías tirar la que tienes.")

    return inventario

def tirar_arma():

    if inventario["arma"] == None:

        print("No puedes tirar un arma porque no tienes ninguna")

    else:

        inventario["arma"] == None

    return inventario

def coger_escudo(escudo):

    if inventario["escudo"] == None:

        inventario["escudo"] == escudo

    else:

        print("No puedes coger el escudo porque ya tienes uno.")

    return inventario

def tirar_escudo():

    if inventario["escudo"] == None:

        print("No puedes tirar el escudo porque no tienes ninguno")

    else:

        inventario["escudo"] == None

    return inventario

def regenerar_vida(vida, pocion):

    vida += pocion

    if vida >= 100:

        return 100

    else:

        return vida