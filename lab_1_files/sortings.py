# Сортировка выбором
def selection_sort(matrix):
    height = len(matrix)
    for line in range(height):
        width = len(matrix[line])
        for i in range(width - 1):
            minimal = i
            for j in range(i + 1, width):
                if matrix[line][j] < matrix[line][minimal]:
                    minimal = j
            matrix[line][i], matrix[line][minimal] = matrix[line][minimal], matrix[line][i]

    return matrix


# Сортировка вставками
def insertion_sort(matrix):
    height = len(matrix)
    for line in range(height):
        width = len(matrix[line])
        for i in range(1, width):
            key = matrix[line][i]
            k = i - 1
            while k >= 0 and key < matrix[line][k]:
                matrix[line][k + 1] = matrix[line][k]
                k -= 1
            matrix[line][k + 1] = key
    return matrix


# Сортировка обменом
def bubble_sort(matrix):
    height = len(matrix)
    for line in range(height):
        width = len(matrix[line])
        for i in range(width - 1):
            for j in range(width - i - 1):
                if matrix[line][j] > matrix[line][j + 1]:
                    matrix[line][j], matrix[line][j + 1] = matrix[line][j + 1], matrix[line][j]
    return matrix


# Сортировка методом Шелла
def shell_sort(matrix):
    height = len(matrix)
    for line in range(height):
        width = len(matrix[line])
        d = width // 2
        while d > 0:
            for i in range(width):
                for j in range(i + d, width, d):
                    if matrix[line][i] > matrix[line][j]:
                        matrix[line][i], matrix[line][j] = matrix[line][j], matrix[line][i]
            d = d // 2
    return matrix


# Турнирная
def tournament_sort(matrix):
    height = len(matrix)
    for line in range(height):
        width = len(matrix[line])
        tree = [None] * 2 * (width + width % 2)
        tree_width = len(tree)
        index = tree_width - width - width % 2

        for i, v in enumerate(matrix[line]):
            tree[index + i] = (i, v)

        for j in range(width):
            n = width
            index = tree_width - width - width % 2
            while index > -1:
                n = (n + 1) // 2
                for i in range(n):
                    i = max(index + i * 2, 1)
                    if tree[i] is not None and tree[i + 1] is not None:
                        if tree[i][1] < tree[i + 1][1]:
                            tree[i // 2] = tree[i]
                        else:
                            tree[i // 2] = tree[i + 1]
                    else:
                        tree[i // 2] = tree[i] if tree[i] is not None else tree[i + 1]
                index -= n

            index, x = tree[0]
            matrix[line][j] = x
            tree[tree_width - width - width % 2 + index] = None
    return matrix


# Быстрая сортировка
def quick_sort(matrix):

    def partition(array, start, end):
        pivot = array[start]
        i = start + 1
        j = end - 1
        while True:
            while i <= j and array[i] <= pivot:
                i = i + 1
            while i <= j and array[j] >= pivot:
                j = j - 1
            if i <= j:
                array[i], array[j] = array[j], array[i]
            else:
                array[start], array[j] = array[j], array[start]
                return j

    def quick_sort_line(array, start, end):
        if end - start > 1:
            p = partition(array, start, end)
            quick_sort_line(array, start, p)
            quick_sort_line(array, p + 1, end)

    height = len(matrix)
    for line in range(height):
        width = len(matrix[line])
        quick_sort_line(matrix[line], 0, width)
    return matrix


# Сортировка кучами
def heap_sort(matrix):

    def max_heapify(array, index, size):
        l = 2 * index + 1
        r = 2 * index + 2
        if l < size and array[l] > array[index]:
            largest = l
        else:
            largest = index
        if r < size and array[r] > array[largest]:
            largest = r
        if largest != index:
            array[largest], array[index] = array[index], array[largest]
            max_heapify(array, largest, size)

    def build_max_heap(array):
        height = len(array)
        start = (height - 1 - 1) // 2
        while start >= 0:
            max_heapify(array, index=start, size=height)
            start = start - 1

    height = len(matrix)
    for line in range(height):
        width = len(matrix[line])
        build_max_heap(matrix[line])
        for i in range(width - 1, 0, -1):
            matrix[line][0], matrix[line][i] = matrix[line][i], matrix[line][0]
            max_heapify(matrix[line], index=0, size=i)
    return matrix
