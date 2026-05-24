import gestion
from clases.validaciones import pedir_opcion_menu


def menu_ingenieria():
    while True:
        print("""
╔══════════════════════════════════════╗
║       ESTUDIANTES INGENIERÍA        ║
╠══════════════════════════════════════╣
║  1. Registrar préstamo              ║
║  2. Modificar datos                 ║
║  3. Devolver equipo                 ║
║  4. Buscar estudiante               ║
║  5. Listar todos                    ║
║  6. Volver al menú principal        ║
╚══════════════════════════════════════╝""")
        opcion = pedir_opcion_menu("  Opción: ", ["1", "2", "3", "4", "5", "6"])
        if opcion == "1":
            gestion.registrar_ingeniero()
        elif opcion == "2":
            gestion.modificar_ingeniero()
        elif opcion == "3":
            gestion.devolver_equipo_ingeniero()
        elif opcion == "4":
            gestion.buscar_ingeniero()
        elif opcion == "5":
            gestion.listar_ingenieros()
        elif opcion == "6":
            break


def menu_diseno():
    while True:
        print("""
╔══════════════════════════════════════╗
║         ESTUDIANTES DISEÑO          ║
╠══════════════════════════════════════╣
║  1. Registrar préstamo              ║
║  2. Modificar datos                 ║
║  3. Devolver equipo                 ║
║  4. Buscar estudiante               ║
║  5. Listar todos                    ║
║  6. Volver al menú principal        ║
╚══════════════════════════════════════╝""")
        opcion = pedir_opcion_menu("  Opción: ", ["1", "2", "3", "4", "5", "6"])
        if opcion == "1":
            gestion.registrar_disenador()
        elif opcion == "2":
            gestion.modificar_disenador()
        elif opcion == "3":
            gestion.devolver_equipo_disenador()
        elif opcion == "4":
            gestion.buscar_disenador()
        elif opcion == "5":
            gestion.listar_disenadores()
        elif opcion == "6":
            break


def menu_equipos():
    while True:
        print("""
╔══════════════════════════════════════╗
║          GESTIÓN DE EQUIPOS         ║
╠══════════════════════════════════════╣
║  1. Registrar portátil              ║
║  2. Registrar tableta               ║
║  3. Ver inventario completo         ║
║  4. Volver al menú principal        ║
╚══════════════════════════════════════╝""")
        opcion = pedir_opcion_menu("  Opción: ", ["1", "2", "3", "4"])
        if opcion == "1":
            gestion.registrar_portatil()
        elif opcion == "2":
            gestion.registrar_tableta()
        elif opcion == "3":
            gestion.listar_equipos()
        elif opcion == "4":
            break


def main():
    while True:
        print("""
╔══════════════════════════════════════╗
║    SISTEMA DE PRÉSTAMO DE EQUIPOS   ║
║          San Juan de Dios           ║
╠══════════════════════════════════════╣
║  1. Gestión Estudiantes Ingeniería  ║
║  2. Gestión Estudiantes Diseño      ║
║  3. Gestión de Equipos              ║
║  4. Salir                           ║
╚══════════════════════════════════════╝""")
        opcion = pedir_opcion_menu("  Opción: ", ["1", "2", "3", "4"])
        if opcion == "1":
            menu_ingenieria()
        elif opcion == "2":
            menu_diseno()
        elif opcion == "3":
            menu_equipos()
        elif opcion == "4":
            print("\n  👋 Hasta luego!\n")
            break


if __name__ == "__main__":
    main()
