import os


# Реализация вида
class View:
    s: {} = {}  # Словарь всех видов

    # Инициализация вида
    def __init__(self, name: str, code: () = None):
        self.name = name  # Имя вида
        self.code = code  # Исполняемый код вида
        self.children = []  # Список дочерних видов
        self.parent = None  # Родительский вид
        View.s.setdefault(name, self)

    # Добавление дочерних видов к виду
    def add_children(self, *views):
        for view in views:
            self.children.append(view)
            view.parent = self

    # Вывод вида в консоль
    def display(self):
        # Сохранение в файл
        with open("save.data", 'w') as save:
            save.write(self.name)

        print("-----------------------------------------------")
        os.system('clear')
        print(f"{self.name}\n")

        if self.code is not None:
            self.code()
            """
            try: 
                self.code()
            except(): 
                print("Ой, во время выполнения кода произошла ошибка 🤕")
            """

        if len(self.children) > 0:
            i = 0
            for view in self.children:
                i += 1
                print(f"{i}. {view.name}")
            if self.parent is not None: print(f"0. {self.parent.name}")
            print()
            while True:
                try:
                    enter = int(input("Введите номер элемента, чтобы перейти: "))
                    if enter == 0:
                        if self.parent is not None:
                            self.parent.display()
                            break
                        else:
                            break
                    elif 1 <= enter <= len(self.children):
                        self.children[enter - 1].display()
                        break
                except:
                    pass
        elif self.parent is not None:
            input("\nНажмите Enter чтобы вернуться")
            self.parent.display()

    # Загрузка сохранения из файла
    @staticmethod
    def load_save(start_view):
        with open("save.data") as save:
            link = save.readline().rstrip()
        view = View.s.get(link)
        if view is not None:
            view.display()
        else:
            input("Сохранение повреждено.\n\nНажмите Enter чтобы вернуться к стартовому меню")
            start_view.display()
