import generators
from compare import find_bestie, display_times, func_name
from lab_1_files.sortings import selection_sort, insertion_sort, \
    bubble_sort, shell_sort, tournament_sort, quick_sort, heap_sort


# Алгоритмы сортировки
def task_3():

    # Ввод значений и генерация матрицы
    n = int(input('n = '))
    m = int(input('m = '))
    min_limit = int(input('min_limit = '))
    max_limit = int(input('max_limit = '))
    matrix = generators.generate_matrix(m, n, min_limit, max_limit)

    # Задание функций
    funcs = (selection_sort, insertion_sort, bubble_sort, shell_sort,
             tournament_sort, quick_sort, heap_sort, sorted)
    names = list(map(func_name, funcs))

    # Вывод времен
    times, best_time, _ = find_bestie(funcs, [matrix.copy() for _ in range(8)])
    display_times(names, times, best_time)
