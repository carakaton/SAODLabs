from os import system


SAVE_FILE = 'save.data'
M_ENTER_NUMBER = 'Введите номер элемента, чтобы перейти: '
M_PRESS_ENTER = '\nНажмите Enter чтобы вернуться'
M_SAVE_FAULT = f'\nСохранение повреждено.\n{M_PRESS_ENTER} к стартовому экрану'


# Реализация экрана
class View:

    s = {}  # Словарь всех экранов

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
        with open(SAVE_FILE, 'w') as save: save.write(self.name)

        # Обнуление и вывод имени
        print('\n' + '-' * 40)
        system('clear')
        print(f'\n{self.name}\n')

        # Выполнение кода, если есть
        if self.code is not None: self.code()

        # Если есть дочерние элементы
        if len(self.children) > 0:

            # Вывод списка связанных элементов
            for i, view in enumerate(self.children): print(f'{i + 1}. {view.name}')
            if self.parent is not None: print(f'0. {self.parent.name}')

            # Получение номера
            number = get_variant(
                message=M_ENTER_NUMBER,
                variants=[x for x in range(0, len(self.children)+1)])

            # Запуск выбранного экрана
            if number == 0: self.parent.display()
            else: self.children[number-1].display()

        # Если есть только родительский экран
        else:
            input(M_PRESS_ENTER)
            self.parent.display()

    # Загрузка сохранения из файла
    @staticmethod
    def load_save(start_view) -> None:
        with open(SAVE_FILE) as save: link = save.readline().rstrip()
        view = View.s.get(link)

        if view is None:
            input(M_SAVE_FAULT)
            start_view.display()
        else:
            view.display()


# Ввод значения из определённого допустимого списка
def get_variant(message: str = None, variants=None) -> str or int:
    print()
    entered = None
    while entered not in variants:
        entered = input(message)
        if entered.isnumeric(): entered = int(entered)
    return entered
