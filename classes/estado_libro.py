from connection.conn import Conexion

class Estado_libro:
    def __init__(self):
        self.model = Conexion('estado_libro')

    def guardar_estado_libro(self, estado_libro):
        return self.model.insert(estado_libro)

    def obtener_estado_libro(self, id_estado_libro):
        return self.model.get_by_id(id_estado_libro)

    def obtener_estados_libro(self, order):
        return self.model.get_all(order)

    def buscar_estado_libro(self, data_estado_libro):
        return self.model.get_by_column(data_estado_libro)

    def modificar_estado_libro(self, id_estado_libro, data_estado_libro):
        return self.model.update(id_estado_libro, data_estado_libro)

    def eliminar_estado_libro(self, id_estado_libro):
        return self.model.delete(id_estado_libro)


