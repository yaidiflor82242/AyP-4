class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class Pila:

    def __init__(self):
        self.tope=None

    def push(self, dato):
        nuevo=Nodo(dato)
        nuevo.siguiente=self.tope

    def pop(self):
        if self.esta_vacia():
            return None
        dato=self.tope.dato
        self.tope=self.tope.siguiente
        return dato

    def peek(self):
        if self.esta_vacia():
            return None
        return self.tope.dato

    def esta_vacia(self):
        return self.tope is None


def verificar_balanceo(expresion):

    pila = Pila()

    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
#creacionde conjunto de aperturas para optimizar la verificacion
    aperturas=set (pares.values())
    cierres=set(pares.keys())

    for token in expresion:

        if token in aperturas:
            pila.push(token)
            print(f"Agregando {token} a la pila")

        elif token in cierres:
            if pila.esta_vacia():
                return False 
            tope=pila.pop() 
            if tope != pares[token]:
                return False    
    if pila.esta_vacia():
            return True
    else:
            return  False    

  

exp ="{[*(+D)]}"

print(verificar_balanceo(exp))

#heap arbol binario 