# Programa Registro de Calificaciones escolares el programa solicite al usuario ingresar las calificaciones de las materias Español, Matemáticas, Ciencias y Sociales. El programa muestra en pantalla las calificaciones ingresadas y calcular el promedio total de las materias.

ciencias = float(input("Ingrese la calificación de Ciencias: "))
espanol = float(input("Ingrese la calificacion para Español: "))
matematicas = float(input("Ingrese la calificacion para Matematicas: "))
sociales = float(input("Ingrese la calificacion para Sociales: "))
print("")
print("Las calificaciones ingresadas son: ")
print(f"Ciencias: {ciencias}")
print(f"Español: {espanol}")
print(f"Matematicas: {matematicas}")
print(f"Sociales: {sociales}")
print("El promedio total de las materias es: "+str(round((ciencias+espanol+matematicas+sociales)/4,2)))