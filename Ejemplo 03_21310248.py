# 3. Búsqueda por Saltos: Encontrar una fecha en un calendario
def busqueda_saltos_calendario(calendario, fecha_buscar):
    n = len(calendario)
    paso = int(n ** 0.5)
    prev = 0
    while calendario[min(paso, n) - 1] < fecha_buscar:
        prev = paso
        paso += int(n ** 0.5)
        if prev >= n:
            return "Fecha no encontrada"
    
    for i in range(prev, min(paso, n)):
        if calendario[i] == fecha_buscar:
            return f"Evento programado para la fecha {fecha_buscar}"
    
    return "Fecha no encontrada"

# Ejemplo de uso:
calendario = ["2024-01-01", "2024-02-14", "2024-03-08", "2024-04-22", "2024-05-01", "2024-06-15"]
print(busqueda_saltos_calendario(calendario, "2024-03-08"))