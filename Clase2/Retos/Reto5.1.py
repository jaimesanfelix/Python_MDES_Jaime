def ultimo_caracter(texto):
    if(type(texto) != str):
        return "Debo ser ejecutada con un string";
    else:
        return texto[-1];

print(ultimo_caracter("Hola"))