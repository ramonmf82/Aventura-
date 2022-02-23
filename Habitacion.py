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

    def mostrar_habitacion(self):

        print(f"\nTe encuentras en la habitación {self.numero}")

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

    def moverse_a(self, direccion):

        if self.numero == 0 and direccion == "sur":

            return 1

        elif self.numero == 1 and direccion == "sur":

            return 4

        elif self.numero == 1 and direccion == "norte":

            return 0

        elif self.numero == 1 and direccion == "este":

            return 2

        elif self.numero == 1 and direccion == "oeste":
        
            return 3

        elif self.numero == 2 and direccion == "oeste":

            return 1

        elif self.numero == 3 and direccion == "este":
        
            return 1

        elif self.numero == 4 and direccion == "norte":

            return 1

        elif self.numero == 4 and direccion == "sur":

            return 5
       
        else:

            print("No puedes ir en esa dirección")    
            return self.numero
