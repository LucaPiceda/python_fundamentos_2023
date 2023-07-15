def filtrarPares(numeros):
 pares = []
 for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
 return pares