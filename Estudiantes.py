
pasaron = []
cont = 1
print("Dime la cantidad de estudiantes que quieres y su nota")
estudiantes = int (input("Cuantos estudiantes? :"))
while cont <= estudiantes:
  print(f"Estudiante {cont}")
  nombre = str(input("Cual es su nombre? :"))
  nota = float(input("Y cual fue su nota? :"))
  if nota >= 3.0:
        pasaron.append (nombre)
  cont += 1
print("Los estudiantes que pasaron son\n: ")
print(pasaron)




    