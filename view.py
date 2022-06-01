from os import system


def get_variant(message: str = None, variants=None) -> str or int:
    entered = None
    while entered not in variants:
        entered = input(message)
        if entered.isnumeric(): entered = int(entered)
    return entered


# Реализация экрана
class View:
    SAVE_FILE = 'save.data'
    M_PRESS_ENTER = ''

    s: {} = {}  # Словарь всех экранов

    # Инициализация экрана
    def __init__(self, name: str, code=None) -> None:
        self.name = name  # Имя экрана
        self.code = code  # Исполняемый код экрана
        self.children = []  # Список дочерних экранов
        self.parent = None  # Родительский экран
        View.s.setdefault(name, self)

    # Добавление дочерних экранов
    def add_children(self, *views) -> None:
        for view in views:
            self.children.append(view)
            view.parent = self

    # Вывод экрана в консоль
    def display(self) -> None:
        # Запись сохранения в файл
        with open(View.SAVE_FILE, 'w') as save: save.write(self.name)

        # Подготовка
        print('-' * 40)
        system('clear')
        print(f'{self.name}\n')

        # Выполнение кода, если есть
        if self.code is not None: self.code()

        # Вывод списка связанных элементов
        for i, view in enumerate(self.children): print(f'{i+1}. {view.name}')
        if self.parent is not None: print(f'0. {self.parent.name}')
        print()

        # Если есть связанные экраны
        if len(self.children) > 0:
            # Получение номера
            number = get_variant(
                message='Введите номер элемента, чтобы перейти: ',
                variants=[x for x in range(0, len(self.children))])

            # Запуск выбранного экрана
            if number != 0: self.children[number-1].display()
            else: self.parent.display()

        # Если есть только родительский экран
        elif self.parent is not None:
            input('\nНажмите Enter чтобы вернуться')
            self.parent.display()

    # Загрузка сохранения из файла
    @staticmethod
    def load_save(start_view) -> None:
        with open(View.SAVE_FILE) as save: name = save.readline().rstrip()
        view = View.s.get(name)

        if view is not None: view.display()
        else:
            input('Сохранение повреждено.\n\nНажмите Enter чтобы вернуться к стартовому экрану')
            start_view.display()
