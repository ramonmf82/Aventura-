from Habitacion import *
from Arma import *
from Enemigo import *

inventario = {
    "vida": 100,
    "pocion": None,
    "arma": None,
    "escudo": None
}

pocion = {
    "Poción Pequeña": 10,
    "Poción Mediana": 25,
    "Poción Grande": 50
}

frases_validas = {
    "dir": "ver directorio",
    "inv": "ver inventario",
    "norte": "ir al norte", 
    "sur": "ir al sur",
    "este": "ir al este",
    "oeste": "ir al oeste",
    "arriba": "ir arriba",
    "abajo": "ir abajo",
    "coger": "coger objeto"
}

    #numero, norte, sur, este, oeste, arriba, abajo, arma, escudo, pocion, enemigo, descripcion
h = [
    Habitacion(0, 0, 1, 0, 0, 0, 0, "cuchillo", None, None, None, None),
    Habitacion(1, 1, 1, 1, 1, 0, 0, "hacha", None, None, None, None),
    Habitacion(2, 0, 0, 0, 1, 0, 0, "espada", None, None, None, None),
    Habitacion(3, 0, 0, 1, 0, 0, 0, None, "escudo", None, None, None),
    Habitacion(4, 1, 1, 0, 0, 0, 0, None, None, "pocion", None, None),
    Habitacion(5, 0, 0, 0, 0, 0, 0, None, None, None, None, None)
]

arma = {
    "cuchillo": Arma(1, 0),
    "hacha": Arma(4, -1),
    "espada": Arma(7, -2),
    "escudo": Arma(0, 10)
}

enemigo = {
    "orco": Enemigo(1, 0, "cuchillo", 5),
    "troll": Enemigo(4, 2, "hacha", 15),
    "mago": Enemigo(10, 5, "espada", 50)
}