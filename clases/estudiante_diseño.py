from clases.validaciones import pedir_texto, pedir_cedula, pedir_telefono, pedir_entero, pedir_opcion_menu
from constantes import ASIGNATURAS_MIN, MODALIDADES, ASIGNATURAS_MAX


class EstudianteDiseño:

    def __init__(self):
        self.__cedula = ""
        self.__nombre = ""
        self.__apellido = ""
        self.__telefono = ""
        self.__modalidad = ""
        self.__cant_asignaturas = 0
        self.__serial_equipo = ""

    
    def get_cedula(self):
        return self.__cedula

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_telefono(self):
        return self.__telefono

    def get_modalidad(self):
        return self.__modalidad

    def get_cant_asignaturas(self):
        return self.__cant_asignaturas

    def get_serial_equipo(self):
        return self.__serial_equipo

    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_modalidad(self, modalidad):
        self.__modalidad = modalidad

    def set_cant_asignaturas(self, cant):
        self.__cant_asignaturas = cant

    def set_serial_equipo(self, serial):
        self.__serial_equipo = serial

    # MÉTODOS DE CAPTURA DE DATOS
    def capturar_datos(self):
        """Captura y valida todos los datos del estudiante al registrar."""
        print("\n─── Registro Estudiante Diseño ───")
        self.__cedula = pedir_cedula("  Cédula: ")
        self.__nombre = pedir_texto("  Nombre: ")
        self.__apellido = pedir_texto("  Apellido: ")
        self.__telefono = pedir_telefono("  Teléfono: ")

        print("\n  Modalidad:")
        print("    1. Virtual")
        print("    2. Presencial")
        opcion = pedir_opcion_menu("  Opción: ", ["1", "2"])
        self.__modalidad = "Virtual" if opcion == "1" else "Presencial"

        self.__cant_asignaturas = pedir_entero("  Cantidad de asignaturas (1-10): ", minimo=1, maximo=10)
        self.__serial_equipo = pedir_texto("  Serial del equipo a prestar: ")

    def modificar_datos(self):
        """Permite modificar solo los campos permitidos (no cédula ni serial)."""
        print("\n─── Modificar Estudiante Diseño ───")
        print("  (Cédula y serial no se pueden modificar)")
        self.__nombre = pedir_texto("  Nuevo nombre: ")
        self.__apellido = pedir_texto("  Nuevo apellido: ")
        self.__telefono = pedir_telefono("  Nuevo teléfono: ")

        print("\n  Nueva modalidad:")
        for i, m in enumerate(MODALIDADES, 1):
            print(f"    {i}. {m}")
        opcion = pedir_opcion_menu("  Opción: ", [str(i) for i in range(1, len(MODALIDADES)+1)])
        self.__modalidad = MODALIDADES[int(opcion)-1]
        self.__cant_asignaturas = pedir_entero("  Cantidad de asignaturas: ", minimo=ASIGNATURAS_MIN, maximo=ASIGNATURAS_MAX)
    # IMPRIMIR 
    def imprimir(self):
        print(f"""
  ┌─ Estudiante Diseño ──────────────────
  │  Cédula:            {self.__cedula}
  │  Nombre:            {self.__nombre} {self.__apellido}
  │  Teléfono:          {self.__telefono}
  │  Modalidad:         {self.__modalidad}
  │  Asignaturas:       {self.__cant_asignaturas}
  │  Serial equipo:     {self.__serial_equipo}
  └──────────────────────────────────────""")
