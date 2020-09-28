from helpers.menu import Menu
from helpers.helper import input_data, print_table, pregunta


def Lector():
    try:
        print('''
        =============================================
            Bienvenido a la Biblioteca Municipal
        =============================================
        ''')
        menu_principal = ['Nuevo Usuario', 'Iniciar', 'Salir']
        respuesta = Menu(menu_principal).show()
        if respuesta == 1:
            pass
        elif respuesta == 2:
            pass
        elif respuesta == 3:
            pass

        print("\nGracias por utilizar el sistema\n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')