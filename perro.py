class Dog():
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None
    def ladrar(self):
        if self.peso = None:
            print("soy un fantasma")
        if self.peso >= 8:
            print ('GUAU, GUAU')
        else:
            print('ay, ay')
            
    

class Perro():
    def __init__(self, n, e, p):
        self.nombre = n
        self.edad = e
        self.peso = p
    def ladrar(self):
        if self.peso >= 8:
            print ('GUAU, GUAU')
        else:
            print('guau, guau')
    def __str__(self):
        return "Perro {}, e: {}, p: {}".format(self.nombre, self.edad, self.peso)
    
class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, perso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.trabajando = False
    
    def __str__(self):
        return "Perro de asistencia de {}".format(self.amo)

    def pasear(self):
        print("{} ayudo a mi duelo, {} a pasear".format(self.nombre, self.amo))
    
    def ladrar(self):
        if self.__trabajando:
            print("shhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
    
    def trabajando(self, valor = None):
        if valor = None:
            return self.__trabajando
        else:
            self.__trabajando = valor
        