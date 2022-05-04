import random
import generators
import compare

from lab_2_files import searches
from lab_2_files.node import generate_binary_tree
from lab_2_files import hashes
from lab_2_files import chess


# Задание №1
def task_1():
    numbers = generators.generate_numbers(99999, 000, 999)
    tree = generate_binary_tree(numbers)
    numbers.sort()

    desired_number = generators.random_value(numbers)
    compare.find_bestie([
        (searches.binary_search, numbers, desired_number),
        (searches.binary_tree_search, tree, desired_number),
        (searches.fibonacci_search, numbers, desired_number),
        (searches.interpolation_search, numbers, desired_number),
        (numbers.index, desired_number),
    ], 10)


# Задание №2
def task_2():
    strings = generators.generate_strings("emojies", hashes.Hash_table.size)

    simple_rehash_table = hashes.Simple_rehash_table(strings)
    simple_rehash_table.display(show_rehashes=True)

    random_rehash_table = hashes.Random_rehash_table(strings)
    random_rehash_table.display(show_rehashes=True)

    chain_rehash_table = hashes.Chain_rehash_table(strings)
    chain_rehash_table.display()

    desired_number = generators.random_value(strings)
    compare.find_bestie([
        (simple_rehash_table.find, desired_number),
        (random_rehash_table.find, desired_number),
        (chain_rehash_table.find, desired_number)
    ], 1)


# Задание №3
def task_three():
    board = [[" " for j in range(8)] for i in range(8)]
    first_y, first_x = random.randint(0, 7), random.randint(0, 7)

    # Расстановка ферзей
    while len(chess.Queen.s) != 8:
        chess.Queen.s = []
        chess.Queen(first_y, first_x)

    chess.Queen.place_on_board(board)
    chess.print_board(board)
