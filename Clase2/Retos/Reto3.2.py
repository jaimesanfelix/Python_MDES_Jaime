# contador = 5;
# i = 0
# piramide = ""
# while i < 5:
#     piramide += str(contador);
#     contador -= 1;
#     i += 1;
#     print(piramide);
    
lista = [1,2,3,4,5];

i = 5;
piramide = "";
while i > 0:
    piramide += str(lista[i-1]);
    i -= 1;   
