from connection.conn import Conexion

class Estado_lector:
    def __init__(self):
        self.model = Conexion('estado_lector')

    def guardar_estado_lector(self, estado_lector):
        return self.model.insert(estado_lector)

    def obtener_estado_lector(self, id_estado_lector):
        return self.model.get_by_id(id_estado_lector)

    def obtener_estados_lector(self, order):
        return self.model.get_all(order)

    def buscar_estado_lector(self, data_estado_lector):
        return self.model.get_by_column(data_estado_lector)

    def modificar_estado_lector(self, id_estado_lector, data_estado_lector):
        return self.model.update(id_estado_lector, data_estado_lector)

    def eliminar_estado_lector(self, id_estado_lector):
        return self.model.delete(id_estado_lector)