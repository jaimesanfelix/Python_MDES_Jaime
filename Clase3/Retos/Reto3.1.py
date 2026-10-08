numero1 = int(input("Introduce un numero para dividir "));
numero2 = int(input("Introduce el otro numero "));

try:
    resultado = numero1/numero2;
    print(resultado);
except ZeroDivisionError:
    print("No se puede dividir por cero");