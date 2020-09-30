from connection.conn import Conexion

class Lector:
    def __init__(self):
        self.model = Conexion('nombre de bd')

    def guardar_lector(self, lector):
        return self.model.insert(periodo)

    def obtener_lector(self, id_lector):
        return self.model.get_by_id(id_lector)

    def obtener_lectores(self, order):
        return self.model.get_all(order)

    def buscar_lectores(self, data_genero):
        return self.model.get_by_column(data_genero)

    def modificar_lector(self, id_lector, data_lector):
        return self.model.update(id_lector, data_lector)

    def eliminar_lector(self, id_lector):
        return self.model.delete(id_genero)