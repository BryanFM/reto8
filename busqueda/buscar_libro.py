from helpers.menu import Menu
from helpers.helper import input_data, print_table, pregunta
from controllers.genero_controller import genero_controller
from controllers.editorial_controller import Editorial_controller


def buscar_libro():
    try:
        print('''
        ======================
            Buscar Libro
        ======================
        ''')
        menu_principal = ['libros', 'autores', 'generos', 'editorial', 'salir' ]
        respuesta = Menu(menu_principal).show()
        if respuesta == 1:
            pass
        elif respuesta == 2:
            pass
        elif respuesta == 3:
            genero = genero_controller()
            genero.listar_generos()
            genero.buscar_genero()
            if genero.salir:
                buscar_libro()
        elif respuesta == 4:
            editorial = Editorial_controller()
            editorial.listar_editoriales()
            editorial.buscar_editorial()
            if editorial.salir:
                buscar_libro()

        print("\nGracias por utilizar la biblioteca\n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')