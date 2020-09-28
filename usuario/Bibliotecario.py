from helpers.menu import Menu
from helpers.helper import input_data, print_table, pregunta


def Bibliotecario():
    try:
        print('''
        =================================================
            Sistema de Mantenimiento de la Biblioteca
        =================================================
        ''')
        menu_principal = ['libros', 'autores', 'generos', 'editorial', ]
        respuesta = Menu(menu_principal).show()
        if respuesta == 1:
            pass
        elif respuesta == 2:
            pass
        elif respuesta == 3:
            pass
        elif respuesta == 4:
            pass
        elif respuesta == 5:
            pass
        elif respuesta == 6:
            pass
        elif respuesta == 7:
            pass

        print("\nGracias por utilizar el sistema\n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')