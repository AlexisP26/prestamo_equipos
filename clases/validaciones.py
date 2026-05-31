def pedir_texto(mensaje):
    """Solo letras y espacios. Sin números ni caracteres especiales."""
    valor = input(mensaje).strip()
    if not valor:
        print("El campo no puede estar vacío.")
        return pedir_texto(mensaje)
    if len(valor) < 2:
        print("Debe ingresar al menos 2 caracteres.")
        return pedir_texto(mensaje)
    if not all(c.isalpha() or c.isspace() for c in valor):
        print("Solo se permiten letras, sin números ni símbolos.")
        return pedir_texto(mensaje)
    if "  " in valor:
        print("No se permiten espacios consecutivos.")
        return pedir_texto(mensaje)
    if not valor.replace(" ", ""):
        print("El campo no puede ser solo espacios.")
        return pedir_texto(mensaje)
    return valor


def pedir_cedula(mensaje):
    """Solo números, longitud entre 6 y 12 dígitos, no puede ser cero."""
    valor = input(mensaje).strip()
    if not valor:
        print("El campo no puede estar vacío.")
        return pedir_cedula(mensaje)
    if not valor.isdigit():
        print("La cédula solo puede contener números.")
        return pedir_cedula(mensaje)
    if len(valor) < 6 or len(valor) > 12:
        print("La cédula debe tener entre 6 y 12 dígitos.")
        return pedir_cedula(mensaje)
    if int(valor) == 0:
        print("La cédula no puede ser cero.")
        return pedir_cedula(mensaje)
    return valor


def pedir_telefono(mensaje):
    """Solo números, exactamente 10 dígitos, debe empezar en 3."""
    valor = input(mensaje).strip()
    if not valor:
        print("El campo no puede estar vacío.")
        return pedir_telefono(mensaje)
    if not valor.isdigit():
        print("El teléfono solo puede contener números.")
        return pedir_telefono(mensaje)
    if len(valor) != 10:
        print("El teléfono debe tener exactamente 10 dígitos.")
        return pedir_telefono(mensaje)
    if valor[0] != "3":
        print("El teléfono debe empezar en 3 (ej: 3001234567).")
        return pedir_telefono(mensaje)
    return valor


def pedir_serial(mensaje):
    """Alfanumérico, longitud entre 4 y 15 caracteres, sin símbolos."""
    valor = input(mensaje).strip()
    if not valor:
        print("El campo no puede estar vacío.")
        return pedir_serial(mensaje)
    if not valor.isalnum():
        print("El serial solo puede contener letras y números, sin símbolos.")
        return pedir_serial(mensaje)
    if len(valor) < 4 or len(valor) > 15:
        print("El serial debe tener entre 4 y 15 caracteres.")
        return pedir_serial(mensaje)
    return valor


def pedir_entero(mensaje, minimo=None, maximo=None):
    """Número entero, con rango opcional."""
    valor = input(mensaje).strip()
    if not valor.lstrip('-').isdigit():
        print("Debe ingresar un número entero válido.")
        return pedir_entero(mensaje, minimo, maximo)
    valor = int(valor)
    if minimo is not None and valor < minimo:
        print(f"El valor mínimo permitido es {minimo}.")
        return pedir_entero(mensaje, minimo, maximo)
    if maximo is not None and valor > maximo:
        print(f"El valor máximo permitido es {maximo}.")
        return pedir_entero(mensaje, minimo, maximo)
    return valor


def pedir_flotante(mensaje, minimo=0.0, maximo=None):
    """Número decimal con rango opcional."""
    valor = input(mensaje).strip()
    try:
        valor = float(valor)
        if valor < minimo:
            print(f"El valor debe ser mayor o igual a {minimo}.")
            return pedir_flotante(mensaje, minimo, maximo)
        if maximo is not None and valor > maximo:
            print(f"El valor debe ser menor o igual a {maximo}.")
            return pedir_flotante(mensaje, minimo, maximo)
        return valor
    except ValueError:
        print("Debe ingresar un número decimal válido (ej: 15.5).")
        return pedir_flotante(mensaje, minimo, maximo)


def pedir_precio(mensaje):
    """Número decimal, mínimo $100."""
    valor = input(mensaje).strip()
    try:
        valor = float(valor)
        if valor < 100:
            print("El precio no puede ser menor a $100.")
            return pedir_precio(mensaje)
        return valor
    except ValueError:
        print("Debe ingresar un número decimal válido (ej: 2500000).")
        return pedir_precio(mensaje)


def pedir_opcion_menu(mensaje, opciones_validas):
    """Valida que la opción ingresada esté dentro de las permitidas."""
    valor = input(mensaje).strip()
    if valor not in opciones_validas:
        print(f"Opción inválida. Elija entre: {', '.join(opciones_validas)}")
        return pedir_opcion_menu(mensaje, opciones_validas)
    return valor


def confirmar_accion(mensaje):
    """Confirmación S/N antes de ejecutar una acción crítica."""
    valor = input(f"{mensaje} (S/N): ").strip().upper()
    if valor not in ["S", "N"]:
        print(" Ingrese S para confirmar o N para cancelar.")
        return confirmar_accion(mensaje)
    return valor == "S"
