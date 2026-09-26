from datetime import datetime

from cliente import Cliente
from consultorio import Consultorio

def solicitar_nombre():
    while True:
        nombre = input("Ingrese el nombre del cliente: ")
        if nombre.strip() == "":
            print("ERROR: El nombre no puede estar vacío ni contener solo espacios.")
        else:
            return nombre.strip()

def solicitar_opcion_entero(mensaje, minimo, maximo):
    while True:
        entrada = input(mensaje)
        try:
            opcion = int(entrada)
        except ValueError:
            print("ERROR: Debe ingresar un valor numérico entero.")
            continue

        if opcion < minimo or opcion > maximo:
            print(f"ERROR: La opción debe estar entre {minimo} y {maximo}.")
        else:
            return opcion

def solicitar_tipo_atencion():
    opciones_tipo_atencion = {
        1: "Extracción",
        2: "Limpieza",
        3: "Ortodoncia",
        4: "Revisión general",
    }
    print("Tipo de atención odontológica:")
    for numero, tipo in opciones_tipo_atencion.items():
        print(f"  {numero}. {tipo}")

    opcion = solicitar_opcion_entero("Seleccione una opción: ", 1, len(opciones_tipo_atencion))
    return opciones_tipo_atencion[opcion]

def solicitar_prioridad():
    opciones_prioridad = {
        1: "Urgente",
        2: "Normal",
    }
    print("Prioridad de la cita:")
    for numero, prioridad in opciones_prioridad.items():
        print(f"  {numero}. {prioridad}")

    opcion = solicitar_opcion_entero("Seleccione una opción: ", 1, len(opciones_prioridad))
    return opciones_prioridad[opcion]


def solicitar_fecha_cita():
    while True:
        fecha_texto = input("Ingrese la fecha de la cita (formato AAAA-MM-DD): ")
        fecha_texto = fecha_texto.strip()

        if fecha_texto == "":
            print("ERROR: La fecha no puede estar vacía.")
            continue

        try:
            datetime.strptime(fecha_texto, "%Y-%m-%d")
        except ValueError:
            print("ERROR: Fecha inválida. Use el formato AAAA-MM-DD, por ejemplo 2026-10-05.")
            continue

        return fecha_texto

def registrar_cliente(consultorio: Consultorio):
    print("\n--- Registrar cliente en la agenda ---")
    nombre = solicitar_nombre()
    tipo_atencion = solicitar_tipo_atencion()
    prioridad = solicitar_prioridad()
    fecha_cita = solicitar_fecha_cita()

    cliente = Cliente(nombre, tipo_atencion, prioridad, fecha_cita)
    consultorio.agendar_cliente(cliente)
    print(f"Cliente '{nombre}' agendado correctamente.")

def mostrar_menu():
    print("\n----- CONSULTORIO ODONTOLÓGICO -----")
    print("1. Registrar cliente en la agenda (Cola)")
    print("2. Atender siguiente cliente de la agenda (Cola)")
    print("3. Consultar siguiente cliente de la agenda")
    print("4. Consultar toda la agenda")
    print("5. Generar pila de urgencias de extracción")
    print("6. Atender siguiente urgencia de extracción (Pila)")
    print("7. Generar informe de la pila de urgencias")
    print("8. Salir")

def main():
    consultorio = Consultorio("Consultorio Odontológico Sonrisa Sana")

    while True:
        mostrar_menu()
        opcion = solicitar_opcion_entero("Ingrese una opción (1...8): ", 1, 8)

        if opcion == 1:
            registrar_cliente(consultorio)

        elif opcion == 2:
            consultorio.atender_siguiente_cliente()

        elif opcion == 3:
            consultorio.consultar_siguiente_cliente()

        elif opcion == 4:
            consultorio.consultar_toda_la_agenda()

        elif opcion == 5:
            consultorio.generar_pila_urgencias_extraccion()

        elif opcion == 6:
            consultorio.atender_siguiente_urgencia()

        elif opcion == 7:
            consultorio.generar_informe_pila_urgencias()

        elif opcion == 8:
            print("Saliendo del sistema del consultorio...")
            break

if __name__ == "__main__":
    main()
