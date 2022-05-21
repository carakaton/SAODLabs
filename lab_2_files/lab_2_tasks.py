import random
import generators
from compare import find_bestie, display_times, func_name
from lab_2_files.searches import binary_search, binary_tree_search, fibonacci_search, interpolation_search
from lab_2_files.node import generate_binary_tree
from lab_2_files import hashes, chess


# Поиск
def task_1():

    # Генерация
    numbers = generators.generate_numbers(99999, 000, 999)
    tree = generate_binary_tree(numbers)
    numbers.sort()
    desired_number = generators.random_value(numbers)

    # Задание функций
    funcs = (binary_search, binary_tree_search, fibonacci_search, interpolation_search, numbers.index)
    names = list(map(func_name, funcs))

    args = [(numbers, desired_number) for _ in range(5)]
    args[1], args[4] = (tree, desired_number), desired_number

    # Вывод
    times, best_time, _ = find_bestie(funcs, args)
    display_times(names, times, best_time)


# Поиск рехешированием
def task_2():

    # Генерация
    strings = generators.generate_strings('emojies', hashes.HashTable.size)

    simple_rehash_table = hashes.SimpleRehashTable(strings)
    simple_rehash_table.display(show_rehashes=True)

    random_rehash_table = hashes.RandomRehashTable(strings)
    random_rehash_table.display(show_rehashes=True)

    chain_rehash_table = hashes.ChainRehashTable(strings)
    chain_rehash_table.display()

    desired_number = generators.random_value(strings)

    # Задание функций
    funcs = (simple_rehash_table.find, random_rehash_table.find, chain_rehash_table.find)
    names = list(map(func_name, funcs))

    # Вывод
    times, best_time, _ = find_bestie(funcs, [desired_number for _ in range(3)])
    display_times(names, times, best_time)


# Шахматы
def task_3():
    board = [[' ' for j in range(8)] for i in range(8)]
    first_y, first_x = random.randint(0, 7), random.randint(0, 7)

    # Расстановка ферзей
    while len(chess.Queen.s) != 8:
        chess.Queen.s = []
        chess.Queen(first_y, first_x)

    chess.Queen.place_on_board(board)
    chess.print_board(board)
