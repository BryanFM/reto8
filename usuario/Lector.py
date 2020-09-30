from helpers.menu import Menu
from helpers.helper import input_data, print_table, pregunta
from usuario_lector.nuevo_lector import nuevo_usuario
from usuario_lector.iniciar_lector import iniciar_sesion

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
            nuevo_usuario()
        elif respuesta == 2:
            iniciar_sesion()

        print("\nGracias por utilizar la biblioteca\n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')
