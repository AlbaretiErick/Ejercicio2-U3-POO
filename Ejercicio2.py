from Clases import ManejaSabores
from Clases import ManejaHelados
from Clases import Menu
if __name__ == '__main__':
    manejaSabores = ManejaSabores()
    manejaHelados = ManejaHelados()
    menu = Menu()
    manejaSabores.testSabores()
    bul = False
    while bul==False:
        opcion = input ('Seleccione:\n1 - Cargar una venta.\n2 - Mostrar los 5 sabores mas pedidos.\n3 - Mostrar el total de gramos vendidos para un sabor especifico.\n4 - Mostrar los sabores vendidos para un tipo de helado especifico.\n5 - Mostrar total recaudado por cada tipo de helado.\nIngresar cualquier otro valor para salir del programa\nOpcion: ')
        bul = menu.opcion (opcion, manejaHelados, manejaSabores)
        print ('\n')