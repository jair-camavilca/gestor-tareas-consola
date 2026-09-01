from datetime import datetime

# ============================================
# FUNCIÓN PARA VALIDAR FECHA (con control de errores)
# ============================================
def validar_fecha():
    """
    Esta función pide una fecha en formato dd-mm-aaaa.
    - Usa try/except para evitar errores por formato incorrecto (ej. 32-15-2025)
    - Repite hasta que la fecha sea válida y no sea anterior a la actual.
    """
    while True:
        try:
            fecha_texto = input("Ingrese la fecha límite (dd-mm-aaaa): ")
            fecha = datetime.strptime(fecha_texto, "%d-%m-%Y")  # Valida automáticamente día, mes y año
            fecha_actual = datetime.now()
            
            # Evita fechas anteriores a la actual
            if fecha.date() < fecha_actual.date():
                print(" La fecha no puede ser anterior a la actual. Intente nuevamente.")
            else:
                return fecha  # Si todo está bien, se devuelve la fecha válida
        except ValueError:
            # Captura fechas imposibles o mal escritas (como día 32 o mes 15)
            print(" Fecha inválida. Asegúrese de usar el formato correcto y una fecha real.")

# ============================================
# LISTA PRINCIPAL Y FUNCIONES AUXILIARES
# ============================================
lista_tareas = []
# ============================================
# FUNCIÓN PARA CREAR TAREA
# ============================================
def crear_tarea():
    print("""
╔═══╦════════════════════════════════════════╗
║ 1 ║ CREAR TAREA                            ║
╚═══╩════════════════════════════════════════╝
    """)
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    
    fecha_limite = validar_fecha()  # Llama a la función que valida fecha
    
    id_tarea = len(lista_tareas) + 1
    fecha_creacion = datetime.now()
    estado = "Pendiente"

    tarea = {
        "id_tarea": id_tarea,
        "titulo": titulo,
        "descripcion": descripcion,
        "fecha_creacion": fecha_creacion,
        "fecha_limite": fecha_limite,
        "estado": estado
    }
    
    lista_tareas.append(tarea)
    print(" Tarea creada correctamente.\n")

# ============================================
# FUNCIÓN PARA VER TAREAS
# ============================================
def ver_tareas():
    print("""
╔═══╦════════════════════════════════════════╗
║ 2 ║ VER LISTA DE TAREAS                    ║
╚═══╩════════════════════════════════════════╝
    """)
    print("=" * 60)
    
    if not lista_tareas:
        print("  No hay tareas registradas.\n")
    else:
        for tarea in lista_tareas:
            print(f" ID            : {tarea['id_tarea']}")
            print(f" Título        : {tarea['titulo']}")
            print(f" Descripción   : {tarea['descripcion']}")
            print(f" Creación      : {tarea['fecha_creacion'].strftime('%d-%m-%Y')}")
            print(f" Fecha límite  : {tarea['fecha_limite'].strftime('%d-%m-%Y')}")
            print(f" Estado        : {tarea['estado']}")
            print("-" * 60)

# ============================================
# FUNCIÓN PARA ACTUALIZAR TAREA
# ============================================
def actualizar_tarea():
    print("""
╔═══╦════════════════════════════════════════╗
║ 3 ║ ACTUALIZAR TAREA                       ║
╚═══╩════════════════════════════════════════╝
    """)
    try:
        id_tarea = int(input("Ingrese el ID de la tarea a actualizar: "))
        tarea = None
        for t in lista_tareas:
            if t["id_tarea"] == id_tarea:
                tarea = t
                break
        
        if tarea is None:
            print(" ID no encontrado.\n")
            return
        
        nuevo_titulo = input("Nuevo título (deje vacío para no cambiar): ")
        nueva_descripcion = input("Nueva descripción (deje vacío para no cambiar): ")
        nuevo_estado = input("Nuevo estado (Pendiente / En ejecución / Completado): ")
        
        if nuevo_titulo:
            tarea["titulo"] = nuevo_titulo
        if nueva_descripcion:
            tarea["descripcion"] = nueva_descripcion
        if nuevo_estado:
            tarea["estado"] = nuevo_estado
        
        print(" Tarea actualizada correctamente.\n")
    except ValueError:
        print(" Ingrese un número de ID válido.\n")

# ============================================
# FUNCIÓN PARA ELIMINAR TAREA
# ============================================
def eliminar_tarea():
    print("""
╔═══╦════════════════════════════════════════╗
║ 4 ║ ELIMINAR TAREA                         ║
╚═══╩════════════════════════════════════════╝
    """)
    try:
        id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
        for tarea in lista_tareas:
            if tarea["id_tarea"] == id_tarea:
                lista_tareas.remove(tarea)
                print(" Tarea eliminada correctamente.\n")
                return
        print(" ID no encontrado.\n")
    except ValueError:
        print(" Ingrese un número de ID válido.\n")

# ============================================
# PROGRAMA PRINCIPAL
# ============================================
while True:
    print("""
╔════════════════════════════════════════════╗
║       APLICACIÓN DE GESTIÓN DE TAREAS      ║
╠═══╦════════════════════════════════════════╣
║ 1 ║ CREAR TAREA                            ║
║ 2 ║ VER LISTA DE TAREAS                    ║
║ 3 ║ ACTUALIZAR TAREA                       ║
║ 4 ║ ELIMINAR TAREA                         ║
║ 0 ║ SALIR DEL PROGRAMA                     ║ 
╚═══╩════════════════════════════════════════╝
    """)
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        crear_tarea()
    elif opcion == "2":
        ver_tareas()
    elif opcion == "3":
        actualizar_tarea()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "0":
        print(" Saliendo del programa...")
        break
    else:
        print(" Opción inválida. Intente nuevamente.\n")