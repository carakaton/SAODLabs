import os


# Вывод списка значений
def values(values, message=""):
    text = message
    for value in values:
        text += f"{value}, "
    print(text[:-2])


# Комментарий
def title(text):
    print(f"\n\n{text}\n")


# Вывод матрицы в консоль
def print_matrix(matrix, title=""):
    print("\n" + title)
    for line in matrix:
        for number in line:
            cell = str(number)
            print(cell + " " * (4 - len(cell)), end=' ')
        print("\n")


# Комментарий
class View:
    def __init__(self, name, code=None):
        self.name = name
        self.code = code
        self.children = []
        self.parent = None

    def add_children(self, views):
        for view in views:
            self.children.append(view)
            view.parent = self

    def display(self):
        os.system('clear')
        print(f"{self.name}\n")

        if self.code is not None:
            self.code()
            #try: self.code()
            #except: print("Ой, во время выполнения кода произошла ошибка 🤕")

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
