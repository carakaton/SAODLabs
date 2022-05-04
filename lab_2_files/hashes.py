import display


# Таблица хешей
class Hash_table:
    size = 10

    def __init__(self, values, length=size):
        self.values = [None] * length
        for value in values:
            self.insert(value)

    @staticmethod
    def hash_string(string):
        hash = 0
        for i in range(len(string)):
            hash += ord(string[i]) * (i + 1)
        return hash % Hash_table.size

    @staticmethod
    def hash_number(number):
        hash = int(((number % Hash_table.size) * 331) & 127)
        return hash % Hash_table.size


# Таблица с простым рехешированием
class Simple_rehash_table(Hash_table):
    overflow = []
    rehashes = []

    def insert(self, value):
        hash = Hash_table.hash_string(value)
        base_hash = hash
        while self.values[hash] is not None:
            hash -= 1
            if hash == -(Hash_table.size - base_hash):
                self.overflow.append(value)
                return

        if hash != base_hash: self.rehashes.append(
            f"\n{value} ({(hash + Hash_table.size) % Hash_table.size}) коллизия в ячейке {base_hash}")
        self.values[hash] = value

    def display(self, show_overflows=True, show_rehashes=False):
        print("Таблица с простым рехешированием")

        for i in range(len(self.values)):
            if self.values[i] is not None:
                print(f"{i}: {self.values[i]}")
            else:
                print(f"{i}: Нет значения")

        if self.overflow != [] and show_overflows:
            display.values(self.overflow, "Переполнение: ")
        if self.rehashes != [] and show_rehashes:
            display.values(self.rehashes, "Рехеширование: ")
        print()

    def find(self, value):
        hash = Hash_table.hash_string(value)
        base_hash = hash
        while self.values[hash] != value:
            hash -= 1
            if hash == -(Hash_table.size - base_hash):
                self.overflow.append(value)
                return False
        return True


# Таблица с рехешированием с помощью псведослучайных чисел
class Random_rehash_table(Hash_table):
    overflow = []
    rehashes = []

    def insert(self, value):
        hash = Hash_table.hash_string(value)
        base_hash = hash

        attempt = 1
        rand = 1
        while self.values[hash] is not None:
            rand *= attempt
            hash = (hash + rand + 1) % Hash_table.size
            attempt += 1
            if attempt == Hash_table.size + 1:
                self.overflow.append(value)
                return

        if hash != base_hash: self.rehashes.append(
            f"\n{value} ({(hash + Hash_table.size) % Hash_table.size}) коллизия в ячейке {base_hash}")
        self.values[hash] = value

    def display(self, show_overflows=True, show_rehashes=False):
        print("Таблица с рехешированием с помощью псведослучайных чисел")

        for i in range(len(self.values)):
            if self.values[i] is not None:
                print(f"{i}: {self.values[i]}")
            else:
                print(f"{i}: Нет значения")

        if self.overflow != [] and show_overflows:
            display.values(self.overflow, "Переполнение: ")
        if self.rehashes != [] and show_rehashes:
            display.values(self.rehashes, "Рехеширование: ")
        print()

    def find(self, value):
        hash = Hash_table.hash_string(value)
        base_hash = hash

        attempt = 1
        rand = 1
        while self.values[hash] != value:
            rand *= attempt
            hash = (hash + rand + 1) % Hash_table.size
            if hash == Hash_table.size + 1:
                self.overflow.append(value)
                return False
        return True


# Таблица с рехешированием методом цепочек
class Chain_rehash_table(Hash_table):

    def insert(self, value):
        hash = Hash_table.hash_string(value)
        if self.values[hash] is None:
            self.values[hash] = [value]
        else:
            self.values[hash].append(value)

    def display(self):
        print("Таблица с рехешированием методом цепочек")

        for i in range(len(self.values)):
            if self.values[i] is not None:
                display.values(self.values[i], f"{i}: ")
            else:
                print(f"{i}: Нет значений")

        print()

    def find(self, value):
        hash = Hash_table.hash_string(value)
        if self.values[hash] is not None:
            for _value in self.values[hash]:
                if _value == value:
                    return True
        return False