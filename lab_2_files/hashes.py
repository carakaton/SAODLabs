# Реализация хеш-таблицы
class HashTable:

    SIZE = 10  # Размер любой хеш-таблицы

    # Инициализация
    def __init__(self, name: str, values: list, length: int = SIZE) -> None:
        self.name = name
        self.rehashes = []
        self.values = [None] * length
        for value in values: self.insert(value)

    # Шаблон метода рехеширования
    def rehash_method(self, searched: str or None, _hash: int):
        return _hash

    # Вставка элемента в таблицу
    def insert(self, value: str):
        base_hash = self.hash_string(value)
        index = self.rehash_method(None, base_hash)

        if index != base_hash: self.rehashes.append(f'Коллизия: {base_hash}->{index}')
        if index is not None: self.values[index] = value

    # Отображение таблицы
    def display(self, show_rehashes=False):
        print(f'\n{self.name}')

        for i, value in enumerate(self.values):
            if value is not None: print(f'{i}: {value}')
            else: print(f'{i}: Нет значения')

        if self.rehashes != [] and show_rehashes: print(*self.rehashes, sep=', ')

    # Поиск элемента в таблице
    def find(self, value):
        base_hash = HashTable.hash_string(value)

        index = self.rehash_method(value, base_hash)
        return index is not None

    @staticmethod
    def hash_string(string: str) -> int:
        _hash = 0
        for i in range(len(string)):
            _hash += ord(string[i]) * (i + 1)
        return _hash % HashTable.SIZE


# Таблица с простым рехешированием
class SimpleRehashTable(HashTable):
    def rehash_method(self, searched, _hash):
        attempt = 0
        while self.values[_hash] is not searched:
            _hash = (_hash + 1) % HashTable.SIZE
            attempt += 1
            if attempt == HashTable.SIZE:
                return None
        return _hash


# Таблица с рехешированием с помощью псевдослучайных чисел
class RandomRehashTable(HashTable):
    def rehash_method(self, searched, _hash):
        attempt = 0
        while self.values[_hash] is not searched:
            _hash = HashTable.hash_string(str(_hash)) % HashTable.SIZE
            attempt += 1
            if attempt == HashTable.SIZE:
                return None
        return _hash


# Таблица с рехешированием методом цепочек
class ChainRehashTable(HashTable):

    def insert(self, value: str):
        _hash = HashTable.hash_string(value)

        if self.values[_hash] is None:
            self.values[_hash] = [value]
        else:
            self.values[_hash].append(value)

    def display(self):
        print(f'\n{self.name}')

        for i, elements in enumerate(self.values):
            if elements is not None:
                print(f'{i}:', end=' ')
                print(*elements, sep=', ')
            else:
                print(f'{i}: Нет значения')

    def find(self, value):
        _hash = HashTable.hash_string(value)

        if self.values[_hash] is not None:
            for element in self.values[_hash]:
                if element == value:
                    return True
        return False
