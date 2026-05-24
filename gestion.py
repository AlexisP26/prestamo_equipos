# gestion.py
# Vectores y operaciones - Proyecto Gestión Préstamo Equipos

from clases.estudiante_ingenieria import EstudianteIngenieria
from clases.estudiante_diseno import EstudianteDiseno
from clases.computador_portatil import ComputadorPortatil
from clases.tableta_grafica import TabletaGrafica
from clases.validaciones import pedir_cedula, pedir_serial, pedir_opcion_menu

# ─── 4 VECTORES PRINCIPALES ────────────────────────────────
vector_ingenieros   = []
vector_disenadores  = []
vector_portatil     = []
vector_tableta      = []


# ══════════════════════════════════════════════════════════════
#  UTILIDADES DE BÚSQUEDA
# ══════════════════════════════════════════════════════════════

def buscar_ingeniero_cedula(cedula):
    """Busca un ingeniero por cédula. Retorna el objeto o None."""
    for est in vector_ingenieros:
        if est.get_cedula() == cedula:
            return est
    return None

def buscar_disenador_cedula(cedula):
    """Busca un diseñador por cédula. Retorna el objeto o None."""
    for est in vector_disenadores:
        if est.get_cedula() == cedula:
            return est
    return None

def buscar_portatil_serial(serial):
    """Busca un portátil por serial. Retorna el objeto o None."""
    for eq in vector_portatil:
        if eq.get_serial() == serial:
            return eq
    return None

def buscar_tableta_serial(serial):
    """Busca una tableta por serial. Retorna el objeto o None."""
    for eq in vector_tableta:
        if eq.get_serial() == serial:
            return eq
    return None


# ══════════════════════════════════════════════════════════════
#  GESTIÓN ESTUDIANTES INGENIERÍA
# ══════════════════════════════════════════════════════════════

def registrar_ingeniero():
    print("\n╔══ REGISTRAR PRÉSTAMO - INGENIERÍA ══╗")
    estudiante = EstudianteIngenieria()
    estudiante.capturar_datos()

    # Validación: cédula no duplicada
    if buscar_ingeniero_cedula(estudiante.get_cedula()):
        print("❌ Ya existe un estudiante con esa cédula.")
        return

    # Validación: serial del equipo disponible
    equipo = buscar_portatil_serial(estudiante.get_serial_equipo())
    if not equipo:
        equipo = buscar_tableta_serial(estudiante.get_serial_equipo())
    if not equipo:
        print("❌ No existe un equipo con ese serial en el inventario.")
        return
    if equipo.get_estado() == "Prestado":
        print("❌ Ese equipo ya está prestado.")
        return

    equipo.set_estado("Prestado")
    vector_ingenieros.append(estudiante)
    print("✅ Préstamo registrado exitosamente.")

def modificar_ingeniero():
    print("\n╔══ MODIFICAR - INGENIERÍA ══╗")
    cedula = pedir_cedula("  Cédula del estudiante: ")
    estudiante = buscar_ingeniero_cedula(cedula)
    if not estudiante:
        print("❌ No se encontró un estudiante con esa cédula.")
        return
    estudiante.modificar_datos()
    print("✅ Datos actualizados exitosamente.")

def devolver_equipo_ingeniero():
    print("\n╔══ DEVOLUCIÓN EQUIPO - INGENIERÍA ══╗")
    cedula = pedir_cedula("  Cédula del estudiante: ")
    estudiante = buscar_ingeniero_cedula(cedula)
    if not estudiante:
        print("❌ No se encontró un estudiante con esa cédula.")
        return

    # Liberar el equipo
    serial = estudiante.get_serial_equipo()
    equipo = buscar_portatil_serial(serial)
    if not equipo:
        equipo = buscar_tableta_serial(serial)
    if equipo:
        equipo.set_estado("Disponible")

    vector_ingenieros.remove(estudiante)
    print(f"✅ Equipo {serial} devuelto y registro eliminado.")

def buscar_ingeniero():
    print("\n╔══ BUSCAR - INGENIERÍA ══╗")
    print("  1. Buscar por cédula")
    print("  2. Buscar por serial de equipo")
    opcion = pedir_opcion_menu("  Opción: ", ["1", "2"])

    if opcion == "1":
        cedula = pedir_cedula("  Cédula: ")
        estudiante = buscar_ingeniero_cedula(cedula)
        if estudiante:
            estudiante.imprimir()
        else:
            print("❌ No se encontró el estudiante.")
    else:
        serial = pedir_serial("  Serial del equipo: ")
        resultado = None
        for est in vector_ingenieros:
            if est.get_serial_equipo() == serial:
                resultado = est
                break
        if resultado:
            resultado.imprimir()
        else:
            print("❌ No se encontró un estudiante con ese serial.")

