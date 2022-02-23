class Arma:

    def __init__(self, ataque, defensa):

        self.ataque = ataque
        self.defensa = defensa

    def atacar(self):

        print(f"atacando. te he quitado {self.ataque} de vida")

    def defender(self):

        print(f"defendiendo. te he ahorrado {self.defensa} de vida")