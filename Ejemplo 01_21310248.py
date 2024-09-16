# 1. Búsqueda Binaria: Encontrar un contacto en una lista telefónica
def busqueda_binaria_contactos(lista_contactos, nombre_buscar):
    izquierda, derecha = 0, len(lista_contactos) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista_contactos[medio][0] == nombre_buscar:
            return lista_contactos[medio][1]  # Retorna el número de teléfono
        elif lista_contactos[medio][0] < nombre_buscar:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return "Contacto no encontrado"

# Ejemplo de uso:
contactos = [("Ana", "1234567"), ("Carlos", "2345678"), ("María", "3456789"), ("Pedro", "4567890")]
print(busqueda_binaria_contactos(sorted(contactos), "María"))
