import random
from datetime import datetime

#создание матрицы m*n из случынйх чисел от min_limit до max_limit
def generateMatrix(m = 50, n = 50, min_limit = -250, max_limit = 1009):
    return [[random.randint(min_limit, max_limit) for j in range(n)] for i in range(m)]
#вывод матрицы в консоль
def printMatrix(matrix, title = ""):
    print("\n" + title)
    for line in matrix:
        for number in line:
            cell = str(number)
            print(cell + " "*(4-len(cell)), end=' ')
        print("\n")
#сортировка выбором 
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
#сортировка вставками 
def insertion_sort(matrix):
    height = len(matrix)
    for line in range(height):
        width = len(matrix[line])
        for i in range(1, width): 
            key = matrix[line][i] 
            k = i - 1 
            while k >= 0 and key < matrix[line][k]: 
                matrix[line][k+1] = matrix[line][k] 
                k -= 1 
            matrix[line][k+1] = key
    return matrix
#сортировка обменом
def bubble_sort(matrix):
    height = len(matrix)
    for line in range(height): 
        width = len(matrix[line])
        for i in range(width-1): 
            for j in range(width-i-1): 
                if matrix[line][j] > matrix[line][j+1]: 
                    matrix[line][j], matrix[line][j+1] = matrix[line][j+1], matrix[line][j]
    return matrix
#сортировка методом шелла
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
#турнирная
def tournament_sort(matrix):
    height = len(matrix)
    for line in range(height):
        width = len(matrix[line])
        tree = [None] * 2 * (width + width % 2)
        treeWitdh = len(tree)
        index = treeWitdh - width - width % 2
    
        for i, v in enumerate(matrix[line]):
            tree[index + i] = (i, v)
    
        for j in range(width):
            n = width
            index = treeWitdh - width - width % 2
            while index > -1:
                n = (n + 1) // 2
                for i in range(n):
                    i = max(index + i * 2, 1)
                    if tree[i] != None and tree[i + 1] != None:
                        if tree[i][1] < tree[i + 1][1]:
                            tree[i // 2] = tree[i]
                        else: 
                            tree[i // 2] = tree[i + 1]
                    else: 
                        tree[i // 2] = tree[i] if tree[i] != None else tree[i + 1] 
                index -= n 
                
            index, x = tree[0] 
            matrix[line][j] = x 
            tree[treeWitdh - width - width % 2 + index] = None
    return matrix
#быстрая сортировка
def quick_sort(matrix):
    height = len(matrix)
    for line in range(height):
        width = len(matrix[line])
        quicksort(matrix[line], 0, width)
    return matrix
def quicksort(array, start, end):
    if end - start > 1: 
        p = partition(array, start, end) 
        quicksort(array, start, p) 
        quicksort(array, p + 1, end)
def partition(array, start, end): 
    pivot = array[start] 
    i = start + 1 
    j = end - 1 
    while True: 
        while (i <= j and array[i] <= pivot): 
            i = i + 1 
        while (i <= j and array[j] >= pivot): 
            j = j - 1 
        if i <= j: 
            array[i], array[j] = array[j], array[i] 
        else: 
            array[start], array[j] = array[j], array[start] 
            return j 
#пирамидальная сортировка 
def heap_sort(matrix):
    height = len(matrix)
    for line in range(height):
        width = len(matrix[line])
        build_max_heap(matrix[line]) 
        for i in range(width - 1, 0, -1): 
            matrix[line][0], matrix[line][i] = matrix[line][i], matrix[line][0] 
            max_heapify(matrix[line], index = 0, size = i)
    return matrix  
def build_max_heap(array): 
    height = len(array) 
    start = (height - 1 - 1) // 2
    while start >= 0: 
        max_heapify(array, index = start, size = height) 
        start = start - 1 
def max_heapify(array, index, size): 
    l = 2 * index + 1 
    r = 2 * index + 2 
    if (l < size and array[l] > array[index]): 
        largest = l 
    else: 
        largest = index 
    if (r < size and array[r] > array[largest]): 
        largest = r 
    if (largest != index): 
        array[largest], array[index] = array[index], array[largest] 
        max_heapify(array, largest, size) 
        
#m = int(input("n = ")) 
#n = int(input("m = ")) 
#min_lim = int(input("min_limit = ")) 
#max_lim = int(input("max_limit = "))
matrix = generateMatrix()

before = int(datetime.now().microsecond)
selection_sort(matrix.copy())
after = int(datetime.now().microsecond)
time = str(abs(after - before))
print("Методом выбора:\t" + time)

before = int(datetime.now().microsecond)
insertion_sort(matrix.copy())
after = int(datetime.now().microsecond)
time = str(abs(after - before))
print("Вставками:\t" + time)

before = int(datetime.now().microsecond)
bubble_sort(matrix.copy())
after = int(datetime.now().microsecond)
time = str(abs(after - before))
print("Методом обмена:\t" + time)

before = int(datetime.now().microsecond)
shell_sort(matrix.copy())
after = int(datetime.now().microsecond)
time = str(abs(after - before))
print("Методом Шелла:\t" + time)

before = int(datetime.now().microsecond)
tournament_sort(matrix.copy())
after = int(datetime.now().microsecond)
time = str(abs(after - before))
print("Турнирная:\t" + time)

before = int(datetime.now().microsecond)
quick_sort(matrix.copy())
after = int(datetime.now().microsecond)
time = str(abs(after - before))
print("Быстрая:\t" + time)

before = int(datetime.now().microsecond)
heap_sort(matrix.copy())
after = int(datetime.now().microsecond)
time = str(abs(after - before))
print("Пирамидальная:\t" + time)

before = int(datetime.now().microsecond)
sorted(matrix.copy())
after = int(datetime.now().microsecond)
time = str(abs(after - before))
print("Стандартная:\t" + time)


