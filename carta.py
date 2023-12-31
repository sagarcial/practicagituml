class Carta:
    def __init__(self, valor, pinta):
        self.pinta = pinta
        self.valor = valor
        self.pintas = []
    
    def mostrar_carta(self):
        return self.pinta, self.valor

    def obtener_valor(self):
        if self.valor == 'A':
            return 1
        if self.valor in ['J', 'Q', 'K']:
            return 10
        return int(self.valor)

class CartaFrancesa(Carta):
    pass

class CartaEspanola(Carta):
    pass
        