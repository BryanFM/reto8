from connection.conn import Conexion

class Estado_alquiler:
    def __init__(self):
        self.model = Conexion('estado_alquiler')

    def guardar_estado_alquiler(self, estado_alquiler):
        return self.model.insert(estado_alquiler)

    def obtener_estado_alquiler(self, id_estado_alquiler):
        return self.model.get_by_id(id_estado_alquiler)

    def obtener_estados_alquiler(self, order):
        return self.model.get_all(order)

    def buscar_estado_alquiler(self, data_estado_alquiler):
        return self.model.get_by_column(data_estado_alquiler)

    def modificar_estado_alquiler(self, id_estado_alquiler, data_estado_alquiler):
        return self.model.update(id_estado_alquiler, data_estado_alquiler)

    def eliminar_estado_alquiler(self, id_estado_alquiler):
        return self.model.delete(id_estado_alquiler)


