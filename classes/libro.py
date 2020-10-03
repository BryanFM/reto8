from connection.conn import Conexion

class Libro:
    def __init__(self):
        self.model = Conexion('libro')

    def guardar_libro(self, libro):
        return self.model.insert(libro)

    def obtener_libro(self, id_libro):
        return self.model.get_by_id(id_libro)

    def obtener_libros(self,  order):
        fields_select = {
            'libro' : {
                '1' : 'id',
                '2' : 'nombres'
            },
            'editorial' : {
                '1' : 'nombres'
            },
            'genero' : {
                '1' : 'descripcion'
            },
            'estado_libro' : {
                '1' : 'descripcion'
            }

        }
        table_select = {

            'libro' : {
                'editorial' : {
                    'ideditorial' : 'id'
                },
                'genero' : {
                    'idgenero' : 'id'
                },
                'estado_libro' : {
                    'idestlibro' : 'id'
                }
            }
        }
        return self.model.get_all_inner(fields_select, table_select, order)

    def buscar_libro(self, data_libro):
        return self.model.get_by_column(data_libro)

    def modificar_libro(self, id_libro, data_libro):
        return self.model.update(id_libro, data_libro)

    def eliminar_libro(self, id_libro):
        return self.model.delete(id_libro)