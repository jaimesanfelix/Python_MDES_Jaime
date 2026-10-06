def area_cuadrado(lado):
    """La funcion devuelve la area del cuadrado"""
    return lado * lado;

def area_triangulo(base, altura):
    """La funion devielve el area del triangulo"""
    return base * altura / 2;

area_total = area_cuadrado(10) + (5 * area_triangulo(2,4));
print(area_total);