from classes.editorial import Editorial
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu


class Editorial_controller:
    def __init__(self):
        self.editorial = Editorial()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                =================
                    Editorial
                =================
                ''')
                menu = ['Listar editorial', 'Buscar editorial', "Nuevo editorial", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_editoriales()
                elif respuesta == 2:
                    self.buscar_editorial()
                elif respuesta == 3:
                    self.insertar_editorial()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_editoriales(self):
        print('''
        ============================
            Lista de editoriales
        ============================
        ''')
        editoriales = self.editorial.obtener_editoriales('id')
        print(print_table(editoriales, ['ID', 'Nombres', 'Dirección']))
        input("\nPresione una tecla para continuar...")

    def buscar_editorial(self):
        print('''
        ========================
            Buscar editorial
        ========================
        ''')
        try:
            id_editorial = input_data("Ingrese el ID del editorial >> ", "int")
            editorial = self.editorial.obtener_editorial({'id': id_editorial})
            print(print_table(editorial, ['ID', 'Nombre', 'Descripción']))

            if editorial:
                if pregunta("¿Deseas dar mantenimiento al editorial?"):
                    opciones = ['Editar editorial', 'Eliminar editorial', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_editorial(id_editorial)
                    elif respuesta == 2:
                        self.eliminar_editorial(id_editorial)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_editorial(self):
        nombre = input_data("Ingrese el nombre del editorial >> ")
        direccion = input_data("Ingrese dirección del editorial >> ")
        self.editorial.guardar_editorial({
            'nombres': nombre,
            'direccion': direccion
        })
        print('''
        ==================================
            Nuevo editorial agregado !
        ==================================
        ''')
        self.listar_editoriales()

    def editar_editorial(self, id_editorial):
        nombre = input_data("Ingrese el nuevo nombre del editorial >> ")
        direccion = input_data("Ingrese la nueva dirección del editorial >> ")
        self.editorial.modificar_editorial({
            'editorial_id': id_editorial
        }, {
            'nombres': nombre,
            'direccion': direccion
        })
        print('''
        ===========================
            editorial Editado !
        ===========================
        ''')

    def eliminar_editorial(self, id_editorial):
        self.editorial.eliminar_editorial({
            'id': id_editorial
        })
        print('''
        =============================
            editorial Eliminado !
        =============================
        ''')