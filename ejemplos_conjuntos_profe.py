"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 1: SPOTIFY - PLAYLISTS COMPARTIDAS
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
Spotify quiere implementar una función de "Playlists Compartidas".
Dados dos usuarios con sus canciones favoritas, el sistema debe:

1. Encontrar canciones que ambos disfrutan (para playlist compartida)
2. Sugerir canciones que uno tiene y el otro no
3. Mostrar el catálogo combinado de ambos
4. Verificar si un usuario escucha un subconjunto de lo que escucha otro

Implementar usando operaciones de conjuntos.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════

canciones_juan = {
    "Blinding Lights", "Bohemian Rhapsody", "Shape of You",
    "Despacito", "Hotel California", "Billie Jean",
    "Rolling in the Deep", "Smells Like Teen Spirit"
}

canciones_maria = {
    "Shape of You", "Despacito", "Bad Guy",
    "Blinding Lights", "Watermelon Sugar", "Levitating",
    "Rolling in the Deep", "drivers license"
}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   SPOTIFY - PLAYLISTS COMPARTIDAS")
print("=" * 60)

print(f"\nCanciones de Juan ({len(canciones_juan)}):")
for c in sorted(canciones_juan):
    print(f"  ♪ {c}")

print(f"\nCanciones de María ({len(canciones_maria)}):")
for c in sorted(canciones_maria):
    print(f"  ♪ {c}")

# 1. Playlist compartida (intersección)
compartidas = canciones_juan & canciones_maria
print(f"\n1. Playlist compartida ({len(compartidas)} canciones):")
for c in sorted(compartidas):
    print(f"  ♪ {c}")

# 2. Sugerencias (diferencia)
sugerencias_para_juan = canciones_maria - canciones_juan
sugerencias_para_maria = canciones_juan - canciones_maria

print(f"\n2. Sugerencias para Juan ({len(sugerencias_para_juan)}):")
for c in sorted(sugerencias_para_juan):
    print(f"  → {c}")

print(f"\n   Sugerencias para María ({len(sugerencias_para_maria)}):")
for c in sorted(sugerencias_para_maria):
    print(f"  → {c}")

# 3. Catálogo combinado (unión)
catalogo = canciones_juan | canciones_maria
print(f"\n3. Catálogo combinado ({len(catalogo)} canciones únicas):")
for c in sorted(catalogo):
    print(f"  ♪ {c}")

# 4. ¿Un usuario escucha subconjunto del otro?
print(f"\n4. ¿Juan escucha subconjunto de María? {canciones_juan <= canciones_maria}")
print(f"   ¿María escucha subconjunto de Juan? {canciones_maria <= canciones_juan}")

# Bonus: Canciones exclusivas (diferencia simétrica)
exclusivas = canciones_juan ^ canciones_maria
print(f"\n5. Canciones que solo uno de los dos escucha ({len(exclusivas)}):")
for c in sorted(exclusivas):
    print(f"  ♪ {c}")

"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 2: UNIVERSIDAD - CRUCE DE HORARIOS
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
La universidad necesita un sistema para analizar la matrícula de estudiantes.
Dados los estudiantes inscritos en diferentes materias, el sistema debe:

1. Encontrar estudiantes que cursan ambas materias (para evitar cruces)
2. Encontrar estudiantes que solo cursan una materia
3. Total de estudiantes únicos entre todas las materias
4. Verificar si todos los de una materia están en otra
5. Encontrar estudiantes que cursan las 3 materias

Implementar usando operaciones de conjuntos.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════

algoritmos = {
    "Ana", "Carlos", "Diana", "Eduardo", "Fernanda",
    "Gabriel", "Helena", "Ivan"
}

bases_datos = {
    "Carlos", "Diana", "Juan", "Karen",
    "Gabriel", "Luis", "Maria"
}

