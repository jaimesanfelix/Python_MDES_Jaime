tipo = "Coche";
peso = 1500;
if(peso > 5000):
    tipo = "Vehículo pesado";
elif(peso > 2000):
    tipo = "Vehículo pesadito";
elif(peso > 1000 and peso < 2000):
    tipo = "Vehículo mediano";
else:
    tipo = "Vehículo mediano";

print(tipo);