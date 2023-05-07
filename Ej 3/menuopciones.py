from ManejadorRegistro import manejador
from registro import Registro
class Menu:
    def __init__(self):
        self.__opcion=None
    def opciones(self,lista):
        while True:
            print("1: Mostrar para cada variable el día y hora de menor y mayor valor. \n 2: Indicar la temperatura promedio mensual por cada hora. \n 3: Dado un número de día listar los valores de las tres variables para cada hora del día dado. \n 4: Salir.")    
            self.__opcion=int(input("Seleccione una opcion: "))
            if self.__opcion == 1:
                tipo=str(input("Ingrese una variable. Temperatura, Humedad, Presion: "))
                if tipo =="Temperatura":
                    lista.menortemp()
                    lista.mayortemp()
                elif tipo=="Humedad":
                    lista.menorhum()
                    lista.mayorhum()
                elif tipo=="Presion":
                    lista.menorpres()
                    lista.mayorpres()
                else:
                    print("Error: La variable ingresada no es valida.")
            elif self.__opcion == 2:
                lista.prom()
            elif self.__opcion == 3:
                lista.listar()
            elif self.__opcion == 4: 
                break
            else:
                print("La opcion ingresada es invalida, ingrese otra opcion")

