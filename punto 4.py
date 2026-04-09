def formas_cambio(monedas, total):
    """
    Dado un conjunto de monedas (sin repetir valores) y un total,
    calcular de cuántas formas se puede obtener ese total.

    Puedes usar una moneda varias veces.
    """

    def resolver(i, total):
        # Caso base exacto
        if total == 0:
            return 1

        # Si me paso o no hay más monedas
        if total < 0 or i == len(monedas):
            return 0

        # Usar moneda actual
        usar = resolver(i, total - monedas[i])

        # No usar moneda actual
        no_usar = resolver(i + 1, total)

        return usar + no_usar

    return resolver(0, total)


print(formas_cambio([1,2,5], 5))  # 4

#SUBCONJUNTOS QUE SUMAN UN VALOR

def subconjuntos_suma(lista, objetivo):
    """
    Dada una lista de números, retorna cuántos subconjuntos
    suman exactamente el valor objetivo.

    Cada elemento se puede usar UNA sola vez.
    """

    def resolver(i, suma_actual):
        # Caso exacto
        if suma_actual == objetivo:
            return 1
        
        # Si me paso o termino lista
        if suma_actual > objetivo or i == len(lista):
            return 0
        
        # Incluir elemento
        incluir = resolver(i + 1, suma_actual + lista[i])
        
        # No incluir
        no_incluir = resolver(i + 1, suma_actual)
        
        return incluir + no_incluir

    return resolver(0, 0)
print(subconjuntos_suma([1,2,3,4], 5))  # 2
