
i = 0;

while i < 5:
    try:    
        numero_usuario = int(input("Introduce un numero "));
        print("Has introducido un numero valido");
        break;
    except:
        i += 1;
        print("No has introducido un numero valido");