from clases.validaciones import pedir_texto, pedir_cedula, pedir_telefono, pedir_entero, pedir_flotante, pedir_serial
from constantes import SEMESTRE_MIN, SEMESTRE_MAX, PROMEDIO_MIN, PROMEDIO_MAX

class EstudianteIngenieria:

    def __init__(self):
        self.__cedula = ""
        self.__nombre = ""
        self.__apellido = ""
        self.__telefono = ""
        self.__semestre = 0
        self.__promedio = 0.0
        self.__serial_equipo = ""

    
    def get_cedula(self):
        return self.__cedula

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_telefono(self):
        return self.__telefono

    def get_semestre(self):
        return self.__semestre

    def get_promedio(self):
        return self.__promedio

    def get_serial_equipo(self):
        return self.__serial_equipo

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_semestre(self, semestre):
        self.__semestre = semestre

    def set_promedio(self, promedio):
        self.__promedio = promedio

    def set_serial_equipo(self, serial):
        self.__serial_equipo = serial

    def capturar_datos(self):
        print("\n─── Registro Estudiante Ingeniería ───")
        self.__cedula = pedir_cedula("  Cédula: ")
        self.__nombre = pedir_texto("  Nombre: ")
        self.__apellido = pedir_texto("  Apellido: ")
        self.__telefono = pedir_telefono("  Teléfono: ")
        self.__semestre = pedir_entero("  Semestre: ", minimo=SEMESTRE_MIN, maximo=SEMESTRE_MAX)
        self.__promedio = pedir_flotante("  Promedio acumulado: ", minimo=PROMEDIO_MIN)
        self.__serial_equipo = pedir_serial("  Serial del equipo a prestar: ")

    def modificar_datos(self):
        """Permite modificar solo los campos permitidos (no cédula ni serial)."""
        print("\n─── Modificar Estudiante Ingeniería ───")
        print("  (Cédula y serial no se pueden modificar)")
        self.__nombre = pedir_texto("  Nuevo nombre: ")
        self.__apellido = pedir_texto("  Nuevo apellido: ")
        self.__telefono = pedir_telefono("  Nuevo teléfono: ")
        self.__semestre = pedir_entero("  Nuevo semestre: ", minimo=SEMESTRE_MIN, maximo=SEMESTRE_MAX)
        self.__promedio = pedir_flotante("  Nuevo promedio: ", minimo=PROMEDIO_MIN)

    def imprimir(self):
        print(f"""
  ┌─ Estudiante Ingeniería ──────────────
  │  Cédula:          {self.__cedula}
  │  Nombre:          {self.__nombre} {self.__apellido}
  │  Teléfono:        {self.__telefono}
  │  Semestre:        {self.__semestre}
  │  Promedio:        {self.__promedio}
  │  Serial equipo:   {self.__serial_equipo}
  └──────────────────────────────────────""")
