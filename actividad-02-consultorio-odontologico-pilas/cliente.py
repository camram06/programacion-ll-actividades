class Cliente:
    """
    Representa a un cliente (paciente) del consultorio odontológico.
    """

    def __init__(self, nombre, tipo_atencion, prioridad, fecha_cita):
        self.nombre = nombre
        self.tipo_atencion = tipo_atencion  # Ej: "Extracción", "Limpieza", "Ortodoncia"
        self.prioridad = prioridad          # Ej: "Urgente", "Normal"
        self.fecha_cita = fecha_cita        # Formato: AAAA-MM-DD
