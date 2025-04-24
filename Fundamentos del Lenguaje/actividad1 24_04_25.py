def calculadora():
    try:
        # Solicitar al usuario los números y el operador
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        operador = input("Ingrese el operador (+, -, *, /, **, //): ")

        # Evaluar el operador ingresado
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir entre cero.")
            resultado = num1 / num2
        elif operador == '**':
            resultado = num1 ** num2
        elif operador == '//':
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir entre cero.")
            resultado = num1 // num2
        else:
            raise ValueError("Operador no válido.")

        print(f"Resultado: {num1} {operador} {num2} = {resultado}")

    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except ZeroDivisionError as zde:
        print(f"Error de división: {zde}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
