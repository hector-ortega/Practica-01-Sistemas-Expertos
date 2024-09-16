# 5. Búsqueda por Interpolación: Encontrar una canción en una playlist ordenada por duración
def busqueda_interpolacion_canciones(playlist, duracion_buscar):
    bajo = 0
    alto = len(playlist) - 1
    
    while bajo <= alto and duracion_buscar >= playlist[bajo][1] and duracion_buscar <= playlist[alto][1]:
        if bajo == alto:
            if playlist[bajo][1] == duracion_buscar:
                return f"Canción encontrada: {playlist[bajo][0]}"
            return "Canción no encontrada"
        
        pos = bajo + int(((float(alto - bajo) / (playlist[alto][1] - playlist[bajo][1])) * (duracion_buscar - playlist[bajo][1])))
        
        if playlist[pos][1] == duracion_buscar:
            return f"Canción encontrada: {playlist[pos][0]}"
        
        if playlist[pos][1] < duracion_buscar:
            bajo = pos + 1
        else:
            alto = pos - 1
    
    return "Canción no encontrada"

# Ejemplo de uso:
playlist = [("Canción A", 180), ("Canción B", 210), ("Canción C", 230), ("Canción D", 250), ("Canción E", 300)]
print(busqueda_interpolacion_canciones(playlist, 230))
