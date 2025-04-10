def separar_pares_impares(lista_numeros):
    pares = sorted([num for num in lista_numeros if num % 2 == 0])
    impares = sorted([num for num in lista_numeros if num % 2 != 0])
    return pares, impares

    #ejemplo 
    numeros = [5, 8, 12, 3, 7, 6, 14, 9]
    pares, impares = separar_ separar_pares_impares(numeros)
    print("pares:", pares)
    print("impares:", impares)
