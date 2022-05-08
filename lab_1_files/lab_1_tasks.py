import generators
import compare
from lab_1_files import sortings


def task_3():

    matrix = generators.generate_matrix()

    compare.find_bestie([
        (sortings.selection_sort, matrix.copy()),
        (sortings.insertion_sort, matrix.copy()),
        (sortings.bubble_sort, matrix.copy()),
        (sortings.shell_sort, matrix.copy()),
        (sortings.tournament_sort, matrix.copy()),
        (sortings.quick_sort, matrix.copy()),
        (sortings.heap_sort, matrix.copy()),
        (sorted, matrix.copy()),
    ], 10)

# m = int(input('n = '))
# n = int(input('m = '))
# min_lim = int(input('min_limit = '))
# max_lim = int(input('max_limit = '))

