from connection.conn import Conexion

class Lector:
    def __init__(self):
        self.model = Conexion('sistema_biblioteca')

    def guardar_lector(self, lector):
        return self.model.insert(lector)

    def obtener_lector(self, lector_id):
        return self.model.get_by_id(lector_id)

    def obtener_lectores(self, order):
        return self.model.get_all(order)

    def buscar_lectores(self, data_lector):
        return self.model.get_by_column(data_lector)

    def modificar_lector(self, id_lector, data_lector):
        return self.model.update(id_lector, data_lector)

    def eliminar_lector(self, lector_id):
        return self.model.delete(lector_id)