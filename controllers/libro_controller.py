from classes.libro import Libro
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu


class Libro_controller:
    def __init__(self):
        self.libro = Libro()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                =============
                    Libro
                =============
                ''')
                menu = ['Listar libro', 'Buscar libro', "Nuevo libro", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_libros()
                elif respuesta == 2:
                    self.buscar_libro()
                elif respuesta == 3:
                    self.insertar_libro()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_libros(self):
        print('''
        ========================
            Lista de libros
        ========================
        ''')
        libros = self.libro.obtener_libros('id')
        print(print_table(libros, ['ID', 'Nombres', 'Editorial', 'Género', 'Estado']))
        input("\nPresione una tecla para continuar...")

    def buscar_libro(self):
        print('''
        ====================
            Buscar libro
        ====================
        ''')
        try:
            id_libro = input_data("Ingrese el ID del libro >> ", "int")
            libro = self.libro.obtener_libro({'id': id_libro})
            print(print_table(libro, ['ID', 'Nombres', 'Apellidos', 'Fecha de nacimiento']))

            if libro:
                if pregunta("¿Deseas dar mantenimiento al libro?"):
                    opciones = ['Editar libro', 'Eliminar libro', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_libro(id_libro)
                    elif respuesta == 2:
                        self.eliminar_libro(id_libro)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_libro(self):
        nombres = input_data("Ingrese el nombres del libro >> ")
        apellidos = input_data("Ingrese Apellidos del libro >> ")
        fecha_nacimiento = input_data("Ingrese Fecha de nacimiento del libro >> ")
        self.libro.guardar_libro({
            'nombres': nombres,
            'apellidos': Apellidos,
            'fecha_nacimiento': fecha_nacimiento
        })
        print('''
        ==============================
            Nuevo libro agregado !
        ==============================
        ''')
        self.listar_libroes()

    def editar_libro(self, id_libro):
        nombres = input_data("Ingrese nuevos nombres del libro >> ")
        apellidos = input_data("Ingrese nuevos apellidos del libro >> ")
        fecha_nacimiento = input_data("Ingrese fecha de nacimiento del libro >> ")
        
        self.libro.modificar_libro({
            'id': id_libro
        }, {
            'nombres': nombres,
            'apellidos': apelldidos,
            'fecha_nacimiento': fecha_nacimiento
        })
        print('''
        =======================
            libro editado !
        =======================
        ''')

    def eliminar_libro(self, id_libro):
        self.libro.eliminar_libro({
            'id': id_libro
        })
        print('''
        =========================
            libro Eliminado !
        =========================
        ''')