# 4. Búsqueda Exponencial: Buscar un libro en una biblioteca digital
def busqueda_exponencial_libros(biblioteca, libro_buscar):
    if biblioteca[0] == libro_buscar:
        return "Libro encontrado en la primera posición"
    
    i = 1
    while i < len(biblioteca) and biblioteca[i] <= libro_buscar:
        i = i * 2
    
    return busqueda_binaria_libros(biblioteca, libro_buscar, i // 2, min(i, len(biblioteca)))

def busqueda_binaria_libros(biblioteca, libro_buscar, izquierda, derecha):
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if biblioteca[medio] == libro_buscar:
            return f"Libro '{libro_buscar}' encontrado"
        elif biblioteca[medio] < libro_buscar:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return "Libro no encontrado"

# Ejemplo de uso:
biblioteca = sorted(["El Quijote", "Cien años de soledad", "1984", "El principito", "Rayuela"])
print(busqueda_exponencial_libros(biblioteca, "1984"))