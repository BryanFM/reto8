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
        print(print_table(generos, ['genero_id', 'genero']))
        input("\nPresione una tecla para continuar...")

    def buscar_genero(self):
        print('''
        ==================================
            Buscar Generos Literarios
        ==================================
        ''')
        try:
            genero_id = input_data("Ingrese el ID del genero >> ", "int")
            genero = self.genero.obtener_genero({'id_genero': genero_id})
            print(print_table(genero, ['genero_id', 'descripcion']))

            if genero:
                if pregunta("¿Deseas editar el genero literario?"):
                    opciones = ['Editar genero literario', 'Eliminar genero literario', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_genero(genero_id)
                    elif respuesta == 2:
                        self.eliminar_genero(genero_id)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def agregar_genero(self):
        nombre = input_data("Ingrese el nombre del genero literario >> ")
        self.genero.guardar_genero({
            'descripcion': descripcion
        })
        print('''
        ==========================================
            Nuevo Genero Literario agregado !
        ==========================================
        ''')
        self.listar_generos()

    def editar_genero(self, genero_id):
        nombre = input_data("Ingrese el nuevo nombre del Genero Literario >> ")
        self.genero.modificar_genero({
            'id_genero': genero_id
        }, {
            'descripcion': descripcion
        })
        print('''
        ==================================
            Genero Literario Editado !
        ==================================
        ''')

    def eliminar_genero(self, genero_id):
        self.genero.eliminar_genero({
            'genero_id': genero_id
        })
        print('''
        ====================================
            Genero Literario Eliminado !
        ====================================
        ''')

