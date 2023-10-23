from src.Ejercicio3 import cuentaAtras, mensajeSalida
import pytest

def test_cuentaAtras():
    with pytest.raises(ValueError):
        cuentaAtras(-2)
    assert cuentaAtras(9) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def test_mensajeSalida():
     assert mensajeSalida([3, 2, 1]) == "Cuenta atrás de los numeros: [3, 2, 1]"