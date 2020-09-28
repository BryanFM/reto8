from classes.lector import lector
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
        print(print_table(lector, ['ID', 'Nombre', 'Edad', 'Correo']))
        input("\nPresione una tecla para continuar...")
    def buscar_lector(self):
        print('''
        ===========================
            Buscar Usuario
        ===========================
        ''')
        try:
            id_lector = input_data("Ingrese el ID del Usuario >> ", "int")
            lector = self.lector.obtener_lector({'lector_id': id_lector})
            print(print_table(alumno, ['ID', 'Nombre', 'Edad', 'Correo']))

            if alumno:
                if pregunta("¿Deseas dar mantenimiento a la lista de Usuarios?"):
                    opciones = ['Editar Usuario', 'Eliminar Usuario', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_lector(id_lector)
                    elif respuesta == 2:
                        self.eliminar_lector(id_lector)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")
    def insertar_lector(self):
        nombre = input_data("Ingrese el nombre del Usuario >> ")
        edad = input_data("Ingrese la edad del Usuario >> ")
        correo = input_data("Ingrese el correo del Usuario >> ")
        self.lector.guardar_lector({
            'nombres': nombre,
            'edad': edad,
            'correo': correo
        })
        print('''
        =================================
            Nuevo Usuario agregado !
        =================================
        ''')
        self.listar_lectores()

    def editar_lector(self, id_lector):
        nombre = input_data("Ingrese el nuevo nombre del Usuario >> ")
        edad = input_data("Ingrese la nueva edad del Usuario >> ")
        correo = input_data("Ingrese el nuevo correo del Usuario >> ")
        self.lector.modificar_lector({
            'alumno_id': id_alumno
        }, {
            'nombres': nombre,
            'edad': edad,
            'correo': correo
        })
        print('''
        ===================================
            Datos del Usuario Editado !
        ===================================
        ''')
    def eliminar_lector(self, id_lector):
        self.lector.eliminar_lector({
            'lector_id': id_lector
        })
        print('''
        ========================
            Usuario Eliminado !
        ========================
        ''')