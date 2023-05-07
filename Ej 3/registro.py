class Registro:
    __temp = ""
    __humedad= ""
    __presion=""
    def __init__(self, temp="", hum="", pres=""):
        self.__temp=temp
        self.__humedad=hum
        self.__presion=pres
    def retornatemp(self):
        return self.__temp
    def retornahum(self):
        return self.__humedad
    def retornapres(self):
        return self.__presion
        

