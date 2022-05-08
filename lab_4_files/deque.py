# Реализация структуры данных "Дек"
class Deque:

    # Инициализация дека
    def __init__(self):
        self.data = [None] * 0

    # Значение пустой ли дек
    def is_empty(self) -> bool:
        return True if len(self.data) == 0 else False

    # Добавление нового элемента в конец дека
    def push(self, element):
        length = len(self.data)
        data = [None] * (length + 1)
        for i in range(length):
            data[i] = self.data[i]
        data[-1] = element
        self.data = data

    # Извлечение последнего элемента из дека
    def pop(self):
        length = len(self.data) - 1
        data = [None] * length
        popped = self.data[-1]
        for i in range(length):
            data[i] = self.data[i]
        self.data = data
        return popped

    # Получение последнего элемента в деке
    def peek(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
            return None

    # Добавление нового элемента в начало дека
    def push_left(self, element):
        length = len(self.data)
        data = [None] * (length + 1)
        for i in range(length):
            data[i+1] = self.data[i]
        data[0] = element
        self.data = data

    # Извлечение первого элемента из дека
    def pop_left(self):
        length = len(self.data) - 1
        data = [None] * length
        popped = self.data[0]
        for i in range(length):
            data[i] = self.data[i+1]
        self.data = data
        return popped

    # Получение первого элемента в деке
    def peek_left(self):
        if len(self.data) > 0:
            return self.data[0]
        else:
            return None

    # Вывод элементов дека в консоль
    def display(self):
        print(self.data)

    # Значение количества элементов в деке
    def __len__(self) -> int:
        return len(self.data)
