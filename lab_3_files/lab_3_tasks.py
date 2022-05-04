# Ввод строки и подстроки с клавиатуры
import compare
from lab_3_files import index_searches
from lab_3_files import barley_break


def enter_strings():
    haystack = input("Введите строку: ")
    needle = input("Введите подстроку: ")
    return haystack, needle


# Вывод индекса
def display_index(haystack, needle_length, index):
    if index != -1:
        print(f"\n{haystack}")
        print(" " * index + "^" + "-" * (needle_length - 1))
        print(" " * index + str(index))
    else:
        print("\nПодстрока отсутствует")


# Задание №1
def task_1():
    haystack, needle = enter_strings()
    original_haystack = haystack

    isCaseMatter = ""
    while isCaseMatter != "y" and isCaseMatter != "n":
        isCaseMatter = input("Необходима чувствительность к регистру? (y/n): ")
    if isCaseMatter == "n":
        haystack = haystack.lower()
        needle = needle.lower()

    index = index_searches.KMP_search(haystack, needle)
    display_index(original_haystack, len(needle), index)

    index = index_searches.BM_search(haystack, needle)
    display_index(original_haystack, len(needle), index)

    compare.find_bestie([
        (index_searches.KMP_search, haystack, needle),
        (index_searches.BM_search, haystack, needle),
        (haystack.find, needle, None, None),
    ], 10)


# Задание №2
def task_2():
    desk = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
