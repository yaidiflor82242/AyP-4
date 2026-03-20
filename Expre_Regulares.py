# implementacion pila enlazada
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    def __init__(self):
        self.tope = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.tope is None

    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.tamanio += 1


# pila pop y peek
def pop(self):
    if self.esta_vacia():
        raise Exception("Pila vacía")
    dato = self.tope.dato
    self.tope = self.tope.siguiente
    self.tamanio -= 1
    return dato
def peek(self):
    if self.esta_vacia():
        raise Exception("Pila vacía")
    return self.tope.dato
def __len__(self):
    return self.tamanio

#evaluar posfija 
def evaluar_postfija(expresion):
    pila = Pila()
    tokens = expresion.split()
    for token in tokens:
        if token.isdigit():
            pila.push(int(token))
    else:
        b = pila.pop() # Segundo operando
        a = pila.pop() # Primer operando
    if token == '+': resultado = a + b
    elif token == '-': resultado = a - b
    elif token == '*': resultado = a * b
    elif token == '/': resultado = a / b
    pila.push(resultado)
    return pila.pop()

