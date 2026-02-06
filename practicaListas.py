class Nodo:
    def __init__(self, documento, nombre):
        self.documento=documento
        self.nombre=nombre
        self.siguiente=None
class lista:
    def __init__(self):  
        self.cabeza=None  
        
    def agregaralFinal(self, nombre, documento):
        nuevo=Nodo(nombre,documento)
        #verificar si esta vacio
        if self.cabeza is None:
            self.cabeza=nuevo
            self.cola=nuevo
        else:
            self.cola.siguiente=nuevo
            self.cola=nuevo
            

           
 

        


    