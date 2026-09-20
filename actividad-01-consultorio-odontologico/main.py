from cliente import Cliente, formato_pesos
from validaciones import (pedir_nombre, pedir_cedula, pedir_telefono,
                          pedir_opcion, pedir_cantidad, pedir_fecha)
from ordenamiento_busqueda import ordenar_por_valor_atencion, buscar_cliente_por_cedula

def registrar_cliente(lista_clientes):
    print("\n--- Registrar cliente ---")
    cedula = pedir_cedula(lista_clientes)
    nombre = pedir_nombre()
    telefono = pedir_telefono()
    tipo_cliente = pedir_opcion("Tipo de cliente:", ["Particular", "EPS", "Prepagada"])
    tipo_atencion = pedir_opcion("Tipo de atención:",
                                 ["Limpieza", "Calzas", "Extracción", "Diagnóstico"])

    if tipo_atencion == "Limpieza" or tipo_atencion == "Diagnóstico":
        cantidad = 1
        print("Cantidad asignada automáticamente: 1")
    else:
        cantidad = pedir_cantidad()

    prioridad = pedir_opcion("Prioridad de atención:", ["Normal", "Urgente"])
    fecha = pedir_fecha()

    cliente = Cliente(cedula, nombre, telefono, tipo_cliente,
                      tipo_atencion, cantidad, prioridad, fecha)
    lista_clientes.append(cliente)
    print("Cliente registrado. Total a pagar:", formato_pesos(cliente.total_a_pagar))


# Calcula y muestra los 3 resultados que pide el enunciado
def mostrar_resumen(lista_clientes):
    total_clientes = len(lista_clientes)
    ingresos_totales = 0
    clientes_extraccion = 0

    for cliente in lista_clientes:
        ingresos_totales += cliente.total_a_pagar
        if cliente.tipo_atencion == "Extracción":
            clientes_extraccion += 1

    print("\n--- Resumen ---")
    print("Total de clientes:", total_clientes)
    print("Ingresos totales:", formato_pesos(ingresos_totales))
    print("Clientes que van a extracción:", clientes_extraccion)


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================
if __name__ == "__main__":

    lista_clientes = []  # arreglo en memoria donde se guardan los clientes
    salir = False

    while salir == False:
        opcion = pedir_opcion("\n===== CONSULTORIO ODONTOLÓGICO Dr. JOHAN RAMIREZ =====", [
            "Registrar cliente",
            "Ver resumen",
            "Ver clientes ordenados por valor de atención (mayor a menor)",
            "Buscar cliente por cédula",
            "Salir",
        ])

        if opcion == "Salir":
            salir = True
            print("Hasta luego.")

        elif len(lista_clientes) == 0 and opcion != "Registrar cliente":
            print("Aún no hay clientes registrados. Registre al menos uno.")

        elif opcion == "Registrar cliente":
            registrar_cliente(lista_clientes)

        elif opcion == "Ver resumen":
            mostrar_resumen(lista_clientes)

        elif opcion.startswith("Ver clientes ordenados"):
            ordenar_por_valor_atencion(lista_clientes)
            print("\n--- Clientes de mayor a menor valor de atención ---")
            for cliente in lista_clientes:
                cliente.mostrar()
                print()

        else:  # Buscar cliente por cédula
            ordenar_por_valor_atencion(lista_clientes)
            cedula_buscada = input("Cédula a buscar: ").strip()
            if cedula_buscada == "":
                print("ERROR: la cédula no puede estar vacía")
            else:
                cliente, comparaciones = buscar_cliente_por_cedula(lista_clientes, cedula_buscada)
                if cliente is not None:
                    print(f"Cliente encontrado ({comparaciones} comparaciones):")
                    cliente.mostrar()
                else:
                    print(f"No existe un cliente con la cédula {cedula_buscada} "
                          f"({comparaciones} comparaciones)")
