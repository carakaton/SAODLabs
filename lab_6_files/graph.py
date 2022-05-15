from networkx import DiGraph, planar_layout, draw, \
    draw_networkx_edges as draw_edges, \
    get_edge_attributes as get_attributes, \
    draw_networkx_edge_labels as draw_labels

from matplotlib.pyplot import show


# Запись данных из файла в матрицу
def get_matrix_from(file: str) -> [[float]]:
    with open(file) as lines:
        matrix = [[float(char) if char != '.' else float('Inf')
                   for char in line.split()]
                  for line in lines]
    return matrix


# Реализация графа
class Graph:

    # Инициализация
    def __init__(self, matrix: [[float]]):
        self.point_count = len(matrix)
        self.edges = [(i, j, matrix[i][j])
                      for j in range(self.point_count)
                      for i in range(self.point_count)
                      if matrix[i][j] != float('Inf')]

    # Поиск кратчайшего пути алгоритмом Беллмана-Форда
    def bellman_ford(self, start_point: int, end_point: int) -> ([int], float):
        parent = [None] * self.point_count
        distances = [float('Inf')] * self.point_count
        distances[start_point] = 0.0

        # Поиск расстояния
        for _ in range(self.point_count-1):
            for start, end, weight in self.edges:
                if distances[start] != float('Inf') and distances[start] + weight < distances[end]:
                    distances[end] = distances[start] + weight
                    parent[end] = start
        distance = distances[end_point]

        # Проверка на отрицательные циклы
        for start, end, weight in self.edges:
            if distances[start] != float('Inf') and distances[start] + weight < distances[end]:
                return None, float('Inf')

        # Восстановление пути
        if distance == float('Inf'):
            path = None
        else:
            path = [end_point]
            child = end_point
            while child != start_point:
                child = parent[child]
                path.append(child)

        return path, distance

    # Вывод в окне
    def display(self, path=None):
        visualizer = DiGraph()
        visualizer.add_weighted_edges_from(self.edges)

        layout = planar_layout(visualizer)
        draw(visualizer, with_labels='True', pos=layout)
        draw_labels(visualizer, layout, edge_labels=get_attributes(visualizer, 'weight'))

        if path is not None:
            path = [(path[i+1], path[i]) for i in range(len(path) - 1)]
            draw_edges(visualizer, pos=layout, edgelist=path, edge_color='red', arrowsize=16, width=2)
            draw_labels(visualizer, layout, edge_labels=get_attributes(visualizer, 'weight'))

        show()
