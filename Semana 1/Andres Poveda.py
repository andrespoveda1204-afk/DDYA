print("Hola, bienvenid@ al programa\n")
print("Dime cualquier numero entero y te dire si es un numero fibonacci, primo, positivo, negativo o si es cero\n")
numero=int(input("Ingresa un numero entero :"))
divisores = 0
for e in range  (numero + 1):
    suma = e + e
    if suma == numero:
        print ("\nEs un numero fibonacci\n")

for i in range (1, numero + 1 ):
    if numero % i == 0:
        divisores += 1
if divisores == 2:
    print("Es un numero primo\n")
if numero > 0 :
    print("El numero es positivo\n")
elif numero < 0 :
    print("El numero es negativo\n")
elif numero == 0 : 
    print("El numero es cero\n")

print("Fin del programa")