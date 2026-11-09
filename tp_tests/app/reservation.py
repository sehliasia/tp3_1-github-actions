class Stock:
    def __init__(self, quantite):
        self.quantite = quantite

    def retirer(self, quantite):
        if quantite <= 0:
            raise ValueError("La quantité doit être positive")

        if quantite > self.quantite:
            return False

        self.quantite -= quantite
        return True

class Reservation:
    def __init__(self, stock):
        self.stock = stock

    def reserver(self, quantite):
        resultat = self.stock.retirer(quantite)

        if resultat:
            return "confirmee"

        return "refusee"