import pytest
from unittest.mock import patch
from app.surveillance import surveiller
def test_alerte_envoyee():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.15)

        assert resultat == "alerte"
        notifier.assert_called_once_with("Taux eleve")
def test_aucune_alerte():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.05)

        assert resultat == "ok"
        notifier.assert_not_called()

def test_seuil_exact():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.10)

        assert resultat == "ok"
        notifier.assert_not_called()
def test_erreur_notification():
    with patch("app.surveillance.envoyer_notification") as notifier:
        notifier.side_effect = RuntimeError("Service non configure")

        with pytest.raises(RuntimeError):
            surveiller(0.15)

from app.notifications import envoyer_notification

def test_notification_non_configuree():
    with pytest.raises(RuntimeError, match="Service non configure"):
        envoyer_notification("Test")