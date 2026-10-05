gente = [
    {"nombre": "Jamiro", "edad": 45},
    {"nombre": "Juan", "edad": 35},
    {"nombre": "Paco", "edad": 34},
    {"nombre": "Pepe", "edad": 14},
    {"nombre": "Pilar", "edad": 24},
    {"nombre": "Laura", "edad": 24},
    {"nombre": "Jenny", "edad": 10},
]
# p = input("Como te llamas? ")
p = gente[3]["edad"];
# p["edad"]
if(p >= 18):
    print("Es mayor")
elif(p < 18):
    print("Es menor")