# 2. Búsqueda Lineal: Buscar un producto en una lista de compras
def busqueda_lineal_compras(lista_compras, producto_buscar):
    for i, producto in enumerate(lista_compras):
        if producto == producto_buscar:
            return f"El producto {producto} está en la posición {i+1} de tu lista"
    return "Producto no encontrado en la lista"

# Ejemplo de uso:
lista_compras = ["leche", "pan", "huevos", "manzanas", "pasta"]
print(busqueda_lineal_compras(lista_compras, "huevos"))