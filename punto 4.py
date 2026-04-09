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
