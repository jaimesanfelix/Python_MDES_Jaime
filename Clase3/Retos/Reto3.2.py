try:
    numero1 = float(input("Introduce un numero para dividir "))
    numero2 = float(input("Introduce el otro numero "));
    resultado = numero1 / numero2;
    print(resultado)
except:
    print("No se pudo realizar la división");
finally:
    print("Proceso finalizado")