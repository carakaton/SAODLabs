import display


# Таблица хешей
class HashTable():
    size = 10

    def __init__(self, values: list, length: int = size):
        self.values = [None] * length
        for value in values:
            self.insert(value)

    @staticmethod
    def hash_string(string):
        hash = 0
        for i in range(len(string)):
            hash += ord(string[i]) * (i + 1)
        return hash % HashTable.size

    @staticmethod
    def hash_number(number):
        hash = int(((number % HashTable.size) * 331) & 127)
        return hash % HashTable.size


# Таблица с простым рехешированием
class SimpleRehashTable(HashTable):
    overflow = []
    rehashes = []

    def insert(self, value):
        hash = self.hash_string(value)
        base_hash = hash
        while self.values[hash] is not None:
            hash -= 1
            if hash == -(HashTable.size - base_hash):
                self.overflow.append(value)
                return

        if hash != base_hash: self.rehashes.append(
            f"\n{value} ({(hash + HashTable.size) % HashTable.size}) коллизия в ячейке {base_hash}")
        self.values[hash] = value

    def display(self, show_overflows=True, show_rehashes=False):
        print('Таблица с простым рехешированием')

        for i, value in enumerate(self.values):
            if value is not None:
                print(f'{i}: {value}')
            else:
                print(f'{i}: Нет значения')

        if self.overflow != [] and show_overflows:
            display.print_values(self.overflow, 'Переполнение: ')
        if self.rehashes != [] and show_rehashes:
            display.print_values(self.rehashes, 'Рехеширование: ')
        print()

    def find(self, value):
        hash = HashTable.hash_string(value)
        base_hash = hash
        while self.values[hash] != value:
            hash -= 1
            if hash == -(HashTable.size - base_hash):
                self.overflow.append(value)
                return False
        return True


# Таблица с рехешированием с помощью псевдослучайных чисел
class RandomRehashTable(HashTable):
    overflow = []
    rehashes = []

    def insert(self, value):
        hash = HashTable.hash_string(value)
        base_hash = hash

        attempt = 1
        rand = 1
        while self.values[hash] is not None:
            rand *= attempt
            hash = (hash + rand + 1) % HashTable.size
            attempt += 1
            if attempt == HashTable.size + 1:
                self.overflow.append(value)
                return

        if hash != base_hash: self.rehashes.append(
            f"\n{value} ({(hash + HashTable.size) % HashTable.size}) коллизия в ячейке {base_hash}")
        self.values[hash] = value

    def display(self, show_overflows=True, show_rehashes=False):
        print('Таблица с рехешированием с помощью псведослучайных чисел')

        for i, value in enumerate(self.values):
            if value is not None:
                print(f'{i}: {value}')
            else:
                print(f'{i}: Нет значения')

        if self.overflow != [] and show_overflows:
            display.print_values(self.overflow, 'Переполнение: ')
        if self.rehashes != [] and show_rehashes:
            display.print_values(self.rehashes, 'Рехеширование: ')
        print()

    def find(self, value):
        hash = HashTable.hash_string(value)
        base_hash = hash

        attempt = 1
        rand = 1
        while self.values[hash] != value:
            rand *= attempt
            hash = (hash + rand + 1) % HashTable.size
            if hash == HashTable.size + 1:
                self.overflow.append(value)
                return False
        return True


# Таблица с рехешированием методом цепочек
class ChainRehashTable(HashTable):

    def insert(self, value):
        hash = HashTable.hash_string(value)
        if self.values[hash] is None:
            self.values[hash] = [value]
        else:
            self.values[hash].append(value)

    def display(self):
        print("Таблица с рехешированием методом цепочек")

        for i, value in enumerate(self.values):
            if value is not None:
                display.print_values(value, f"{i}: ")
            else:
                print(f'{i}: Нет значения')
        print()

    def find(self, value):
        hash = HashTable.hash_string(value)
        if self.values[hash] is not None:
            for _value in self.values[hash]:
                if _value == value:
                    return True
        return False
