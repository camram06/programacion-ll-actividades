from collections import deque

from cliente import Cliente


class Consultorio:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cola_atencion_general = deque()
        self.pila_urgencias_extraccion = deque()

    # ------------------------------------------------------------------
    # COLA DE ATENCIÓN GENERAL (FIFO)
    # ------------------------------------------------------------------

    def agendar_cliente(self, cliente: Cliente):
        self.cola_atencion_general.append(cliente)

    def atender_siguiente_cliente(self):
        if self.cola_atencion_general:
            cliente = self.cola_atencion_general.popleft()
            print(f"Atendiendo a: {cliente.nombre} "
                  f"(Tratamiento: {cliente.tipo_atencion}, Prioridad: {cliente.prioridad})")
        else:
            print("No hay clientes en la agenda para atender.")

    def consultar_siguiente_cliente(self):
        # Peek: se consulta sin sacarlo de la cola
        if self.cola_atencion_general:
            cliente = self.cola_atencion_general[0]
            print(f"El siguiente cliente de la agenda es: {cliente.nombre}")
        else:
            print("No hay clientes en la agenda.")

    def consultar_toda_la_agenda(self):
        if not self.cola_atencion_general:
            print("No hay clientes en la agenda.")
            return

        print("Clientes pendientes en la agenda (en estricto orden de atención):")
        for cliente in self.cola_atencion_general:
            print(f"- {cliente.nombre} | Tratamiento: {cliente.tipo_atencion} | "
                  f"Prioridad: {cliente.prioridad} | Fecha de cita: {cliente.fecha_cita}")

    # ------------------------------------------------------------------
    # PILA DE URGENCIAS DE EXTRACCIÓN (LIFO)
    # ------------------------------------------------------------------

    def generar_pila_urgencias_extraccion(self):
        clientes_urgentes = []
        for cliente in self.cola_atencion_general:
            if cliente.tipo_atencion == "Extracción" and cliente.prioridad == "Urgente":
                clientes_urgentes.append(cliente)

        self.pila_urgencias_extraccion = deque()

        if not clientes_urgentes:
            print("No se encontraron clientes de extracción con prioridad urgente en la agenda.")
            return

        clientes_urgentes.sort(key=lambda cliente: cliente.fecha_cita, reverse=True)

        for cliente in clientes_urgentes:
            self.pila_urgencias_extraccion.append(cliente)

        print(f"Pila de urgencias generada con {len(self.pila_urgencias_extraccion)} cliente(s).")

    def atender_siguiente_urgencia(self):
        if self.pila_urgencias_extraccion:
            cliente = self.pila_urgencias_extraccion.pop()
            print(f"Llamando con urgencia a: {cliente.nombre} (fecha de cita: {cliente.fecha_cita})")
        else:
            print("No hay clientes urgentes de extracción pendientes. "
                  "Genere la pila primero (opción 5 del menú).")

    def generar_informe_pila_urgencias(self):
        if not self.pila_urgencias_extraccion:
            print("La pila de urgencias está vacía. Genere la pila primero (opción 5 del menú).")
            return

        print("\n=== INFORME: PILA DE URGENCIAS DE EXTRACCIÓN ===")
        print("Orden en que deben ser llamados (de la fecha más cercana a la más lejana):")
        for posicion, cliente in enumerate(reversed(self.pila_urgencias_extraccion), start=1):
            print(f"{posicion}. {cliente.nombre} | Fecha de cita: {cliente.fecha_cita}")
        print("=" * 50)
