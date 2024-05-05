from typing import List, TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __lt__(self, other: T) -> bool:
        raise NotImplementedError

def insertion_sort_in_place(t: List[T]) -> None:
    """
    Ordena la lista t en su lugar utilizando el algoritmo de inserción.
    """
    n = len(t)
    for i in range(1, n):
        temp = t[i]
        j = i - 1
        while j >= 0 and t[j] > temp:
            t[j + 1] = t[j]
            j -= 1
        t[j + 1] = temp

def insertion_sort_with_additional_table(t: List[T]) -> None:
    """
    Ordena la lista t en su lugar utilizando una tabla adicional para reorganizar los elementos.
    """
    n = len(t)
    r = [None] * n
    for i in range(n):
        temp = t[i]
        j = i - 1
        while j >= 0 and r[j] > temp:
            r[j + 1] = r[j]
            j -= 1
        r[j + 1] = temp
    for i in range(n):
        t[i] = r[i]

# Ejemplo de uso:
if __name__ == "__main__":
    # Definir una lista de elementos comparables
    elementos = [5, 2, 7, 1, 9, 3]

    # Usar el primer algoritmo para ordenar la lista en su lugar
    insertion_sort_in_place(elementos)
    print("Lista ordenada en su lugar (primer algoritmo):", elementos)

    # Usar el segundo algoritmo para ordenar la lista en su lugar
    elementos = [5, 2, 7, 1, 9, 3]  # Reiniciar la lista
    insertion_sort_with_additional_table(elementos)
    print("Lista ordenada en su lugar (segundo algoritmo):", elementos)
