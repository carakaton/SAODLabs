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
