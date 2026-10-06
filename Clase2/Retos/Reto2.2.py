gente = [
    {"nombre": "Jamiro", "edad": 45},
    {"nombre": "Juan", "edad": 35},
    {"nombre": "Paco", "edad": 34},
    {"nombre": "Pepe", "edad": 14},
    {"nombre": "Pilar", "edad": 24},
    {"nombre": "Laura", "edad": 24},
    {"nombre": "Jenny", "edad": 10},
]
cortos = []

for i in gente:
    if(len(i["nombre"]) == 4):
        cortos.append(i["nombre"]);
        
print(cortos);