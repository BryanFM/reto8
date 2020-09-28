from classes.genero import Genero
from helpers.menu import Menu
from helpers.helper import print_table, input_data, pregunta

class genero_controller:
    def __init__(self):
        self.genero = Genero()
        self.salir = False
    def menu(self):
        while True:
            try:
                print('''
                ==========================
                    Generos Literarios
                ==========================
                ''')
                menu = ['Listar Generos', 'Buscar Generos', "Nuevo Genero", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_generos()
                elif respuesta == 2:
                    self.buscar_generos()
                elif respuesta == 3:
                    self.agregar_genero()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_generos(self):
        print('''
        ===================================
            Lista de Generos Literarios
        ===================================
        ''')
        generos = self.genero.obtener_generos('genero_id')
        print(print_table(cursos, ['ID', 'genero']))
        input("\nPresione una tecla para continuar...")

    def buscar_genero(self):
        print('''
        ==================================
            Buscar Generos Literarios
        ==================================
        ''')
        try:
            id_genero = input_data("Ingrese el ID del genero >> ", "int")
            genero = self.genero.obtener_genero({'curso_id': id_curso})
            print(print_table(curso, ['ID', 'Nombre']))

            if genero:
                if pregunta("¿Deseas editar el genero literario?"):
                    opciones = ['Editar genero literario', 'Eliminar genero literario', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_genero(id_genero)
                    elif respuesta == 2:
                        self.eliminar_genero(id_genero)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def agregar_genero(self):
        nombre = input_data("Ingrese el nombre del genero literario >> ")
        self.genero.guardar_genero({
            'nombre': nombre
        })
        print('''
        ==========================================
            Nuevo Genero Literario agregado !
        ==========================================
        ''')
        self.listar_generos()

    def editar_genero(self, id_genero):
        nombre = input_data("Ingrese el nuevo nombre del Genero Literario >> ")
        self.genero.modificar_genero({
            'genero_id': id_genero
        }, {
            'nombre': nombre
        })
        print('''
        ==================================
            Genero Literario Editado !
        ==================================
        ''')

    def eliminar_genero(self, id_genero):
        self.genero.eliminar_genero({
            'genero_id': id_genero
        })
        print('''
        ====================================
            Genero Literario Eliminado !
        ====================================
        ''')

