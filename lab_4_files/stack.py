# Реализация структуры данных "Стек"
class Stack:

    # Инициализация стека
    def __init__(self):
        self.data = [None] * 0

    # Значение пустой ли стек
    def is_empty(self) -> bool:
        return True if len(self.data) == 0 else False

    # Добавление нового элемента в стек
    def push(self, element):
        length = len(self.data)
        data = [None] * (length + 1)
        for i in range(length):
            data[i] = self.data[i]
        data[-1] = element
        self.data = data

    # Извлечение последнего элемента из стека
    def pop(self):
        length = len(self.data) - 1
        data = [None] * length
        popped = self.data[-1]
        for i in range(length):
            data[i] = self.data[i]
        self.data = data
        return popped

    # Получение последнего элемента в стеке
    def peek(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
            return None

    # Вывод элементов стека в консоль
    def display(self):
        print(self.data)

    # Значение количества элементов в стеке
    def __len__(self) -> int:
        return len(self.data)
