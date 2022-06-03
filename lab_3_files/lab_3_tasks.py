# Ввод строки и подстроки с клавиатуры
from compare import compare_funcs
from lab_3_files.index_searches import *
from lab_3_files.barley_break import solve_astar
from view import get_variant


# Поиски в строке
def task_1():
    haystack = input('Введите строку: ')
    needle = input('Введите подстроку: ')
    original_haystack = haystack

    is_case_matter = get_variant(
        message='Необходима чувствительность к регистру? (y/n): ',
        variants=('y', 'n', 'д', 'н'))

    if is_case_matter in ('n', 'н'):
        haystack, needle = haystack.lower(), needle.lower()

    funcs = (kmp_search, bm_search, haystack.find)
    args = [(haystack, needle) for _ in range(3)]
    args[2] = (needle, )
    results = compare_funcs(funcs, args)

    display_index(original_haystack, len(needle), results[0])
    display_index(original_haystack, len(needle), results[1])


# Пятнашки
def task_2():
    # Проверка на работу граничных случаев
    print('moves to solve 1st:', solve_astar([1, 2, 3, 4, 5, 6, 7, 8, 13, 9, 11, 12, 10, 14, 15, 0]))  # Решаемо
    print('moves to solve 2nd:', solve_astar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]))  # Решаемо
    print('moves to solve 3rd:', solve_astar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 0]))  # Нерешаемо

    # Вывод сложного пазла
    # start_time = time.time()
    # #moves = solve_astar([9, 5, 14, 15, 13, 6, 7, 11, 12, 10, 8, 2, 3, 4, 1, 0])
    # print('[solve_astar] moves: ', moves, '\n[solve_astar] total moves:', len(moves))  # Решаемо
    # print('[solve_astar] took %s seconds' % (time.time() - start_time))


# Вывод индекса
def display_index(haystack, needle_length, index):
    if index != -1:
        print(f'\n{haystack}')
        print(' ' * index + '^' + '-' * (needle_length - 1))
        print(' ' * index + str(index))
    else:
        print('\nПодстрока отсутствует')
