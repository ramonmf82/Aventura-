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
    "pequeña": 10,
    "mediana": 25,
    "grande": 50
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
    "coger": "coger objeto",
    "tirar arma": "tirar arma",
    "tirar escudo": "tirar escudo",
    "tirar pocion": "tirar pocion"
}

    #numero, norte, sur, este, oeste, arriba, abajo, arma, escudo, pocion, enemigo, descripcion
h = [
    Habitacion(0, 0, 1, 0, 0, 0, 0, "cuchillo", None, None, None, None),
    Habitacion(1, 1, 1, 1, 1, 0, 0, "hacha", None, None, None, None),
    Habitacion(2, 0, 0, 0, 1, 0, 0, "espada", None, None, None, None),
    Habitacion(3, 0, 0, 1, 0, 1, 0, None, "escudo", None, None, None),
    Habitacion(4, 1, 1, 0, 0, 0, 0, None, None, "pocion", None, None),
    Habitacion(5, 0, 0, 0, 0, 0, 0, None, None, None, None, None),
    Habitacion(6, 0, 1, 0, 0, 0, 1, None, None, None, None, None),
    Habitacion(7, 1, 1, 0, 1, 0, 0, None, None, None, None, None),
    Habitacion(8, 1, 1, 0, 0, 0, 0, None, None, None, None, None),
    Habitacion(9, 1, 0, 0, 1, 0, 0, None, None, None, None, None),
    Habitacion(10, 0, 1, 1, 1, 0, 0, None, None, None, None, None),
    Habitacion(11, 0, 1, 1, 0, 0, 0, None, None, None, None, None),
    Habitacion(12, 1, 0, 1, 1, 0, 0, None, None, None, None, None),
    Habitacion(13, 1, 1, 0, 1, 0, 0, None, None, None, None, None),
    Habitacion(14, 1, 1, 1, 0, 0, 0, None, None, None, None, None),
    Habitacion(15, 0, 1, 1, 0, 0, 0, None, None, None, None, None),
    Habitacion(16, 1, 0, 0, 1, 0, 0, None, None, None, None, None),
    Habitacion(17, 1, 0, 1, 1, 0, 0, None, None, None, None, None),
    Habitacion(18, 0, 0, 1, 1, 0, 0, None, None, None, None, None),
    Habitacion(19, 0, 0, 1, 1, 0, 0, None, None, None, None, None),
    Habitacion(20, 1, 0, 1, 0, 1, 0, None, None, None, None, None),
    Habitacion(21, 1, 1, 0, 0, 0, 0, None, None, None, None, None),
    Habitacion(22, 1, 1, 1, 0, 0, 0, None, None, None, None, None),
    Habitacion(23, 0, 0, 1, 1, 0, 0, None, None, None, None, None),
    Habitacion(24, 1, 1, 0, 0, 0, 0, None, None, None, None, None),
    Habitacion(25, 0, 1, 1, 0, 0, 0, None, None, None, None, None),
    Habitacion(26, 1, 0, 0, 1, 0, 0, None, None, None, None, None),
    Habitacion(27, 0, 1, 1, 0, 0, 0, None, None, None, None, None),
    Habitacion(28, 0, 0, 1, 1, 0, 0, None, None, None, None, None),
    Habitacion(29, 0, 0, 1, 1, 0, 0, None, None, None, None, None)
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