# Алгоритм Кнута-Морриса-Пратта
def KMP_search(haystack, needle):
    needle_length = len(needle)
    pi = [0] * needle_length

    for i in range(1, needle_length):
        k = pi[i - 1]
        while k > 0 and needle[k] != needle[i]:
            k = pi[k - 1]
        if needle[k] == needle[i]:
            k += 1
        pi[i] = k

    index = -1
    k = 0
    for i in range(len(haystack)):
        while k > 0 and needle[k] != haystack[i]:
            k = pi[k - 1]
        if needle[k] == haystack[i]:
            k = k + 1
        if k == needle_length:
            index = i - needle_length + 1
            break

    return index


# Упрощенный алгоритм Бойера-Мура
def BM_search(haystack, needle):
    needle_length = len(needle)
    haystack_length = len(haystack)

    # Создание словаря сдвигов
    dictionary = {}
    for i in range(needle_length, 0, -1):
        char = needle[needle_length - i - 1]
        dictionary[ord(char)] = i

    # Поиск подстроки
    haystack_index = needle_length - 1
    while haystack_index < haystack_length:
        needle_index = needle_length - 1
        for i in range(needle_length):
            if haystack[haystack_index] != needle[needle_index]:
                offset = i + dictionary.setdefault(ord(haystack[haystack_index]), needle_length)
                haystack_index += offset
                break
            haystack_index -= 1
            needle_index -= 1
        else:
            return haystack_index + 1
    return -1