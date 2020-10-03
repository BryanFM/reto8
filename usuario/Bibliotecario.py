from helpers.menu import Menu
from helpers.helper import input_data, print_table, pregunta
from controllers.genero_controller import genero_controller
from controllers.lector_controller import lector_controller
from controllers.libro_controller import Libro_controller

def Bibliotecario():
    try:
        print('''
        =================================================
            Sistema de Mantenimiento de la Biblioteca
        =================================================
        ''')
        menu_principal = ['libros', 'autores', 'generos', 'editorial', 'usuarios', 'alquiler', 'estado de libro', 'estado de usuario', 'estado de alquiler', 'salir' ]
        respuesta = Menu(menu_principal).show()
        if respuesta == 1:
            libros = Libro_controller()
            libros.menu()
            if libros.salir:
                iniciar_app()
        elif respuesta == 2:
            pass
        elif respuesta == 3:
            genero = genero_controller()
            genero()
            if genero.salir:
                Bibliotecario()
        elif respuesta == 4:
            pass
        elif respuesta == 5:
            pass
        elif respuesta == 6:
            pass
        elif respuesta == 7:
            pass
        elif respuesta == 8:
            pass
        elif respuesta == 9:
            pass

        print("\nGracias por utilizar la biblioteca\n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')