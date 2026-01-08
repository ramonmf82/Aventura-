from Habitacion import *
from Arma import *
from Enemigo import *

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

    #self, numero, norte, norte_sig, sur, sur_sig, este, este_sig, oeste, oeste_sig, arriba, arriba_sig, abajo, abajo_sig, arma, escudo, pocion, enemigo, descripcion
h = [
    Habitacion(0, 0, 1, 0, 0, 0, 0, "cuchillo", None, None, None, None),
    Habitacion(1, 0, 4, 3, 2, 0, 0, "hacha", None, None, None, None),
    Habitacion(2, 0, 0, 1, 0, 0, 0, "espada", None, None, None, None),
    Habitacion(3, 0, 0, 0, 1, 6, 0, None, "escudo", None, None, None),
    Habitacion(4, 1, 5, 0, 0, 0, 0, None, None, "pocion", None, None),
    Habitacion(5, 0, 0, 0, 0, 0, 0, None, None, None, None, None),
    Habitacion(6, 0, 7, 0, 0, 0, 3, None, None, None, None, None),
    Habitacion(7, 6, 8, 0, 29, 0, 0, None, None, None, None, None),
    Habitacion(8, 7, 9, 0, 0, 0, 0, None, None, None, None, None),
    Habitacion(9, 8, 0, 0, 10, 0, 0, None, None, None, None, None),
    Habitacion(10, 0, 13, 9, 11, 0, 0, None, None, None, None, None),
    Habitacion(11, 0, 12, 10, 0, 0, 0, None, None, None, None, None),
    Habitacion(12, 11, 0, 13, 23, 0, 0, None, None, None, None, None),
    Habitacion(13, 10, 14, 0, 12, 0, 0, None, None, None, None, None),
    Habitacion(14, 13, 17, 15, 0, 0, 0, None, None, None, None, None),
    Habitacion(15, 0, 16, 14, 0, 0, 0, None, None, None, None, None),
    Habitacion(16, 15, 0, 0, 17, 0, 0, None, None, None, None, None),
    Habitacion(17, 14, 0, 16, 18, 0, 0, None, None, None, None, None),
    Habitacion(18, 0, 0, 17, 19, 0, 0, None, None, None, None, None),
    Habitacion(19, 0, 0, 18, 20, 0, 0, None, None, None, None, None),
    Habitacion(20, 21, 0, 19, 0, 30, 0, None, None, None, None, None),
    Habitacion(21, 22, 20, 0, 0, 0, 0, None, None, None, None, None),
    Habitacion(22, 24, 21, 23, 0, 0, 0, None, None, None, None, None),
    Habitacion(23, 0, 0, 12, 22, 0, 0, None, None, None, None, None),
    Habitacion(24, 25, 22, 0, 0, 0, 0, None, None, None, None, None),
    Habitacion(25, 0, 24, 26, 0, 0, 0, None, None, None, None, None),
    Habitacion(26, 27, 0, 0, 25, 0, 0, None, None, None, None, None),
    Habitacion(27, 0, 26, 28, 0, 0, 0, None, None, None, None, None),
    Habitacion(28, 0, 0, 29, 27, 0, 0, None, None, None, None, None),
    Habitacion(29, 0, 0, 7, 28, 0, 0, None, None, None, None, None)
]

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