# Вывод списка значений
def print_values(values: list, message: str = '') -> None:
    text = message
    print(values, sep=', ')


# Вывод матрицы в консоль
def print_matrix(matrix: list[list[any]], element_max_length: int = 4, title: str = '') -> None:
    print(f'\n{title}')
    for line in matrix:
        for number in line:
            cell = str(number)
            print(cell + ' ' * (element_max_length - len(cell)), end=' ')
        print('\n')
