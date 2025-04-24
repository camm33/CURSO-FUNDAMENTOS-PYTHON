import re

def frecuencia_palabras():
    try:
        texto = input("Ingrese un texto: ").strip()

        if not texto:
            raise ValueError("No se ingresó ningún texto.")

        # Convertir a minúsculas y extraer solo palabras (ignorando signos de puntuación)
        palabras = re.findall(r'\b\w+\b', texto.lower())

        # Contar frecuencia de palabras
        frecuencia = {}
        for palabra in palabras:
            frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

        # Mostrar resultados
        print("Frecuencia de palabras:")
        for palabra, conteo in frecuencia.items():
            print(f"{palabra}: {conteo}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