redes = {
    "Diana", "Eduardo", "Gabriel", "Karen",
    "Natalia", "Oscar", "Ivan"
}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   UNIVERSIDAD - CRUCE DE HORARIOS")
print("=" * 60)

print(f"\nAlgoritmos ({len(algoritmos)}): {sorted(algoritmos)}")
print(f"Bases de Datos ({len(bases_datos)}): {sorted(bases_datos)}")
print(f"Redes ({len(redes)}): {sorted(redes)}")

# 1. Estudiantes en Algoritmos Y Bases de Datos (posible cruce)
cruce_alg_bd = algoritmos & bases_datos
print(f"\n1. Cursan Algoritmos Y Bases de Datos: {sorted(cruce_alg_bd)}")

cruce_alg_redes = algoritmos & redes
print(f"   Cursan Algoritmos Y Redes: {sorted(cruce_alg_redes)}")

cruce_bd_redes = bases_datos & redes
print(f"   Cursan Bases de Datos Y Redes: {sorted(cruce_bd_redes)}")

# 2. Estudiantes que SOLO cursan una materia
solo_algoritmos = algoritmos - bases_datos - redes
solo_bd = bases_datos - algoritmos - redes
solo_redes = redes - algoritmos - bases_datos

print(f"\n2. Solo Algoritmos: {sorted(solo_algoritmos)}")
print(f"   Solo Bases de Datos: {sorted(solo_bd)}")
print(f"   Solo Redes: {sorted(solo_redes)}")

# 3. Total de estudiantes únicos
todos = algoritmos | bases_datos | redes
print(f"\n3. Total estudiantes únicos: {len(todos)}")
print(f"   Estudiantes: {sorted(todos)}")

# 4. ¿Todos los de Algoritmos están en Bases de Datos?
print(f"\n4. ¿Algoritmos ⊆ Bases de Datos? {algoritmos <= bases_datos}")
print(f"   ¿Cruce Alg-BD ⊆ Algoritmos? {cruce_alg_bd <= algoritmos}")

# 5. Estudiantes en las 3 materias
en_las_tres = algoritmos & bases_datos & redes
print(f"\n5. Cursan las 3 materias: {sorted(en_las_tres)}")

# Bonus: Resumen por estudiante
print("\n" + "=" * 60)
print("RESUMEN POR ESTUDIANTE")
print("=" * 60)
for estudiante in sorted(todos):
    materias = []
    if estudiante in algoritmos:
        materias.append("Algoritmos")
    if estudiante in bases_datos:
        materias.append("BD")
    if estudiante in redes:
        materias.append("Redes")
    print(f"  {estudiante}: {', '.join(materias)} ({len(materias)} materias)")

"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 3: NETFLIX - SISTEMA DE RECOMENDACIONES
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
Netflix quiere mejorar su sistema de recomendaciones usando conjuntos.
Cada película tiene un conjunto de géneros/etiquetas.
El sistema debe:

1. Encontrar películas similares (comparten géneros)
2. Recomendar películas según los géneros favoritos del usuario
3. Encontrar géneros únicos en el catálogo
4. Agrupar películas por género
5. Calcular un "puntaje de similitud" entre películas

Implementar usando operaciones de conjuntos.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════

catalogo = {
    "Inception": {"ciencia ficción", "acción", "thriller", "drama"},
    "The Matrix": {"ciencia ficción", "acción", "thriller"},
    "Titanic": {"romance", "drama", "histórica"},
    "The Notebook": {"romance", "drama"},
    "Avengers": {"acción", "ciencia ficción", "aventura"},
    "John Wick": {"acción", "thriller", "crimen"},
    "Interstellar": {"ciencia ficción", "drama", "aventura"},
    "The Godfather": {"crimen", "drama", "thriller"},
    "Toy Story": {"animación", "comedia", "aventura"},
    "Shrek": {"animación", "comedia", "aventura"},
}

