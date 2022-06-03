from random import randint
from compare import compare_funcs
from lab_1_files.sortings import selection_sort, insertion_sort, \
    bubble_sort, shell_sort, tournament_sort, quick_sort, heap_sort


# Алгоритмы сортировки
def task_3():

    # Ввод значений и генерация матрицы
    n = int(input('n = '))
    m = int(input('m = '))
    min_limit = int(input('min_limit = '))
    max_limit = int(input('max_limit = '))
    matrix = generate_matrix(m, n, min_limit, max_limit)

    # Вывод времени
    funcs = (selection_sort, insertion_sort, bubble_sort, shell_sort, tournament_sort, quick_sort, heap_sort, sorted)
    args = [(matrix.copy(),) for _ in range(8)]
    compare_funcs(funcs, args)


# Создание матрицы m*n из случайных чисел от min_limit до max_limit
def generate_matrix(m=50, n=50, min_limit=-250, max_limit=1009):
    return [[randint(min_limit, max_limit) for j in range(n)] for i in range(m)]