from classes.autor import Autor
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu


class Autor_controller:
    def __init__(self):
        self.autor = Autor()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                =============
                    Autor
                =============
                ''')
                menu = ['Listar autor', 'Buscar autor', "Nuevo autor", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_autores()
                elif respuesta == 2:
                    self.buscar_autor()
                elif respuesta == 3:
                    self.insertar_autor()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_autores(self):
        print('''
        =========================
            Lista de autores
        =========================
        ''')
        autores = self.autor.obtener_autores('id')
        print(print_table(autores, ['ID', 'Nombres', 'Apellidos', 'Fecha de nacimiento']))
        input("\nPresione una tecla para continuar...")

    def buscar_autor(self):
        print('''
        ====================
            Buscar autor
        ====================
        ''')
        try:
            id_autor = input_data("Ingrese el ID del autor >> ", "int")
            autor = self.autor.obtener_autor({'id': id_autor})
            print(print_table(autor, ['ID', 'Nombres', 'Apellidos', 'Fecha de nacimiento']))

            if autor:
                if pregunta("¿Deseas dar mantenimiento al autor?"):
                    opciones = ['Editar autor', 'Eliminar autor', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_autor(id_autor)
                    elif respuesta == 2:
                        self.eliminar_autor(id_autor)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_autor(self):
        nombres = input_data("Ingrese el nombres del autor >> ")
        apellidos = input_data("Ingrese Apellidos del autor >> ")
        fecha_nacimiento = input_data("Ingrese Fecha de nacimiento del autor >> ")
        self.autor.guardar_autor({
            'nombres': nombres,
            'apellidos': Apellidos,
            'fecha_nacimiento': fecha_nacimiento
        })
        print('''
        ==============================
            Nuevo autor agregado !
        ==============================
        ''')
        self.listar_autores()

    def editar_autor(self, id_autor):
        nombres = input_data("Ingrese nuevos nombres del autor >> ")
        apellidos = input_data("Ingrese nuevos apellidos del autor >> ")
        fecha_nacimiento = input_data("Ingrese fecha de nacimiento del autor >> ")
        
        self.autor.modificar_autor({
            'id': id_autor
        }, {
            'nombres': nombres,
            'apellidos': apelldidos
            'fecha_nacimiento': fecha_nacimiento
        })
        print('''
        =======================
            autor editado !
        =======================
        ''')

    def eliminar_autor(self, id_autor):
        self.autor.eliminar_autor({
            'id': id_autor
        })
        print('''
        =========================
            autor Eliminado !
        =========================
        ''')