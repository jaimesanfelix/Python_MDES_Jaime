contrasena = "mimamamemima";
longitud_minima = 8;
longitud_maxima = 20;

if(len(contrasena) < longitud_minima):
    print(f"La longitud de la contraseña es MUY CORTA debe de ser al menos {longitud_minima}");
elif(len(contrasena) > longitud_maxima):
    print(f"La longitud de la contraseña es DEMASIADO LARGA debe de ser maximo {longitud_maxima}");
else:
    print("La longitud de contraseña es VALIDA. Contraseña ACEPTADA");    