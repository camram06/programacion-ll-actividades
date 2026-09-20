def obtener_valor_cita(tipo_cliente):
    if tipo_cliente == "Particular":
        return 80000
    elif tipo_cliente == "EPS":
        return 5000
    else:  # si no es Particular ni EPS, entonces es Prepagada
        return 30000

def obtener_valor_unitario_atencion(tipo_cliente, tipo_atencion):
    if tipo_cliente == "Particular":
        if tipo_atencion == "Limpieza":
            return 60000
        elif tipo_atencion == "Calzas":
            return 80000
        elif tipo_atencion == "Extracción":
            return 100000
        else:  # Diagnóstico
            return 50000

    elif tipo_cliente == "EPS":
        if tipo_atencion == "Limpieza":
            return 0
        elif tipo_atencion == "Calzas":
            return 40000
        elif tipo_atencion == "Extracción":
            return 40000
        else:  # Diagnóstico
            return 0

    else:  # Prepagada
        if tipo_atencion == "Limpieza":
            return 0
        elif tipo_atencion == "Calzas":
            return 10000
        elif tipo_atencion == "Extracción":
            return 10000
        else:  # Diagnóstico
            return 0
