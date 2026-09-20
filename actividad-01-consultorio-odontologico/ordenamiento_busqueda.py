def ordenar_por_valor_atencion(lista_clientes):
    n = len(lista_clientes)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista_clientes[j].valor_atencion < lista_clientes[j + 1].valor_atencion:
                auxiliar = lista_clientes[j]  # variable temporal para no perder el dato
                lista_clientes[j] = lista_clientes[j + 1]
                lista_clientes[j + 1] = auxiliar

def buscar_cliente_por_cedula(lista_clientes, cedula):
    comparaciones = 0
    for cliente in lista_clientes:
        comparaciones += 1
        if cliente.cedula == cedula:
            return cliente, comparaciones
    return None, comparaciones
