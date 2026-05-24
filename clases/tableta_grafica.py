# tableta_grafica.py
# Clase TabletaGrafica - Proyecto Gestión Préstamo Equipos

from clases.validaciones import pedir_texto, pedir_serial, pedir_flotante, pedir_opcion_menu


class TabletaGrafica:

    def __init__(self):
        self.__serial = ""
        self.__marca = ""
        self.__tamaño = 0.0
        self.__precio = 0.0
        self.__almacenamiento = ""
        self.__peso = 0.0
        self.__estado = "Disponible"  

    def get_serial(self):
        return self.__serial

    def get_marca(self):
        return self.__marca

    def get_tamaño(self):
        return self.__tamaño

    def get_precio(self):
        return self.__precio

    def get_almacenamiento(self):
        return self.__almacenamiento

    def get_peso(self):
        return self.__peso

    def get_estado(self):
        return self.__estado

    
    def set_marca(self, marca):
        self.__marca = marca

    def set_tamaño(self, tamaño):
        self.__tamaño = tamaño

    def set_precio(self, precio):
        self.__precio = precio

    def set_almacenamiento(self, almacenamiento):
        self.__almacenamiento = almacenamiento

    def set_peso(self, peso):
        self.__peso = peso

    def set_estado(self, estado):
        self.__estado = estado

    # SUBMENÚ ALMACENAMIENTO 
    def __seleccionar_almacenamiento(self):
        print("\n  Almacenamiento:")
        print("    1.  64 GB")
        print("    2. 128 GB")
        print("    3. 256 GB")
        print("    4. 512 GB")
        opcion = pedir_opcion_menu("  Opción: ", ["1", "2", "3", "4"])
        opciones = {"1": "64 GB", "2": "128 GB", "3": "256 GB", "4": "512 GB"}
        return opciones[opcion]

    # MÉTODOS DE CAPTURA DE DATOS
    def capturar_datos(self):
        """Captura y valida todos los datos de la tableta al registrar."""
        print("\n─── Registro Tableta Gráfica ───")
        self.__serial = pedir_serial("  Serial: ")
        self.__marca = pedir_texto("  Marca: ")
        self.__tamaño = pedir_flotante("  Tamaño en pulgadas (ej: 10.5): ", minimo=7.0)
        self.__precio = pedir_flotante("  Precio: ", minimo=0.0)
        self.__almacenamiento = self.__seleccionar_almacenamiento()
        self.__peso = pedir_flotante("  Peso en kg (ej: 0.5): ", minimo=0.1)
        self.__estado = "Disponible"

    def modificar_datos(self):
        """Permite modificar solo los campos permitidos (no serial)."""
        print("\n─── Modificar Tableta Gráfica ───")
        print("  (Serial no se puede modificar)")
        self.__marca = pedir_texto("  Nueva marca: ")
        self.__tamaño = pedir_flotante("  Nuevo tamaño en pulgadas: ", minimo=7.0)
        self.__precio = pedir_flotante("  Nuevo precio: ", minimo=0.0)
        self.__almacenamiento = self.__seleccionar_almacenamiento()
        self.__peso = pedir_flotante("  Nuevo peso en kg: ", minimo=0.1)

    # IMPRIMIR 
    def imprimir(self):
        print(f"""
  ┌─ Tableta Gráfica ────────────────────
  │  Serial:            {self.__serial}
  │  Marca:             {self.__marca}
  │  Tamaño:            {self.__tamaño}"
  │  Precio:            ${self.__precio:,.2f}
  │  Almacenamiento:    {self.__almacenamiento}
  │  Peso:              {self.__peso} kg
  │  Estado:            {self.__estado}
  └──────────────────────────────────────""")
