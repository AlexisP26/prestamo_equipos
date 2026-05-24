from clases.validaciones import pedir_texto, pedir_serial, pedir_flotante, pedir_opcion_menu
from constantes import SISTEMAS_OPERATIVOS, PROCESADORES


class ComputadorPortatil:

    def __init__(self):
        self.__serial = ""
        self.__marca = ""
        self.__tamaño = 0.0
        self.__precio = 0.0
        self.__sistema_operativo = ""
        self.__procesador = ""
        self.__estado = "Disponible"  

    
    def get_serial(self):
        return self.__serial

    def get_marca(self):
        return self.__marca

    def get_tamaño(self):
        return self.__tamaño

    def get_precio(self):
        return self.__precio

    def get_sistema_operativo(self):
        return self.__sistema_operativo

    def get_procesador(self):
        return self.__procesador

    def get_estado(self):
        return self.__estado

    
    def set_marca(self, marca):
        self.__marca = marca

    def set_tamaño(self, tamaño):
        self.__tamaño = tamaño

    def set_precio(self, precio):
        self.__precio = precio

    def set_sistema_operativo(self, so):
        self.__sistema_operativo = so

    def set_procesador(self, procesador):
        self.__procesador = procesador

    def set_estado(self, estado):
        self.__estado = estado

    #SUBMENÚ SISTEMA OPERATIVO
    def __seleccionar_so(self):
        print("\n  Sistema Operativo:")
        for i, so in enumerate(SISTEMAS_OPERATIVOS, 1):
            print(f"    {i}. {so}")
        opcion = pedir_opcion_menu("  Opción: ", [str(i) for i in range(1, len(SISTEMAS_OPERATIVOS)+1)])
        return SISTEMAS_OPERATIVOS[int(opcion)-1]

    #SUBMENÚ PROCESADOR 
    def __seleccionar_procesador(self):
        print("\n  Procesador:")
        for i, p in enumerate(PROCESADORES, 1):
            print(f"    {i}. {p}")
        opcion = pedir_opcion_menu("  Opción: ", [str(i) for i in range(1, len(PROCESADORES)+1)])
        return PROCESADORES[int(opcion)-1]

    #MÉTODOS DE CAPTURA DE DATOS
    def capturar_datos(self):
        """Captura y valida todos los datos del equipo al registrar."""
        print("\n─── Registro Computador Portátil ───")
        self.__serial = pedir_serial("  Serial: ")
        self.__marca = pedir_texto("  Marca: ")
        self.__tamaño = pedir_flotante("  Tamaño en pulgadas (ej: 15.6): ", minimo=10.0)
        self.__precio = pedir_flotante("  Precio: ", minimo=0.0)
        self.__sistema_operativo = self.__seleccionar_so()
        self.__procesador = self.__seleccionar_procesador()
        self.__estado = "Disponible"

    def modificar_datos(self):
        """Permite modificar solo los campos permitidos (no serial)."""
        print("\n─── Modificar Computador Portátil ───")
        print("  (Serial no se puede modificar)")
        self.__marca = pedir_texto("  Nueva marca: ")
        self.__tamaño = pedir_flotante("  Nuevo tamaño en pulgadas: ", minimo=10.0)
        self.__precio = pedir_flotante("  Nuevo precio: ", minimo=0.0)
        self.__sistema_operativo = self.__seleccionar_so()
        self.__procesador = self.__seleccionar_procesador()

    #METODO DE IMPRESIÓN
    def imprimir(self):
        print(f"""
  ┌─ Computador Portátil ────────────────
  │  Serial:            {self.__serial}
  │  Marca:             {self.__marca}
  │  Tamaño:            {self.__tamaño}"
  │  Precio:            ${self.__precio:,.2f}
  │  Sistema Operativo: {self.__sistema_operativo}
  │  Procesador:        {self.__procesador}
  │  Estado:            {self.__estado}
  └──────────────────────────────────────""")