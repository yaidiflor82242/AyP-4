"""Un colegio tiene 3 clubes extracurriculares. Cada club tiene un conjunto
de estudiantes inscritos. Responde las preguntas usando operaciones de conjuntos."""

club_ciencias = {"Ana", "Carlos", "Diana", "Elena", "Felipe"}
club_deportes = {"Carlos", "Felipe", "Gabriel", "Hugo", "Isabel"}
club_arte = {"Ana", "Diana", "Gabriel", "Julia", "Karen"}

def estudiantes_en_todos():
    """
    Retorna el conjunto de estudiantes inscritos en LOS TRES clubes.
    (Intersección de los tres)
    """
    return club_ciencias & club_deportes & club_arte
    # TODO: Implementar
    pass

def solo_un_club():
    """
    Retorna el conjunto de estudiantes que están en EXACTAMENTE un club.

    Pista: Un estudiante está en exactamente un club si está en ese club
    pero NO en los otros dos.

    Ejemplo esperado: {"Elena", "Hugo", "Isabel", "Julia", "Karen"}
    """
    solo_ciencias = club_ciencias - club_deportes - club_arte
    solo_deportes = club_deportes - club_ciencias - club_arte
    solo_arte = club_arte - club_ciencias - club_deportes
    
    return solo_ciencias | solo_deportes | solo_arte
    # TODO: Implementar
    pass

def clubes_de_estudiante(nombre):
    """
    Retorna una lista con los nombres de los clubes a los que pertenece
    el estudiante.

    Ejemplo:
    clubes_de_estudiante("Carlos") -> ["Ciencias", "Deportes"]
    clubes_de_estudiante("Julia") -> ["Arte"]
    """
    clubes = []
    
    if nombre in club_ciencias:
        clubes.append("Ciencias")
    
    if nombre in club_deportes:
        clubes.append("Deportes")
    
    if nombre in club_arte:
        clubes.append("Arte")
    
    return clubes
    # TODO: Implementar

# =============================
# PRUEBAS
# =============================

print(" Estudiantes en los 3 clubes:")
print(estudiantes_en_todos())
# Esperado: set()

print("\n Estudiantes en EXACTAMENTE un club:")
print(solo_un_club())
# Esperado: {'Elena', 'Hugo', 'Isabel', 'Julia', 'Karen'}

print("\n Clubes de Carlos:")
print(clubes_de_estudiante("Carlos"))
# Esperado: ['Ciencias', 'Deportes']

print("\n Clubes de Julia:")
print(clubes_de_estudiante("Julia"))
# Esperado: ['Arte']

print("\n Clubes de Ana:")
print(clubes_de_estudiante("Ana"))
# Esperado: ['Ciencias', 'Arte']

print("\n Clubes de alguien que no existe:")
print(clubes_de_estudiante("Pedro"))
# Esperado: []
