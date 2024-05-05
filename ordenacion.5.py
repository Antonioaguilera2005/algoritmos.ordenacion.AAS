from collections import defaultdict, deque
from typing import List, Tuple

def topological_sort(n: int, restrictions: List[Tuple[int, int]]) -> List[int]:
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Llenar graph y in_degree
    for i, j in restrictions:
        graph[i].append(j)
        in_degree[j] += 1

    queue = deque()
    topological_order = []

    # Inicializar la cola con tareas que no tienen dependencias
    for task in range(1, n+1):
        if in_degree[task] == 0:
            queue.append(task)

    # Realizar el ordenamiento topológico
    while queue:
        current_task = queue.popleft()
        topological_order.append(current_task)

        for neighbor in graph[current_task]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Verificar si se cumplen todas las restricciones
    if len(topological_order) == n:
        return topological_order
    else:
        return []  # No hay una ordenación válida

# Ejemplo de uso:
if __name__ == "__main__":
    num_tasks = 5
    restricciones = [(1, 2), (2, 3), (1, 3), (4, 5)]

    orden_topologica = topological_sort(num_tasks, restricciones)
    if orden_topologica:
        print("Orden topológica de las tareas:", orden_topologica)
    else:
        print("No hay una ordenación válida de las tareas.")
