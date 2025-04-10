def numero_a_texto(numero):
    numeros_texto = {
        "0": "cero", "1": "uno", "2": "dos", "3": "tres", "4": "cuatro",
        "5": "cinco", "6": "seis", "7": "siete", "8": "ocho", "9": "nueve"
    }
    return " - ".join(numeros_texto[d] for d in str(numero))

# Ejemplo de uso
print(numero_a_texto(134))  # "uno - tres - cuatro"
