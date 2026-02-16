Lista = [("Ana", 5.0), ("luis", 4.5), ("maria", 3.0), ("pedro", 2.5), ("lucia", 1.0)]
def estudiantes_apro (estudiantes):
    if len(estudiantes) == 1:
        nombre, nota = estudiantes[0]
        if nota >= 3.0:
            return [nombre]
        else: 
            return []
    mid = len(estudiantes) // 2
    izq = estudiantes_apro(estudiantes[:mid])
    der = estudiantes_apro(estudiantes[mid:])
    return izq + der

aprobados = estudiantes_apro(Lista)
print(aprobados)  
    
