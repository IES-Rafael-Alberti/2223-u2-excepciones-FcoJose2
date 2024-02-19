from src.Ejercicio4 import pedirNumero, mensajeSalida
import pytest

def test_pedirNumero(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')
    assert pedirNumero() == 5


    monkeypatch.setattr('builtins.input', lambda _: '0.5')
    with pytest.raises(ValueError):
        pedirNumero()

def test_mensajeSalida():
    assert mensajeSalida(3) == "Su numero es: 3"