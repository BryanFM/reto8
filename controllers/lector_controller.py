from classes.lector import Lector
from helpers.menu import Menu
from helpers.helper import print_table, input_data, pregunta

class lector_controller:
    def __init__(self):
        self.lector = Lector()
        self.salir = False
    def menu(self):
        while True:
            try:
                print('''
                ===================
                    Usuarios
                ===================
                ''')
                menu = ['Listar Usuarios', 'Buscar Usuarios', "Nuevo Usuario", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_lectores()
                elif respuesta == 2:
                    self.buscar_lector()
                elif respuesta == 3:
                    self.insertar_lector()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')
    
    def listar_lectores(self):
        print('''
        ===========================
            Lista de Usuarios
        ===========================
        ''')
        lectores = self.lector.obtener_lectores('lector_id')
        print(print_table(lectores, ['lector_id', 'dni', 'nombres', 'apellidos', 'fecha_nacimiento', 'estado_lector_id']))
        input("\nPresione una tecla para continuar...")
    def buscar_lector(self):
        print('''
        ===========================
            Buscar Usuario
        ===========================
        ''')
        try:
            lector_id = input_data("Ingrese el ID del Usuario >> ", "int")
            lector = self.lector.obtener_lector({'id_lector': lector_id})
            print(print_table(lector, ['lector_id', 'dni', 'nombres', 'apellidos', 'fecha_nacimiento', 'estado_lector_id']))

            if lector:
                if pregunta("¿Deseas dar mantenimiento a la lista de Usuarios?"):
                    opciones = ['Editar Usuario', 'Eliminar Usuario', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_lector(lector_id)
                    elif respuesta == 2:
                        self.eliminar_lector(lector_id)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")
    def insertar_lector(self):
        dni = input_data("Imgrese el DNI del Usuario >> ")
        nombres = input_data("Ingrese el nombre del Usuario >> ")
        apellidos = input_data("Ingrese el apellido del Usuario >> ")
        fecha_nacimiento = input_data("Ingrese la fecha de nacimiento del Usuario >> ")
        self.lector.guardar_lector({
            'dni' : dni,
            'nombres': nombres,
            'apellidos' : apellidos,
            'fecha_nacimiento': fecha_nacimiento
        })
        print('''
        =================================
            Nuevo Usuario agregado !
        =================================
        ''')
        self.listar_lectores()

    def editar_lector(self, lector_id):
        dni = input_data("Imgrese el nuevo DNI del Usuario >> ")
        nombres = input_data("Ingrese el nuevo nombre del Usuario >> ")
        apellidos = input_data("Ingrese el nuevo apellido del Usuario >> ")
        fecha_nacimiento = input_data("Ingrese la nueva fecha de nacimiento del Usuario >> ")
        self.lector.modificar_lector({
            'id_lector': lector_id
        }, {
            'dni' : dni,
            'nombres': nombres,
            'apellidos' : apellidos,
            'fecha_nacimiento': fecha_nacimiento
        })
        print('''
        ===================================
            Datos del Usuario Editado !
        ===================================
        ''')
    def eliminar_lector(self, lector_id):
        self.lector.eliminar_lector({
            'id_lector': lector_id
        })
        print('''
        ========================
            Usuario Eliminado !
        ========================
        ''')