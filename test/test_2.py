from src.Ejercicio2 import numImpares, mensajeSalida
import pytest

def test_numImpares():
    with pytest.raises(ValueError):
        numImpares(-2)
    assert numImpares(10) == [1, 3, 5, 7, 9]

def test_mensajeSalida():
     assert mensajeSalida([1, 3, 5, 7, 9]) == "Numeros impares: [1, 3, 5, 7, 9]"