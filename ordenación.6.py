def esta_explorado(t, inicio, fin):
    # Verificar si los índices son válidos
    if inicio < 0 or fin >= len(t) or inicio > fin:
        return False  # Si los índices no son válidos, salir y devolver False
    
    # Realizar una copia de seguridad del máximo del segmento
    m = t[inicio]  # Guardar el valor en la posición 'inicio' en la variable 'm' como copia de seguridad
    
    # Desplazar los elementos una celda hacia la izquierda
    for i in range(inicio, fin):
        t[i] = t[i + 1]  # Mover cada elemento una posición a la izquierda
    
    # Colocar el elemento más grande en la posición 'fin'
    t[fin] = m  # Colocar el valor guardado en 'm' en la posición 'fin'
    
    return True  # Devolver True para indicar que el segmento ha sido explorado correctamente

# Ejemplo
t = [10, 8, 15, 18, 12, 7, 18, 14, 9, 18, 21, 3]
inicio = 5
fin = 9

# Explorar el segmento definido por los índices 'inicio' y 'fin'
explorado = esta_explorado(t, inicio, fin)

# Imprimir el resultado de la exploración y la lista actualizada 't'
print("El segmento ha sido explorado correctamente:", explorado)
print("Tabla actualizada:", t)