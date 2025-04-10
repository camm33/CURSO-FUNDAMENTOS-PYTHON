def contar_letras(palabra):
    diccionario_letras = {}
    for letra in palabra:
        if letra in diccionario_letras:
            diccionario_letras[letra] += 1
        else:
            diccionario_letras[letra] = 1
    return diccionario_letras

# Ejemplo de uso
resultado = contar_letras("colombia")
print(resultado)
