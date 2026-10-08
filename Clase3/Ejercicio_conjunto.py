nota = 4
# if(nota1 < 5 and nota2 > 5 and nota3 > 9):
#     print("No todos han aprovado")
# elif(nota1 < 5 or nota2 > 5 or nota3 > 9):
#     print("Algunos alumnos han aprovado")
# else

if(nota < 5):
    print("El alumno ha suspendido")
elif(nota > 5 and nota < 9):
    print("El alumno a aprovado con menos de un sobresaliente")
else:
    print("El alumno a aprovado con un sobresaliente")