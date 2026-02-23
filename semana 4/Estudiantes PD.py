# Tabla de promedios según el tamaño del grupo 
# tamaño de estudiantes: promedio cualquiera
VALORES_PROMEDIO = {
    1: 3.0, 
    2: 4.5, 
    3: 4.0, 
    4: 5.2
}

def optimizar_estudiantes(n, memo=None):
    if memo is None:
        memo = {}

   
    if n == 0: return 0
    if n < 0: return -float('inf') 
    
   
    if n in memo:
        return memo[n]
    
    mejor_promedio = 0
     
    for tamano_grupo, valor in VALORES_PROMEDIO.items():
        if n >= tamano_grupo:
          
            opcion = valor + optimizar_estudiantes(n - tamano_grupo, memo)
            if opcion > mejor_promedio:
                mejor_promedio = opcion
    
    memo[n] = mejor_promedio
    return mejor_promedio

def main ():
    n = int(input("Ingrese el número de estudiantes: "))
    resultado = optimizar_estudiantes(n)
    print(f"El mejor promedio posible para {n} estudiantes es: {resultado}")

main ()
