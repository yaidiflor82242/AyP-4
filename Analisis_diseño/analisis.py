"""def tiene_duplicados(lista): #recorrer en complejidad n
    n=len(lista)
    for i in range (n):
        for j in range(i+1,n):
            if lista[i]==lista[j]:
                return True
    return False  #complejidad de 1"""

# f(n)= 1+n+2n^2
#O(n^2)  #siempre se deja el termino mas grande es decir el mas complejo  CUADRATICA


#SUMAS
#cuando se suma la complejidad de ambas se toma la n mayor
#dos  ciclos anidados es CUADRATICO y tienen que depender de la entrada 
"""en un while que tiene una condicion que por ejemplo incremente de 2 en 2 es de complejo LOGARITMICO   O(log n)"""

#divides y venceras forma de programar

"""RELACION DE ORDEN"""
#una lineal y la otra 


#EJERCICIO
lista=[3,5,2,1,3]
#cual es el elemento que mas se repite en la lsta
def lemento_mas_repetido(lista): #recorrer en complejidad n
    max_elemento=lista[0]
    max_conteo= 0
    for i in range (len(lista)):
        conteo=0
        for j in range(len(lista)):
                if lista[i]==lista[j]:
                    conteo +=1
                if conteo > max_conteo:
                    max_conteo=conteo
                    max_elemento=lista[i]
    return max_elemento,max_conteo    

#f(n)=3+2n^2+4n   O(n^2)

#alguna forma en la que la complejidad sea menor

"""HACERLO CON DICCIONARIO"""

def elementos_repetidos(lista):
     frecuencias={}

     for elemento in lista:
          if elemento in frecuencias: #buscar en un diccionario es contaste  si es en una liista es lineal (in)
               frecuencias[elemento]+=1
          else:
               frecuencias[elemento]=0  
     max_elemento=0
     max_conteo=0

     for elemento, conteo in frecuencias:
          if conteo> max_conteo:
            max_conteo=conteo
            max_elemento=elemento

     return max_elemento,max_conteo

#f(n)=4+7n  O(n)  hay dos ciclos pero no uno dentro del otro la complejidad es n porque es una suma de n+n 
# y se toma el valor mayor


#metodo que diga si hay 3 numeros que sumen 0 seguidos 

def sumar_cero(lista):
     n=len(lista)
     for i in range(n):
          for j in range (i+1,n):
               for k in range(j+1,n):
                    if lista[i]+lista[j]+lista[k]==0:
                         return True
                    
     return False

#f(n)=1+n+2n^3
#0(n^3)s





  
        
            
    