# Géneros favoritos del usuario
favoritos_usuario = {"ciencia ficción", "acción", "thriller"}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   NETFLIX - SISTEMA DE RECOMENDACIONES")
print("=" * 60)

print("\nCatálogo:")
for pelicula, generos in catalogo.items():
    print(f"  {pelicula}: {generos}")

# 1. Películas similares (comparten al menos 2 géneros)
print("\n" + "=" * 60)
print("1. PELÍCULAS SIMILARES (comparten 2+ géneros)")
print("=" * 60)

peliculas = list(catalogo.keys())
for i in range(len(peliculas)):
    for j in range(i + 1, len(peliculas)):
        p1, p2 = peliculas[i], peliculas[j]
        comunes = catalogo[p1] & catalogo[p2]
        if len(comunes) >= 2:
            print(f"  {p1} <-> {p2}")
            print(f"    Géneros comunes: {comunes}")

# 2. Recomendaciones según gustos del usuario
print("\n" + "=" * 60)
print(f"2. RECOMENDACIONES (gustos: {favoritos_usuario})")
print("=" * 60)

recomendaciones = []
for pelicula, generos in catalogo.items():
    coincidencias = generos & favoritos_usuario
    if coincidencias:
        puntaje = len(coincidencias) / len(favoritos_usuario)
        recomendaciones.append((pelicula, puntaje, coincidencias))

# Ordenar por puntaje (mayor primero)
recomendaciones.sort(key=lambda x: x[1], reverse=True)

for pelicula, puntaje, coincidencias in recomendaciones:
    barra = "█" * int(puntaje * 10)
    print(f"  {pelicula:20} {barra} {puntaje:.0%} - {coincidencias}")

# 3. Todos los géneros del catálogo
print("\n" + "=" * 60)
print("3. GÉNEROS ÚNICOS EN EL CATÁLOGO")
print("=" * 60)

todos_generos = set()
for generos in catalogo.values():
    todos_generos = todos_generos | generos

print(f"  Total: {len(todos_generos)} géneros")
for g in sorted(todos_generos):
    print(f"  • {g}")

# 4. Agrupar películas por género
print("\n" + "=" * 60)
print("4. PELÍCULAS POR GÉNERO")
print("=" * 60)

for genero in sorted(todos_generos):
    peliculas_genero = set()
    for pelicula, generos in catalogo.items():
        if genero in generos:
            peliculas_genero.add(pelicula)
    print(f"  {genero}: {peliculas_genero}")

# 5. Puntaje de similitud entre dos películas
print("\n" + "=" * 60)
print("5. SIMILITUD (índice de Jaccard)")
print("=" * 60)

def similitud_jaccard(pelicula1, pelicula2):
    """
    Índice de Jaccard = |A ∩ B| / |A ∪ B|
    1.0 = idénticos, 0.0 = nada en común
    """
    g1 = catalogo[pelicula1]
    g2 = catalogo[pelicula2]
    interseccion = len(g1 & g2)
    union = len(g1 | g2)
    return interseccion / union if union > 0 else 0

pares = [
    ("Inception", "The Matrix"),
    ("Inception", "Titanic"),
    ("Toy Story", "Shrek"),
    ("The Godfather", "John Wick"),
]

for p1, p2 in pares:
    sim = similitud_jaccard(p1, p2)
    barra = "█" * int(sim * 20)
    print(f"  {p1:15} vs {p2:15} → {barra} {sim:.2f}")    

"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 4: SEGURIDAD - CONTROL DE ACCESO
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
Una empresa necesita un sistema de control de acceso basado en roles.
Cada rol tiene un conjunto de permisos. El sistema debe:

1. Verificar si un usuario puede realizar una acción
2. Encontrar permisos comunes entre roles
3. Encontrar permisos exclusivos de cada rol
4. Verificar si un rol es "superior" a otro (tiene todos sus permisos)
5. Crear un nuevo rol combinando permisos de otros

Implementar usando operaciones de conjuntos.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════

