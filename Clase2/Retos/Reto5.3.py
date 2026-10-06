def contar_letra(texto, letra):
    duplicado = 0;
    for i in texto:
        if(i.lower() == letra.lower()):
            duplicado += 1;
    return duplicado;

print(contar_letra("miMamaMeMIMA", "a"));