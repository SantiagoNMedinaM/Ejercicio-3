import csv
from registro import Registro
class manejador:
    def __init__(self):
        self.__listabi=[[Registro(None,None,None) for __ in range(24)]for __ in range (3)]
    def cargararch(self):
        archivo=open("metereologicas.csv")
        reader= csv.reader(archivo, delimiter=";")
        for fila in reader:
            dia= int(fila[0])
            hora = int(fila[1])
            temp = float(fila[2])
            hum = float(fila[3])
            pres = float(fila[4])
            obj = Registro(temp, hum, pres)
            self.__listabi[dia-1][hora] = obj
        archivo.close

    def menortemp(self):
        min= 1000000
        dia=0
        hora=0
        for i in range(3):
            for j in range(24):
                if self.__listabi[i][j].retornatemp() < min:
                    min=self.__listabi[i][j].retornatemp()
                    dia= i + 1
                    hora= j
        print("La menor temperatura del mes se registro el dia {} en la hora {} y es de {}°".format(dia, hora, min))

    def mayortemp(self):
        max=-1000000
        dia=0
        hora=0
        for i in range(3):
            for j in range(24):
                if self.__listabi[i][j].retornatemp() > max:
                    min=self.__listabi[i][j].retornatemp()
                    dia= i + 1
                    hora= j
        print("La mayor temperatura del mes se registro el dia {} en la hora {} y es de {}°".format(dia, hora, min))

    def menorhum(self):
        min=1000000
        dia=0
        hora=0
        for i in range(3):
            for j in range(24):
                if self.__listabi[i][j].retornahum() < min:
                    min=self.__listabi[i][j].retornahum()
                    dia= i + 1
                    hora= j
        print("La menor humedad del mes se registro el dia {} en la hora {} y es de {}°".format(dia, hora, min))

    def mayorhum(self):
        max=-1000000
        dia=0
        hora=0
        for i in range(3):
            for j in range(24):
                if self.__listabi[i][j].retornahum() > max:
                    min=self.__listabi[i][j].retornahum()
                    dia= i + 1
                    hora= j
        print("La mayor humedad del mes se registro el dia {} en la hora {} y es de {}°".format(dia, hora, min))

    def menorpres(self):
        min=1000000
        dia=0
        hora=0
        for i in range(3):
            for j in range(24):
                if self.__listabi[i][j].retornapres() < min:
                    min=self.__listabi[i][j].retornapres()
                    dia= i + 1
                    hora= j
        print("La menor presion del mes se registro el dia {} en la hora {} y es de {}°".format(dia, hora, min))

    def mayorpres(self):
        max=-1000000
        dia=0
        hora=0
        for i in range(3):
            for j in range(24):
                if self.__listabi[i][j].retornapres() > max:
                    min=self.__listabi[i][j].retornapres()
                    dia= i + 1
                    hora= j
        print("La mayor pres del mes se registro el dia {} en la hora {} y es de {}°".format(dia, hora, min))
    
    def prom(self):
        for j in range(24):
            ac=0
            for i in range(3):
                ac += self.__listabi[i][j].retornatemp()
            print("La temperatura mensual promedio de la hora {} es de {:.2f}".format(j,ac/3))
        
    def listar(self):
        d=int(input("Ingrese el dia del mes del que desea ver las variables metereologicas por hora "))
        print("Dia: {}".format(d))
        print("Hora\tTemperatura\tHumedad\t\tPresion")
        for j in range(24):
            print("{}\t{}\t\t{}\t\t{}".format(j,self.__listabi[d-1][j].retornatemp(), self.__listabi[d-1][j].retornahum(), self.__listabi[d-1][j].retornapres()))


