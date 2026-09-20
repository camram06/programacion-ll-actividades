from tarifas import obtener_valor_cita, obtener_valor_unitario_atencion

def formato_pesos(valor):
    return "$" + f"{valor:,.0f}".replace(",", ".")

class Cliente:

    def __init__(self, cedula, nombre, telefono, tipo_cliente,
                 tipo_atencion, cantidad, prioridad, fecha):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.tipo_cliente = tipo_cliente
        self.tipo_atencion = tipo_atencion
        self.cantidad = cantidad
        self.prioridad = prioridad
        self.fecha = fecha

        self.valor_cita = obtener_valor_cita(tipo_cliente)
        valor_unitario = obtener_valor_unitario_atencion(tipo_cliente, tipo_atencion)
        self.valor_atencion = valor_unitario * cantidad
        self.total_a_pagar = self.valor_cita + self.valor_atencion

    # Muestra por consola todos los datos del cliente 
    def mostrar(self):
        print(f"  Cédula: {self.cedula} | Nombre: {self.nombre} | Tel: {self.telefono}")
        print(f"  {self.tipo_cliente} | {self.tipo_atencion} x{self.cantidad} | "
              f"Prioridad: {self.prioridad} | Fecha: {self.fecha}")
        print(f"  Cita: {formato_pesos(self.valor_cita)} | "
              f"Atención: {formato_pesos(self.valor_atencion)} | "
              f"TOTAL: {formato_pesos(self.total_a_pagar)}")
