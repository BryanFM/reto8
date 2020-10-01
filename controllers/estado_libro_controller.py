from classes.estado_libro import Estado_libro
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu


class Estado_libro_controller:
    def __init__(self):
        self.estado_libro = Estado_libro()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ====================
                    estado libro
                ====================
                ''')
                menu = ['Listar estados de libro', 'Buscar estado de libro', "Nuevo estado de libro", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_estados_libro()
                elif respuesta == 2:
                    self.buscar_estado_libro()
                elif respuesta == 3:
                    self.insertar_estado_libro()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_estado_libroes(self):
        print('''
        =================================
            Lista de estados de libro
        =================================
        ''')
        estado_libro = self.estado_libro.obtener_estados_libro('id')
        print(print_table(estado_libro, ['ID', 'Descripción']))
        input("\nPresione una tecla para continuar...")

    def buscar_estado_libro(self):
        print('''
        ===========================
            Buscar estado libro
        ===========================
        ''')
        try:
            id_estado_libro = input_data("Ingrese el ID del estado de libro >> ", "int")
            estado_libro = self.estado_libro.obtener_estado_libro({'id': id_estado_libro})
            print(print_table(estado_libro, ['ID', 'Descripción']))

            if estado_libro:
                if pregunta("¿Deseas dar mantenimiento a estado de libro?"):
                    opciones = ['Editar estado de libro', 'Eliminar estado de libro', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_estado_libro(id_estado_libro)
                    elif respuesta == 2:
                        self.eliminar_estado_libro(id_estado_libro)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_estado_libro(self):
        descripcion = input_data("Ingrese descripción del estado de libro >> ")
        self.estado_libro.guardar_estado_libro({
            'descripcion': descripcion
        })
        print('''
        ========================================
            Nuevo estado de libro agregado !
        ========================================
        ''')
        self.listar_estados_libro()

    def editar_estado_libro(self, id_estado_libro):
        descripcion = input_data("Ingrese el nuevo nombre del estado de libro >> ")
        self.estado_libro.modificar_estado_libro({
            'id': id_estado_libro
        }, {
            'descripcion': descripcion
        })
        print('''
        =================================
            Estado de libro editado !
        =================================
        ''')

    def eliminar_estado_libro(self, id_estado_libro):
        self.estado_libro.eliminar_estado_libro({
            'id': id_estado_libro
        })
        print('''
        =============================
            Estado de libro eliminado !
        =============================
        ''')