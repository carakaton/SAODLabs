from random import randint
from compare import compare_funcs
from lab_2_files.searches import binary_search, binary_tree_search, fibonacci_search, interpolation_search
from lab_2_files.node import generate_binary_tree
from lab_2_files import hashes, chess


# Поиск
def task_1():

    # Генерация
    numbers = generate_numbers(99999, 000, 999)
    tree = generate_binary_tree(numbers)
    numbers.sort()
    desired_number = random_value(numbers)

    # Вывод
    funcs = (binary_search, binary_tree_search, fibonacci_search, interpolation_search, numbers.index)
    args = [(numbers, desired_number) for _ in range(5)]
    args[1], args[4] = (tree, desired_number), (desired_number,)
    compare_funcs(funcs, args)


# Поиск рехешированием
def task_2():

    # Генерация
    strings = generate_strings('emojies', hashes.HashTable.SIZE)

    simple_rehash_table = hashes.SimpleRehashTable('Таблица с простым рехешированием', strings)
    simple_rehash_table.display(show_rehashes=True)

    random_rehash_table = hashes.RandomRehashTable('Таблица с рехешированием с помощью псевдослучайных чисел', strings)
    random_rehash_table.display(show_rehashes=True)

    chain_rehash_table = hashes.ChainRehashTable('Таблица с рехешированием методом цепочек', strings)
    chain_rehash_table.display()

    desired_number = random_value(strings)

    # Вывод
    funcs = (simple_rehash_table.find, random_rehash_table.find, chain_rehash_table.find)
    args = [desired_number for _ in range(3)]
    compare_funcs(funcs, args)


# Шахматы
def task_3():
    board = [[' ' for j in range(8)] for i in range(8)]
    first_y, first_x = randint(0, 7), randint(0, 7)

    # Расстановка ферзей
    while len(chess.Queen.s) != 8:
        chess.Queen.s = []
        chess.Queen(first_y, first_x)

    chess.Queen.place_on_board(board)
    chess.print_board(board)


# Генерация списка из случайных чисел
def generate_numbers(count=10, min_limit=0, max_limit=999) -> list:
    return [randint(min_limit, max_limit) for value in range(count)]


# Выбор случайного числа из списка
def random_value(values):
    index = randint(0, len(values) - 1)
    return values[index]


# Генерация данных
def generate_strings(variant, length):
    strings = []

    if variant == "words":
        letters = [
            "a", "a", "b", "c", "o", "o", "d", "v", "g", "u", "u", "e", "e", "e"]
        for i in range(length):
            word = ""
            for j in range(5):
                letter = random_value(letters)
                word += letter
            strings.append(word)

    elif variant == "txt_emojies":
        txt_emojies = [
            "▼・ᴥ・▼", "(O_O)", "(･ω･)", "ʕ•ᴥ•ʔ", "(´∨`)", "(ಥ‿ಥ)", "(　；∀；)", "ʕ •ₒ• ʔ", "=^._.^=", "(๑ↀᆺↀ๑)", "(*´罒`*)"]
        for i in range(length):
            txt_emoji = random_value(txt_emojies)
            strings.append(txt_emoji)

    elif variant == "emojies":
        emojies = [
            "😀", "😃", "😄", "😁", "😆", "🥹", "😅", "😂", "🤣", "🥲", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰",
            "😘", "😗", "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐", "🤓", "😎", "🥸", "🤩", "🥳", "😏", "😒",
            "😞", "😔", "😟", "😕", "🙁", "😣", "😖", "😫", "😩", "🥺", "😢", "😭", "😠", "😡", "🤬", "🤯", "😳", "🥵",
            "🥶", "😶", "😱", "😨", "😰", "😥", "😓", "🤗", "🤔", "🫣", "🤭", "🫢", "🫡", "🤫", "🫠", "🤥", "😶", "🫥",
            "😐", "🫤", "😑", "😬", "🙄", "😯", "😦", "😧", "😮", "😲", "🥱", "😴", "😪", "😮", "😵", "😵", "🤐", "🥴",
            "🤧", "😷", "🤒", "🤕", "😈", "👿", "🤡"]
        for i in range(length):
            emoji = random_value(emojies)
            strings.append(emoji)

    return strings
