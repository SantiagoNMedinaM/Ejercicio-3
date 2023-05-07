from registro import Registro
from ManejadorRegistro import manejador
from menuopciones import Menu
if __name__ == '__main__':
    lista=manejador()
    lista.cargararch()
    a=Menu()
    a.opciones(lista)