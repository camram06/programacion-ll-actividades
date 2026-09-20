from datetime import datetime
from ordenamiento_busqueda import buscar_cliente_por_cedula

def pedir_nombre():
    while True:
        nombre = input("Nombre completo: ").strip()
        if nombre == "":
            print("ERROR: el nombre no puede estar vacío")
        elif not nombre.replace(" ", "").isalpha():  # solo letras (y espacios)
            print("ERROR: el nombre solo puede tener letras y espacios")
        else:
            return nombre

def pedir_cedula(lista_clientes):
    while True:
        cedula = input("Cédula: ").strip()
        if cedula == "":
            print("ERROR: la cédula no puede estar vacía")
        elif not cedula.isdigit():  # True si son solo números
            print("ERROR: la cédula solo acepta números")
        elif len(cedula) < 6 or len(cedula) > 10:
            print("ERROR: la cédula debe tener entre 6 y 10 dígitos")
        elif buscar_cliente_por_cedula(lista_clientes, cedula)[0] is not None:
            print("ERROR: ya existe un cliente con esa cédula")
        else:
            return cedula

def pedir_telefono():
    while True:
        telefono = input("Teléfono: ").strip()
        if telefono == "":
            print("ERROR: el teléfono no puede estar vacío")
        elif not telefono.isdigit():
            print("ERROR: el teléfono solo acepta números")
        elif len(telefono) < 7 or len(telefono) > 10:
            print("ERROR: el teléfono debe tener entre 7 y 10 dígitos")
        else:
            return telefono

def pedir_opcion(titulo, opciones):
    while True:
        print(titulo)
        for i in range(len(opciones)):
            print(f"  {i + 1}. {opciones[i]}")
        texto = input("Seleccione una opción: ").strip()
        if texto == "":
            print("ERROR: debe escribir una opción")
            continue
        try:
            numero = int(texto)
        except ValueError:
            print("ERROR: solo se aceptan números")
            continue
        if numero < 1 or numero > len(opciones):
            print(f"ERROR: elija un número entre 1 y {len(opciones)}")
        else:
            return opciones[numero - 1]

def pedir_cantidad():
    while True:
        texto = input("Cantidad: ").strip()
        if texto == "":
            print("ERROR: la cantidad no puede estar vacía")
            continue
        try:
            cantidad = int(texto)
        except ValueError:
            print("ERROR: la cantidad solo acepta números enteros")
            continue
        if cantidad <= 0:
            print("ERROR: la cantidad debe ser mayor que cero")
        else:
            return cantidad


def pedir_fecha():
    while True:
        texto = input("Fecha de la cita (DD/MM/AAAA): ").strip()
        if texto == "":
            print("ERROR: la fecha no puede estar vacía")
            continue
        try:
            datetime.strptime(texto, "%d/%m/%Y")
            return texto
        except ValueError:
            print("ERROR: fecha inválida. Ejemplo válido: 25/09/2026")
