from display import print_matrix


# Поиск наибольшего периметра
def task_1():

    # Ввод сегментов
    segments = list(map(int, input('Введите длины сегментов: ').split()))
    count = len(segments)

    # Сортировка
    for i in range(count - 1):
        for j in range(count - i - 1):
            if segments[j] > segments[j + 1]:
                segments[j], segments[j + 1] = segments[j + 1], segments[j]

    # Поиск максимума
    max_perimeter = 0
    for i in range(count - 2):
        a, b, c = segments[i], segments[i + 1], segments[i + 2]
        perimeter = a + b + c

        if (a + b > c and a + c > b and b + c > a) and (perimeter > max_perimeter):
            max_perimeter = perimeter

    # Вывод
    print(max_perimeter)


# Создать максимальное число
def task_2():

    # Ввод чисел
    numbers = list(map(int, input().split()))
    count = len(numbers)

    # Сортировка
    for i in range(count - 1):
        for j in range(count - i - 1):
            a = str(numbers[j])
            b = str(numbers[j + 1])

            len_a, len_b = len(a), len(b)
            mod_a = int(a + a[-1] * (len_b - len_a))
            mod_b = int(b + b[-1] * (len_a - len_b))

            if (mod_a < mod_b) or (mod_a == mod_b and len_a > len_b):
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    # Сборка и вывод числа
    result = ''
    for number in numbers:
        result += str(number)
        result += '.'  # разделители для удобной проверки
    print(result)


def task_3():
    # ввод матрицы (пример: 1 2 3, 4 5 6, 7 8 9)
    def enterMatrix():
        enter = list(input().split(","))
        matrix = list()
        for line in range(len(enter)):
            matrix.append(list(map(int, enter[line].split())))
        return matrix

    matrix = enterMatrix()

    # сортировка по-диагонали
    def diagonalSort(matrix):
        matrixHeight = len(matrix)
        matrixLenght = len(matrix[0])
        startY = matrixHeight
        startX = 0

        diagonalCount = matrixLenght + matrixHeight - 1
        for d in range(diagonalCount):
            diagonalLength = min(matrixHeight - startY, matrixLenght - startX)
            for i in range(diagonalLength - 1):
                y = startY
                x = startX
                for j in range(diagonalLength - i - 1):
                    if matrix[y][x] > matrix[y + 1][x + 1]:
                        matrix[y][x], matrix[y + 1][x + 1] = matrix[y + 1][x + 1], matrix[y][x]
                    y += 1
                    x += 1

            if startY != 0:
                startY -= 1
            else:
                startX += 1

    print_matrix(matrix, 3)
