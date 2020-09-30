from helpers.menu import Menu
from helpers.helper import input_data, print_table, pregunta
from classes.lector import Lector
from controllers.lector_controller import lector_controller
#from main import iniciar_app

def iniciar_sesion():
    print('''
    ========================
        Iniciar Sesion
    ========================
    ''')
    try:
        id_lector = input_data("Ingrese la contraseña del Usuario >> ", "int")
        lector = self.lector.obtener_lector({'lector_id': id_lector})
        print(print_table(lector, ['ID', 'Nombre', 'Edad', 'DNI','Correo']))
        if lector:
            if pregunta("¿ Que Desea Realizar?"):
                opciones = ['Buscar Libro', 'Editar Usuario', 'Eliminar Usuario', 'Salir']
                respuesta = Menu(opciones).show()
                if respuesta == 1:
                    pass
                elif respuesta == 2:
                    lect = lector_controller()
                    lect.editar_lector()
                elif respuesta == 3:
                    lect = lector_controller()
                    lect.eliminar_lector()
    except Exception as e:
        print(f'{str(e)}')
    input("\nPresione una tecla para continuar...")

