from helpers.menu import Menu
from helpers.helper import input_data, print_table, pregunta
from classes.lector import Lector
from controllers.lector_controller import lector_controller
from busqueda.buscar_libro import buscar_libro

def iniciar_sesion():
    print('''
    ========================
        Iniciar Sesion
    ========================
    ''')
    try:
        lector_id = input_data("Ingrese la contraseña del Usuario >> ", "int")
        lector = self.lector.obtener_lector({'id_lector': lector_id})
        print(print_table(lector, ['lector_id', 'dni', 'nombres', 'apellidos','fecha_nacimiento']))
        if lector:
            if pregunta("¿Que Desea Realizar?"):
                opciones = ['Buscar Libro', 'Editar Usuario', 'Eliminar Usuario', 'Salir']
                respuesta = Menu(opciones).show()
                if respuesta == 1:
                    buscar_libro()
                elif respuesta == 2:
                    lect = lector_controller()
                    lect.editar_lector()
                elif respuesta == 3:
                    lect = lector_controller()
                    lect.eliminar_lector()
    except Exception as e:
        print(f'{str(e)}')
    input("\nPresione una tecla para continuar...")

