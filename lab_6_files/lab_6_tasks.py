from lab_6_files.graph import *
from compare import time_of


def task_1():

    # Создание графа из файла
    matrix = get_matrix_from('lab_6_files/matrix.data')
    graph = Graph(matrix)

    # Предварительный просмотр
    print('Посмотрите на граф и выберите точки начала и конца пути.\nЧтобы продолжить, закройте окно.')
    graph.display()

    # Ввод точек, поиск кратчайшего маршрута
    start_point, end_point = map(int, input('\nВведите две точки через пробел: ').split())
    path, distance = graph.bellman_ford(start_point, end_point)

    # Времени поиска маршрута
    time = time_of(graph.bellman_ford, start_point, end_point)
    print(f'\nВремя поиска: {time:.3f}')

    # Вывод маршрута
    if distance != float('Inf'):
        print(f'Кратчайшие расстояние от точки "{start_point}" до точки "{end_point}" = {distance}')
    else:
        print(f'Невозможно построить кратчайший маршрут из точки "{start_point}" в точку "{end_point}"')
    graph.display(path=path)