roles = {
    "admin": {
        "leer", "escribir", "eliminar", "crear_usuarios",
        "ver_logs", "configurar", "backup", "restaurar"
    },
    "editor": {"leer", "escribir", "subir_archivos"},
    "viewer": {"leer"},
    "moderador": {"leer", "escribir", "eliminar", "ver_logs"},
    "auditor": {"leer", "ver_logs", "exportar_reportes"},
}

usuarios = {
    "Juan": "admin",
    "María": "editor",
    "Pedro": "viewer",
    "Ana": "moderador",
    "Carlos": "auditor",
}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   SEGURIDAD - CONTROL DE ACCESO")
print("=" * 60)

print("\nRoles y permisos:")
for rol, permisos in roles.items():
    print(f"  {rol}: {sorted(permisos)}")

print("\nUsuarios:")
for usuario, rol in usuarios.items():
    print(f"  {usuario} → {rol}")

# 1. Verificar si un usuario puede realizar una acción
print("\n" + "=" * 60)
print("1. VERIFICAR ACCESO")
print("=" * 60)

def puede_hacer(usuario, acciones_requeridas):
    """Verifica si el usuario tiene todos los permisos necesarios"""
    rol = usuarios.get(usuario)
    if not rol:
        return False
    permisos = roles.get(rol, set())
    return acciones_requeridas <= permisos  # subconjunto

verificaciones = [
    ("Juan", {"leer", "eliminar"}),
    ("María", {"leer", "escribir"}),
    ("María", {"eliminar"}),
    ("Pedro", {"leer"}),
    ("Pedro", {"escribir"}),
    ("Ana", {"leer", "ver_logs"}),
]

for usuario, acciones in verificaciones:
    resultado = "✓" if puede_hacer(usuario, acciones) else "✗"
    print(f"  {resultado} {usuario} → {acciones}")

# 2. Permisos comunes entre roles
print("\n" + "=" * 60)
print("2. PERMISOS COMUNES")
print("=" * 60)

pares_roles = [
    ("editor", "moderador"),
    ("moderador", "auditor"),
    ("editor", "auditor"),
]

for r1, r2 in pares_roles:
    comunes = roles[r1] & roles[r2]
    print(f"  {r1} ∩ {r2}: {sorted(comunes)}")

# 3. Permisos exclusivos de cada rol
print("\n" + "=" * 60)
print("3. PERMISOS EXCLUSIVOS")
print("=" * 60)

for nombre, permisos in roles.items():
    otros_permisos = set()
    for otro_nombre, otros in roles.items():
        if otro_nombre != nombre:
            otros_permisos = otros_permisos | otros
    exclusivos = permisos - otros_permisos
    if exclusivos:
        print(f"  {nombre}: {sorted(exclusivos)}")
    else:
        print(f"  {nombre}: (ninguno exclusivo)")

# 4. ¿Un rol es "superior" a otro?
print("\n" + "=" * 60)
print("4. JERARQUÍA DE ROLES")
print("=" * 60)

for r1 in roles:
    for r2 in roles:
        if r1 != r2 and roles[r2] < roles[r1]:
            print(f"  {r1} contiene todos los permisos de {r2}")

# 5. Crear nuevo rol combinando otros
print("\n" + "=" * 60)
print("5. CREAR ROL COMBINADO")
print("=" * 60)

nuevo_rol = roles["editor"] | roles["auditor"]
print(f"  editor + auditor = {sorted(nuevo_rol)}")

# Verificar que no tenga permisos peligrosos
permisos_peligrosos = {"eliminar", "crear_usuarios", "configurar"}
conflictos = nuevo_rol & permisos_peligrosos
if conflictos:
    print(f"  Alerta: tiene permisos peligrosos: {conflictos}")
else:
    print(f"  Sin permisos peligrosos")

