from usuario.Bibliotecario import Bibliotecario
from usuario.Lector import Lector
from helpers.menu import Menu
from helpers.helper import input_data, print_table, pregunta

def iniciar_app():
    try:
        if pregunta('¿Desea ingresar a la biblioteca municipal?'):
            opciones = ['Bibliotecario', 'Lector']
            respuesta = Menu(opciones).show()
            if respuesta == 1:
                Bibliotecario()
            elif respuesta == 2:
                Lector()
    except Exception as e:
            print(f'{str(e)}')

iniciar_app()
                