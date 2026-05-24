def pedir_texto(mensaje):
    """Solo letras y espacios. Sin números ni caracteres especiales."""
    valor = input(mensaje).strip()
    if not valor:
        print("❌ El campo no puede estar vacío.")
        return pedir_texto(mensaje)
    if not all(c.isalpha() or c.isspace() for c in valor):
        print("❌ Solo se permiten letras, sin números ni símbolos.")
        return pedir_texto(mensaje)
    return valor


def pedir_cedula(mensaje):
    """Solo números, sin caracteres especiales."""
    valor = input(mensaje).strip()
    if not valor:
        print("❌ El campo no puede estar vacío.")
        return pedir_cedula(mensaje)
    if not valor.isdigit():
        print("❌ La cédula solo puede contener números.")
        return pedir_cedula(mensaje)
    return valor


def pedir_telefono(mensaje):
    """Solo números."""
    valor = input(mensaje).strip()
    if not valor:
        print("❌ El campo no puede estar vacío.")
        return pedir_telefono(mensaje)
    if not valor.isdigit():
        print("❌ El teléfono solo puede contener números.")
        return pedir_telefono(mensaje)
    return valor


def pedir_serial(mensaje):
    """Alfanumérico, sin caracteres especiales."""
    valor = input(mensaje).strip()
    if not valor:
        print("❌ El campo no puede estar vacío.")
        return pedir_serial(mensaje)
    if not valor.isalnum():
        print("❌ El serial solo puede contener letras y números, sin símbolos.")
        return pedir_serial(mensaje)
    return valor


def pedir_entero(mensaje, minimo=None, maximo=None):
    """Número entero, con rango opcional."""
    valor = input(mensaje).strip()
    if not valor.lstrip('-').isdigit():
        print("❌ Debe ingresar un número entero válido.")
        return pedir_entero(mensaje, minimo, maximo)
    valor = int(valor)
    if minimo is not None and valor < minimo:
        print(f"❌ El valor mínimo permitido es {minimo}.")
        return pedir_entero(mensaje, minimo, maximo)
    if maximo is not None and valor > maximo:
        print(f"❌ El valor máximo permitido es {maximo}.")
        return pedir_entero(mensaje, minimo, maximo)
    return valor


def pedir_flotante(mensaje, minimo=0.0):
    """Número decimal positivo."""
    valor = input(mensaje).strip()
    try:
        valor = float(valor)
        if valor < minimo:
            print(f"❌ El valor debe ser mayor o igual a {minimo}.")
            return pedir_flotante(mensaje, minimo)
        return valor
    except ValueError:
        print("❌ Debe ingresar un número decimal válido (ej: 15.5).")
        return pedir_flotante(mensaje, minimo)


def pedir_opcion_menu(mensaje, opciones_validas):
    """Valida que la opción ingresada esté dentro de las permitidas."""
    valor = input(mensaje).strip()
    if valor not in opciones_validas:
        print(f"❌ Opción inválida. Elija entre: {', '.join(opciones_validas)}")
        return pedir_opcion_menu(mensaje, opciones_validas)
    return valor
