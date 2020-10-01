from connection.conn import Conexion

class Autor:
    def __init__(self):
        self.model = Conexion('autor')

    def guardar_autor(self, autor):
        return self.model.insert(autor)

    def obtener_autor(self, id_autor):
        return self.model.get_by_id(id_autor)

    def obtener_autores(self, order):
        return self.model.get_all(order)

    def buscar_autor(self, data_autor):
        return self.model.get_by_column(data_autor)

    def modificar_autor(self, id_autor, data_autor):
        return self.model.update(id_autor, data_autor)

    def eliminar_autor(self, id_autor):
        return self.model.delete(id_autor)


