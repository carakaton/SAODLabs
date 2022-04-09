# Бинарный поиск
def binary_search(data, value):
    left = 0
    right = len(data)

    while left <= right:
        index = (right + left) // 2

        if data[index] > value:
            right = index
        elif data[index] < value:
            left = index
        else:
            return index

    return None


# Поиск в бинарном дереве
def binary_tree_search(tree, value):
    return tree.find_value(value)


# Поиск фибоначчи
def fibonacci_search(data, value):
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib_m = fib_m_minus_1 + fib_m_minus_2
    while fib_m < len(data):
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib_m
        fib_m = fib_m_minus_1 + fib_m_minus_2
    index = -1
    while fib_m > 1:
        i = min(index + fib_m_minus_2, (len(data) - 1))
        if data[i] < value:
            fib_m = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1
            index = i
        elif data[i] > value:
            fib_m = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1
        else:
            return i
    if fib_m_minus_1 and index < (len(data) - 1) and data[index + 1] == value:
        return index + 1
    return None


# Интерполяционный поиск
def interpolation_search(data, value):
    low = 0
    high = (len(data) - 1)
    while low <= high and data[low] <= value <= data[high]:
        index = low + int(((float(high - low) / (data[high] - data[low])) * (value - data[low])))
        if data[index] == value:
            return index
        if data[index] < value:
            low = index + 1
        else:
            high = index - 1
    return None
