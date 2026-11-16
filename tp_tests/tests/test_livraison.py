from app.livraison import frais_livraison

def test_livraison_panier_ordinaire():
    montant = 120
    resultat = frais_livraison(montant)
    assert resultat == 25

def test_livraison_299():
    assert frais_livraison(299) == 25

def test_livraison_300():
    assert frais_livraison(300) == 0

def test_livraison_301():
    assert frais_livraison(301) == 0
def test_livraison_panier_nul():
    assert frais_livraison(0) == 25
    
import pytest
def test_livraison_montant_negatif():
    with pytest.raises(ValueError):
        frais_livraison(-1)