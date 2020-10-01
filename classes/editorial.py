from connection.conn import Conexion

class Editorial:
    def __init__(self):
        self.model = Conexion('Editorial')

    def guardar_editorial(self, editorial):
        return self.model.insert(editorial)

    def obtener_editorial(self, id_editorial):
        return self.model.get_by_id(id_editorial)

    def obtener_editoriales(self, order):
        return self.model.get_all(order)

    def buscar_editorial(self, data_editorial):
        return self.model.get_by_column(data_editorial)

    def modificar_editorial(self, id_editorial, data_editorial):
        return self.model.update(id_editorial, data_editorial)

    def eliminar_editorial(self, id_editorial):
        return self.model.delete(id_editorial)