"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 5: RED SOCIAL - ANÁLISIS DE CONEXIONES
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
Una red social necesita analizar las conexiones entre usuarios.
Cada usuario tiene un conjunto de amigos. El sistema debe:

1. Encontrar amigos en común entre dos usuarios
2. Sugerir amigos (amigos de amigos que no conoces)
3. Encontrar grupos aislados (usuarios sin amigos en común)
4. Calcular el "grado de conexión" entre usuarios
5. Encontrar el usuario más conectado

Implementar usando operaciones de conjuntos.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════

red = {
    "Ana": {"Carlos", "Diana", "Eduardo", "Fernanda"},
    "Carlos": {"Ana", "Diana", "Gabriel"},
    "Diana": {"Ana", "Carlos", "Eduardo", "Helena"},
    "Eduardo": {"Ana", "Diana", "Fernanda"},
    "Fernanda": {"Ana", "Eduardo", "Gabriel", "Helena"},
    "Gabriel": {"Carlos", "Fernanda", "Ivan"},
    "Helena": {"Diana", "Fernanda", "Ivan"},
    "Ivan": {"Gabriel", "Helena"},
}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   RED SOCIAL - ANÁLISIS DE CONEXIONES")
print("=" * 60)

print("\nConexiones:")
for usuario, amigos in red.items():
    print(f"  {usuario} ({len(amigos)} amigos): {sorted(amigos)}")

# 1. Amigos en común
print("\n" + "=" * 60)
print("1. AMIGOS EN COMÚN")
print("=" * 60)

pares = [("Ana", "Carlos"), ("Ana", "Gabriel"), ("Diana", "Fernanda")]
for u1, u2 in pares:
    comunes = red[u1] & red[u2]
    print(f"  {u1} y {u2}: {sorted(comunes) if comunes else 'ninguno'}")

# 2. Sugerir amigos (amigos de amigos que no conoces)
print("\n" + "=" * 60)
print("2. SUGERENCIAS DE AMISTAD")
print("=" * 60)

for usuario in sorted(red.keys()):
    amigos_de_amigos = set()
    for amigo in red[usuario]:
        amigos_de_amigos = amigos_de_amigos | red[amigo]
    
    # Quitar al usuario mismo y sus amigos actuales
    sugerencias = amigos_de_amigos - red[usuario] - {usuario}
    
    if sugerencias:
        print(f"  {usuario} → Sugerencias: {sorted(sugerencias)}")

# 3. Usuarios sin amigos en común (disjuntos)
print("\n" + "=" * 60)
print("3. USUARIOS SIN AMIGOS EN COMÚN")
print("=" * 60)

usuarios = list(red.keys())
for i in range(len(usuarios)):
    for j in range(i + 1, len(usuarios)):
        u1, u2 = usuarios[i], usuarios[j]
        if red[u1].isdisjoint(red[u2]):
            print(f"  {u1} y {u2} no tienen amigos en común")

# 4. Grado de conexión (amigos en común / total amigos)
print("\n" + "=" * 60)
print("4. GRADO DE CONEXIÓN")
print("=" * 60)

u1, u2 = "Ana", "Diana"
comunes = red[u1] & red[u2]
total = red[u1] | red[u2]
grado = len(comunes) / len(total) if total else 0
print(f"  {u1} y {u2}:")
print(f"    Amigos en común: {sorted(comunes)}")
print(f"    Total amigos: {sorted(total)}")
print(f"    Grado de conexión: {grado:.2%}")

# 5. Usuario más conectado
print("\n" + "=" * 60)
print("5. USUARIO MÁS CONECTADO")
print("=" * 60)

ranking = []
for usuario, amigos in red.items():
    ranking.append((usuario, len(amigos)))

ranking.sort(key=lambda x: x[1], reverse=True)

for i, (usuario, num_amigos) in enumerate(ranking, 1):
    barra = "█" * num_amigos
    print(f"  {i}. {usuario:10} {barra} ({num_amigos} amigos)")


    