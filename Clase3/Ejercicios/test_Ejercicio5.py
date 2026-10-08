import Clase3.Ejercicios.Ejercicio5 as Ejercicio5


def test_precio_negativo():
    assert Ejercicio5.precio_final(5,5) == 2;
    
def test_precio_correcto():
    assert Ejercicio5.precio_final(10,5) == 5;