def cuentaCaracteres(palabra):
    if(type(palabra) != str):
        return "Debo ser ejecutada con un string";
    else:
        return len(palabra);

print(cuentaCaracteres("Hola mundo"));
print(cuentaCaracteres(2432));