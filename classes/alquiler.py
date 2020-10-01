from connection.conn import Conexion

class Alquiler:
    def __init__(self):
        self.model = Conexion('alquiler')

    def guardar_alquiler(self, alquiler):
        return self.model.insert(alquiler)

    def obtener_alquiler(self, id_alquiler):
        return self.model.get_by_id(id_alquiler)

    def obtener_alquilers(self, order):
        return self.model.get_all(order)

    def buscar_alquiler(self, data_alquiler):
        return self.model.get_by_column(data_alquiler)

    def modificar_alquiler(self, id_alquiler, data_alquiler):
        return self.model.update(id_alquiler, data_alquiler)

    def eliminar_alquiler(self, id_alquiler):
        return self.model.delete(id_alquiler)