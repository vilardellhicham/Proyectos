class Arma:

    #Constructor
    def __init__(self, Tipo, Dano, TipoDano):
        self.Tipo = Tipo
        self.Dano = Dano
        self.TipoDano = TipoDano

    def getTipo(self):
        return f"{self.Tipo}"
    def setTipo(self, NTipo):
        self.Tipo = NTipo

    def getDano(self):
        return self.Dano
    def setDano(self, NDano):
        self.Dano = NDano
    
    def getTipoDano(self):
        return self.TipoDano
    def setTipoDano(self, NTipoDano):
        self.TipoDano = NTipoDano

    def __str__(self):
        return f"Tipo de arma: {self.Tipo}, Daño del arma: {self.Dano}, Tipo de daño del arma: {self.TipoDano}"