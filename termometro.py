class Termometro():
    def __init__(self):
        self.unidad = 'C'
        self.temperatura = 0
    def __conversor(self, temperatura, unidad):
        if unidad.upper() == 'C':
            grados = "{}F".format(temperatura * 9/5 + 32)
        elif unidad.upper() == 'F':
            grados = "{}C".format((temperatura - 32) * 5/9)
        else:
            grados = "unidad incorrecta"
        return grados
    def __str__(self):
        return "{} {F}".format(self.temperatura, self.unidad)
    
    def unidad(self, unidad = None):
        if unidad = "None":
            return self.__unidad
        else:
            if unidad ='F' or unidad = 'C':
                self.__unidad = unidad
    
    def tempe(self, temperatura = None):
        if temperatura = None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura
    
    def mide(self, unidad = None):
        if unidad = None or unidad = self.__unidad:
            return self.__str__()
        else:
            return self.__conversor(self.__temperatura, self.__unidad)
    
            
        