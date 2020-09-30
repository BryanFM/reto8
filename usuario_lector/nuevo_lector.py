from helpers.menu import Menu
from helpers.helper import input_data, print_table, pregunta
from controllers.lector_controller import lector_controller
from classes.lector import Lector
from usuario_lector.iniciar_lector import iniciar_sesion

def nuevo_usuario():
    print('''
    ==================================
        Registro de Nuevo Usuario
    ==================================
    ''')
    lect = lector_controller()
    lect.insertar_lector()
    iniciar_sesion()
    
    