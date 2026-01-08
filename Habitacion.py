from Arma import *

class Habitacion:
    def __init__(self, numero, norte, sur, este, oeste, arriba, abajo, arma, escudo, pocion, enemigo, descripcion):
        self.numero = numero
        self.norte = norte
        self.sur = sur
        self.este = este
        self.oeste = oeste
        self.arriba = arriba
        self.abajo = abajo
        self.arma = arma
        self.escudo = escudo
        self.pocion = pocion
        self.enemigo = enemigo
        self.descripcion = descripcion

    def moverse_a(self, direccion):
        if self.norte and direccion == "norte":
            return self.norte
        elif self.sur and direccion == "sur":
            return self.sur
        elif self.este and direccion == "este":
            return self.este
        elif self.oeste and direccion == "oeste":
            return self.oeste
        elif self.arriba and direccion == "arriba":
            return self.arriba
        elif self.abajo and direccion == "abajo":
            return self.abajo
        else:
            print("No puedes ir en esa dirección")    
            return self.numero

    def mostrar_habitacion(self):
        print(f"\nTe encuentras en la habitación {self.numero}")
        print(self.descripcion)
        if self.norte:
            print("Puedes ir hacia el Norte")
        if self.sur:
            print("Puedes ir hacia el Sur")
        if self.este:
            print("Puedes ir hacia el Este")
        if self.oeste:
            print("Puedes ir hacia el Oeste")
        if self.arriba:
            print("Puedes ir hacia Arriba")
        if self.abajo:
            print("Puedes ir hacia Abajo")
        if self.arma:
            print(f"Hay un(a) {self.arma} en la habitación")
        if self.escudo:
            print(f"Hay un {self.escudo} en la habitación")
        if self.pocion:
            print(f"Hay una {self.pocion} en la habitación")
