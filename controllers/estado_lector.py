from classes.estado_lector import Estado_lector
from helpers.menu import Menu
from helpers.helper import print_table, input_data, pregunta

class estado_lector_controller:
    def __init__(self):
        self.estado_lector = Estado_lector()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ==========================
                    Estado de Usuario
                ==========================
                ''')
                menu = ['Listar estado de usuario', 'Buscar estado de usuario', "Nuevo estado de usuario", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_estado()
                elif respuesta == 2:
                    self.buscar_estado()
                elif respuesta == 3:
                    self.insertar_estado()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_estado(self):
        print('''
        ====================================
            Lista de Estados del Usuario
        ====================================
        ''')
        estado_lector = self.editorial.obtener_estados_lector('id')
        print(print_table(editoriales, ['ID', 'Descripcion']))
        input("\nPresione una tecla para continuar...")

    def buscar_estado(self):
        print('''
        =================================
            Buscar Estado de Usuario
        =================================
        ''')
        try:
            estado_lector_id = input_data("Ingrese el ID del Estado de Usuario >> ", "int")
            estado_lector = self.estado_lector.obtener_estado_lector({'id': estado_lector_id})
            print(print_table(estado_lector, ['ID', 'Descripcion']))

            if editorial:
                if pregunta("¿Deseas dar mantenimiento al estado del Usuario?"):
                    opciones = ['Editar Estado de Usuario', 'Eliminar Estado de Usuario', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_estado(estado_lector_id)
                    elif respuesta == 2:
                        self.eliminar_estado(estado_lector_id)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_estado(self):
        descripcion = input_data("Ingrese el Estado del Usuario >> ")
        self.estado_lector.guardar_estado_lector({
            'descripcion': descripcion
        })
        print('''
        ==========================================
            Nuevo Estado de Usuario Agregado !
        ==========================================
        ''')
        self.listar_estado()

    def editar_estado(self, estado_lector_id):
        descripcion = input_data("Ingrese el nuevo estado del Usuario >> ")
        self.estado_lector.modificar_estado_lector({
            'id_estado lector': estado_lector_id
        }, {
            'descripcion': descripcion
        })
        print('''
        ====================================
            Estado de Usuario Editado !
        ====================================
        ''')

    def eliminar_estado(self, estado_lector_id):
        self.estado_lector.eliminar_estado_lector({
            'id': estado_lector_id
        })
        print('''
        ====================================
            Estado de Usuario Eliminado !
        ====================================
        ''')