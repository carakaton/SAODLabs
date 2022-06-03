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
        result += '.'  # Разделители для удобной проверки
    print(result)


# Сортировка матрицы по-диагонали
def task_3():

    # Ввод матрицы (пример: 1 2 3, 4 5 6, 7 8 9)
    enter = list(input().split(','))
    matrix = list()
    for line in range(len(enter)):
        matrix.append(list(map(int, enter[line].split())))

    # Сортировка
    matrix_height = len(matrix)
    matrix_length = len(matrix[0])
    start_y = matrix_height
    start_x = 0

    diagonal_count = matrix_length + matrix_height - 1
    for d in range(diagonal_count):
        diagonal_length = min(matrix_height - start_y, matrix_length - start_x)
        for i in range(diagonal_length - 1):
            y = start_y
            x = start_x
            for j in range(diagonal_length - i - 1):
                if matrix[y][x] > matrix[y + 1][x + 1]:
                    matrix[y][x], matrix[y + 1][x + 1] = matrix[y + 1][x + 1], matrix[y][x]
                y += 1
                x += 1

        if start_y != 0:
            start_y -= 1
        else:
            start_x += 1

    # Вывод матрицы в консоль
    for line in matrix:
        print()
        for number in line:
            cell = str(number)
            print(cell + ' ' * (3 - len(cell)), end=' ')
    print()
