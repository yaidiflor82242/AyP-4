# Implementación de una lista doblemente enlazada en Python
class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente =None
        self.anterior=None

class ListaDoble:
    def __init__(self): 
        self.cabeza=None
        self.cola=None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_inicio(self, dato):
            nuevo=NodoDoble(dato)
            if self.esta_vacia():
                 self.cabeza=nuevo
                 self.cola=nuevo
            else:
                 nuevo.siguiente=self.cabeza
                 self.cabeza.anterior=nuevo
                 self.cabeza=nuevo

    def insertar_final(self,dato):
            nuevo=NodoDoble(dato)
            if self.esta_vacia():
                self.cabeza=nuevo
                self.cola=nuevo
            else:
                self.cola.siguiente=nuevo
                nuevo.anterior=self.cola
                self.cola=nuevo

    def eliminar_inicio(self):
         if self.esta_vacia():
            return None
         
         dato=self.cabeza.dato
         if self.cabeza==self.cola:
              self.cabeza=None
              self.cola=None
         else:
              self.cabeza = self.cabeza.siguiente
              self.cabeza.anterior=None

         return dato
    def eliminar_final(self):
          if self.esta_vacia():
            return None
          dato=self.cola.dato
          if self.cabeza==self.cola:
              self.cabeza=None
              self.cola=None
          else:
              self.cola=self.cola.anterior
              self.cola.siguiente=None
          return dato    
    
    def recorrer_adelante(self):
         if self.esta_vacia():
              print("lista vacia")
              return
         print("inicio ->fin", end="")
         actual=self.cabeza
         elementos=[]
         while actual:
              elementos.append(str(actual.dato))
              actual=actual.siguiente
         print("<->" .join (elementos))

    def recorrer_atras(self):
         if self.esta_vacia():
              print("lista vacia")
              return

         print("fin<-> inicio", end=" ")
         actual=self.cola
         elementos=[]
         while actual:
              elementos.append(str(actual.dato))
              actual=actual.anterior
         print("<-> ".join(elementos))

    def buscar(self, dato):
              actual=self.cabeza
              while actual:
                   if actual.dato ==dato:
                        return True
                   actual= actual.siguiente
              return False
    def __len__(self):
         contador=0
         actual=self.cabeza
         while actual:
              contador +=1
              actual=actual.siguiente
         return contador
    
    def __str__(self):
         if self.esta_vacia():
              return "lista vacia"
         elementos=[]
         actual= self.cabeza
         while actual:
              elementos.append(str(actual.dato))
              actual=actual.siguiente
         return "<->".join(elementos)     
         
         
              
         
    

                         
                




         

                 