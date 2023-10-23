from src.Ejercicio5 import comprobarContraseña, mensajeSalida
import pytest

def test_cuentaAtras():
    with pytest.raises(NameError):
        comprobarContraseña("Prueba")
    assert comprobarContraseña("Contraseña") == "Contraseña"

def test_mensajeSalida():
    assert mensajeSalida("Contraseña") == "La contraseña Contraseña es correcta."