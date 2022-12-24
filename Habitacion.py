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

        elif self.numero == 3 and direccion == "arriba":
        
            return 6

        elif self.numero == 4 and direccion == "norte":

            return 1

        elif self.numero == 4 and direccion == "sur":

            return 5

        elif self.numero == 6 and direccion == "sur":

            return 7

        elif self.numero == 6 and direccion == "abajo":

            return 3
        
        elif self.numero == 7 and direccion == "norte":

            return 6

        elif self.numero == 7 and direccion == "sur":

            return 8

        elif self.numero == 7 and direccion == "oeste":

            return 29

        elif self.numero == 8 and direccion == "norte":

            return 7

        elif self.numero == 8 and direccion == "sur":

            return 9

        elif self.numero == 9 and direccion == "norte":

            return 8

        elif self.numero == 9 and direccion == "oeste":

            return 10
            
        elif self.numero == 10 and direccion == "sur":

            return 13

        elif self.numero == 10 and direccion == "este":
            
            return 9

        elif self.numero == 10 and direccion == "oeste":

            return 11

        elif self.numero == 11 and direccion == "sur":

            return 12    

        elif self.numero == 11 and direccion == "este":

            return 10

        elif self.numero == 12 and direccion == "norte":

            return 11

        elif self.numero == 12 and direccion == "este":

            return 13

        elif self.numero == 12 and direccion == "oeste":

            return 23

        elif self.numero == 13 and direccion == "norte":

            return 10

        elif self.numero == 13 and direccion == "sur":

            return 14

        elif self.numero == 13 and direccion == "oeste":

            return 12

        elif self.numero == 14 and direccion == "norte":

            return 13

        elif self.numero == 14 and direccion == "sur":

            return 17

        elif self.numero == 14 and direccion == "este":

            return 15

        elif self.numero == 15 and direccion == "sur":

            return 16

        elif self.numero == 15 and direccion == "este":

            return 14

        elif self.numero == 16 and direccion == "norte":

            return 15

        elif self.numero == 16 and direccion == "oeste":

            return 17

        elif self.numero == 17 and direccion == "norte":

            return 14

        elif self.numero == 17 and direccion == "este":

            return 16

        elif self.numero == 17 and direccion == "oeste":

            return 18

        elif self.numero == 18 and direccion == "este":

            return 17

        elif self.numero == 18 and direccion == "oeste":

            return 19

        elif self.numero == 19 and direccion == "este":

            return 18

        elif self.numero == 19 and direccion == "oeste":

            return 20

        elif self.numero == 20 and direccion == "norte":

            return 21

        elif self.numero == 20 and direccion == "este":

            return 19

        elif self.numero == 20 and direccion == "arriba":

            return 30

        elif self.numero == 21 and direccion == "norte":

            return 22

        elif self.numero == 21 and direccion == "sur":

            return 20

        elif self.numero == 22 and direccion == "norte":

            return 24

        elif self.numero == 22 and direccion == "sur":

            return 21

        elif self.numero == 22 and direccion == "este":

            return 23

        elif self.numero == 23 and direccion == "este":

            return 12

        elif self.numero == 23 and direccion == "oeste":

            return 22

        elif self.numero == 24 and direccion == "norte":

            return 25

        elif self.numero == 24 and direccion == "sur":

            return 22

        elif self.numero == 25 and direccion == "sur":

            return 24

        elif self.numero == 25 and direccion == "este":

            return 26

        elif self.numero == 26 and direccion == "norte":

            return 27

        elif self.numero == 26 and direccion == "oeste":

            return 25

        elif self.numero == 27 and direccion == "sur":

            return 26

        elif self.numero == 27 and direccion == "este":

            return 28

        elif self.numero == 28 and direccion == "este":

            return 29

        elif self.numero == 28 and direccion == "oeste":

            return 27

        elif self.numero == 29 and direccion == "este":

            return 7

        elif self.numero == 29 and direccion == "oeste":

            return 28
   
        else:

            print("No puedes ir en esa dirección")    
            return self.numero