def listar_ingenieros():
    print("\n╔══ LISTADO INGENIERÍA ══╗")
    if not vector_ingenieros:
        print("  No hay registros.")
        return
    for est in vector_ingenieros:
        est.imprimir()


# ══════════════════════════════════════════════════════════════
#  GESTIÓN ESTUDIANTES DISEÑO
# ══════════════════════════════════════════════════════════════

def registrar_disenador():
    print("\n╔══ REGISTRAR PRÉSTAMO - DISEÑO ══╗")
    estudiante = EstudianteDiseno()
    estudiante.capturar_datos()

    if buscar_disenador_cedula(estudiante.get_cedula()):
        print("❌ Ya existe un estudiante con esa cédula.")
        return

    equipo = buscar_portatil_serial(estudiante.get_serial_equipo())
    if not equipo:
        equipo = buscar_tableta_serial(estudiante.get_serial_equipo())
    if not equipo:
        print("❌ No existe un equipo con ese serial en el inventario.")
        return
    if equipo.get_estado() == "Prestado":
        print("❌ Ese equipo ya está prestado.")
        return

    equipo.set_estado("Prestado")
    vector_disenadores.append(estudiante)
    print("✅ Préstamo registrado exitosamente.")

def modificar_disenador():
    print("\n╔══ MODIFICAR - DISEÑO ══╗")
    cedula = pedir_cedula("  Cédula del estudiante: ")
    estudiante = buscar_disenador_cedula(cedula)
    if not estudiante:
        print("❌ No se encontró un estudiante con esa cédula.")
        return
    estudiante.modificar_datos()
    print("✅ Datos actualizados exitosamente.")

def devolver_equipo_disenador():
    print("\n╔══ DEVOLUCIÓN EQUIPO - DISEÑO ══╗")
    cedula = pedir_cedula("  Cédula del estudiante: ")
    estudiante = buscar_disenador_cedula(cedula)
    if not estudiante:
        print("❌ No se encontró un estudiante con esa cédula.")
        return

    serial = estudiante.get_serial_equipo()
    equipo = buscar_portatil_serial(serial)
    if not equipo:
        equipo = buscar_tableta_serial(serial)
    if equipo:
        equipo.set_estado("Disponible")

    vector_disenadores.remove(estudiante)
    print(f"✅ Equipo {serial} devuelto y registro eliminado.")

def buscar_disenador():
    print("\n╔══ BUSCAR - DISEÑO ══╗")
    print("  1. Buscar por cédula")
    print("  2. Buscar por serial de equipo")
    opcion = pedir_opcion_menu("  Opción: ", ["1", "2"])

    if opcion == "1":
        cedula = pedir_cedula("  Cédula: ")
        estudiante = buscar_disenador_cedula(cedula)
        if estudiante:
            estudiante.imprimir()
        else:
            print("❌ No se encontró el estudiante.")
    else:
        serial = pedir_serial("  Serial del equipo: ")
        resultado = None
        for est in vector_disenadores:
            if est.get_serial_equipo() == serial:
                resultado = est
                break
        if resultado:
            resultado.imprimir()
        else:
            print("❌ No se encontró un estudiante con ese serial.")

def listar_disenadores():
    print("\n╔══ LISTADO DISEÑO ══╗")
    if not vector_disenadores:
        print("  No hay registros.")
        return
    for est in vector_disenadores:
        est.imprimir()


# ══════════════════════════════════════════════════════════════
#  GESTIÓN EQUIPOS
# ══════════════════════════════════════════════════════════════

def registrar_portatil():
    print("\n╔══ REGISTRAR PORTÁTIL ══╗")
    equipo = ComputadorPortatil()
    equipo.capturar_datos()
    if buscar_portatil_serial(equipo.get_serial()):
        print("❌ Ya existe un portátil con ese serial.")
        return
    vector_portatil.append(equipo)
    print("✅ Portátil registrado exitosamente.")

def registrar_tableta():
    print("\n╔══ REGISTRAR TABLETA ══╗")
    equipo = TabletaGrafica()
    equipo.capturar_datos()
    if buscar_tableta_serial(equipo.get_serial()):
        print("❌ Ya existe una tableta con ese serial.")
        return
    vector_tableta.append(equipo)
    print("✅ Tableta registrada exitosamente.")

def listar_equipos():
    print("\n╔══ INVENTARIO DE EQUIPOS ══╗")
    print("\n  ── Portátiles ──")
    if not vector_portatil:
        print("  No hay portátiles registrados.")
    for eq in vector_portatil:
        eq.imprimir()

    print("\n  ── Tabletas ──")
    if not vector_tableta:
        print("  No hay tabletas registradas.")
    for eq in vector_tableta:
        eq.imprimir()
