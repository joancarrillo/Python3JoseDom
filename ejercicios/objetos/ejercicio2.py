from ejercicio1 import Persona
class Cuenta():

    def __init__(self,titular,cantidad=0):
        self.titular=titular
        self.cantidad=cantidad
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self,titular):
        self.__titular=titular

    @cantidad.setter
    def cantidad(self,cantidad):
        if cantidad<0:
            self.__cantidad=0
        else:    
            self.__cantidad=cantidad
    
    def mostrar(self):
        return "Cuenta\n"+"Titular:"+self.__titular.mostrar()+" - Cantidad:"+str(self.cantidad)
    
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.cantidad = self.cantidad + cantidad
    
    def retirar(self,cantidad):
        if cantidad > 0:
            self.cantidad = self.cantidad - cantidad
    