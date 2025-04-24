# Inventario inicial
inventario = {
    'manzanas': 50,
    'naranjas': 30,
    'peras': 20
}

def mostrar_inventario():
    print("Inventario actual:")
    for producto, cantidad in inventario.items():
        print(f"- {producto}: {cantidad} unidades")
    print()

def agregar_producto(nombre, cantidad):
    if nombre in inventario:
        print(f"El producto '{nombre}' ya existe. Usa actualizar_producto para cambiar su stock.")
    else:
        inventario[nombre] = cantidad
        print(f"Producto '{nombre}' agregado con {cantidad} unidades.")

def actualizar_producto(nombre, cantidad):
    try:
        if nombre not in inventario:
            raise KeyError(f"El producto '{nombre}' no existe en el inventario.")
        inventario[nombre] = cantidad
        print(f"Stock de '{nombre}' actualizado a {cantidad}.")
    except KeyError as e:
        print(e)

def eliminar_producto(nombre):
    try:
        if nombre not in inventario:
            raise KeyError(f"El producto '{nombre}' no se puede eliminar porque no existe.")
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    except KeyError as e:
        print(e)

# Ejemplo de uso paso a paso
print("Inventario inicial:", inventario)
actualizar_producto('peras', 25)
agregar_producto('bananas', 40)
eliminar_producto('naranjas')
print("Inventario final:", inventario)
