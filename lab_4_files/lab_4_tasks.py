from lab_4_files.stack import Stack
from lab_4_files.deque import Deque


# Сортировка названий книг в алфавитном порядке
def task_1():
    deque_1, deque_2 = Deque(), Deque()

    # Чтение и вывод оригинального списка
    with open('lab_4_files/books.txt') as books:
        for book in books:
            print(book.rstrip())
            deque_1.push(book.rstrip())
        print()

    # Сортировка
    while not deque_1.is_empty():
        element = deque_1.pop()
        while not deque_2.is_empty() and deque_2.peek() < element:
            deque_1.push_left(deque_2.pop())
        deque_2.push(element)

    # Вывод отсортированного списка
    while not deque_2.is_empty():
        print(deque_2.pop())


# Расшифровка сообщения из файла
def task_2():

    # Кодирование символа
    def encode(symbol) -> chr:
        if ring.find(symbol) != -1:
            while True:
                if coding.peek_left() == symbol:
                    coding.push(coding.pop_left())
                    coding.push(coding.pop_left())
                    return coding.peek_left()
                coding.push(coding.pop_left())
        return symbol

    # Декодирование символа
    def decode(symbol) -> chr:
        if ring.find(symbol) != -1:
            while True:
                if coding.peek() == symbol:
                    coding.push_left(coding.pop())
                    coding.push_left(coding.pop())
                    return coding.peek()
                coding.push_left(coding.pop())
        return symbol

    # Создание дека с последовательностью всех символов
    ring = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    coding = Deque()
    for char in ring:
        coding.push(char)

    # Чтение и декодирование текста
    encoded_text, decoded_text = '', ''
    with open('lab_4_files/encoded_text.txt') as text:
        for char in text.read():
            encoded_text += char
            decoded_text += decode(char)

    # Вывод изначального и обработанного текста
    print(encoded_text + '\n')
    print(decoded_text)


# Перемещение дисков со стержня на стержень
def task_3():

    # Перемещение верхнего диска с одного стержня на другой
    def move_disk(start, end):

        # Генерация строки, визуализирующей состояние стержня (|---)
        def tower_str(stack) -> str:
            string = '|'
            for element in stack.data:
                string += f'{element}'
            return string + '-' * (disk_count - len(stack))

        # Фиксация состояний стержней до перемещения
        old_a, old_b, old_c = tower_str(a), tower_str(b), tower_str(c)

        # Перемещение
        end.push(start.pop())

        # Вывод шага
        print()
        print(f'{old_a}         {tower_str(a)}')
        print(f'{old_b}   ——>   {tower_str(b)}')
        print(f'{old_c}         {tower_str(c)}')

    # Рекурсивный алгоритм решения задачи
    def tower_of_hanoi(numbers, start, auxiliary, end):
        if numbers == 1:
            move_disk(start, end)
            return
        tower_of_hanoi(numbers - 1, start, end, auxiliary)
        move_disk(start, end)
        tower_of_hanoi(numbers - 1, auxiliary, start, end)

    # Создание стержней и ввод дисков
    a, b, c = Stack(), Stack(), Stack()
    disk_count = int(input('Введите количество дисков: '))
    for i in range(disk_count):
        a.push(disk_count - i)

    # Запуск алгоритма
    tower_of_hanoi(disk_count, a, b, c)


# Проверка баланса круглых скобок
def task_4():
    with open('lab_4_files/code.txt') as code:
        stack = Stack()
        for char in code.read():
            if char == '(':
                stack.push('')
            if char == ')':
                if stack.is_empty():
                    print('Баланс круглых скобок в файле: False')
                    break
                stack.pop()
        else:
            print(f'Баланс круглых скобок в файле: {stack.is_empty()}')


# Проверка баланса квадратных скобок
def task_5():
    with open('lab_4_files/code.txt') as code:
        deque = Deque()
        for char in code.read():
            if char == '[':
                deque.push('')
            if char == ']':
                if deque.is_empty():
                    print('Баланс квадратных скобок в файле: False')
                    break
                deque.pop()
        else:
            print(f'Баланс квадратных скобок в файле: {deque.is_empty()}')


# Вывод из файла сначала цифр, потом букв, а потом других символов
def task_6():
    digits, letters, others = Stack(), Stack(), Stack()

    # Наполнение стеков
    with open('lab_4_files/code.txt') as code:
        for char in code.read():
            if char.isdigit():
                digits.push(char.rstrip())
            elif char.isalpha():
                letters.push(char.rstrip())          
            elif char.rstrip() != '':
                others.push(char.rstrip())

    # Алгоритм обратного вывода
    def stack_str(stack) -> str:
        output = ''
        while not stack.is_empty():
            output = stack.pop() + output
        return output

    # Вывод стеков
    print(f'{stack_str(digits)}\n')
    print(f'{stack_str(letters)}\n')
    print(f'{stack_str(others)}')


# Вывод сначала всех отрицательных, а потом всех положительных чисел
def task_7():
    deque = Deque()

    # Запись отрицательных чисел в начало, а положительных в конец
    with open('lab_4_files/numbers.txt') as numbers:
        for number in numbers:
            print(number.rstrip(), end=' ')
            if int(number) < 0:
                deque.push_left(number.rstrip())
            else:
                deque.push(number.rstrip())
        print('\n')

    # 'Выворачивание' дека, чтобы вывод был в оригинальной последовательности
    while not int(deque.peek()) < 0:
        deque.push_left(deque.pop())

    # Вывод отрицательных чисел
    while int(deque.peek()) < 0:
        print(deque.pop(), end=' ')
    print()

    # Вывод положительных чисел
    while not deque.is_empty():
        print(deque.pop_left(), end=' ')
    print()


# Вывести строки из файла в обратном порядке
def task_8():
    # Чтение и вывод изначального варианта
    stack = Stack()
    with open('lab_4_files/books.txt') as books:
        for book in books:
            print(book.rstrip())
            stack.push(book)

    print('🔄')

    # Запись и вывод перевернутого варианта
    with open('lab_4_files/reversed_books.txt', 'w') as reversed_books:
        while not stack.is_empty():
            print(stack.peek().rstrip())
            reversed_books.write(stack.pop())
