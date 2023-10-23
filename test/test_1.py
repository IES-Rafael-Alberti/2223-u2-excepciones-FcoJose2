from src.Ejercicio1 import contarEdad, mensajeSalida
import pytest



def test_contarEdad():
    with pytest.raises(ValueError):
        contarEdad(-2)
    assert contarEdad(18) == "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]"

def test_mensajeSalida():
     assert mensajeSalida([1, 2, 3]) == "Años cumplidos: [1, 2, 3]"