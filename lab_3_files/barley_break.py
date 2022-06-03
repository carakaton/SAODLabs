import queue


# Инверсия - когда больший элемент стоит до меньшего элемента
# Считаем для всех костяшек
def count_inversions(array):
    inversions = 0
    size = len(array)
    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if array[i] > 0 and array[j] > 0:
                if array[i] > array[j]:
                    inversions += 1
    return inversions


# Для определения решаемы ли костяшки
def is_solvable(array, m=4, n=4):
    inversions = count_inversions(array)
    size = len(array)
    # В случае чётного количества костяшек смотрим, на какой строке снизу
    # находится пустое место (последняя строка - нечётное, предпоследняя - чётное и т.д.
    # для решаемости необходима разная чётность кол-ва инверсий и строки пустого места (чёт/нечёт)
    if n * m % 2 == 0:
        for i in range(0, size):
            if array[i] == 0:
                if ((m - i // n) % 2 == 1):
                    return (inversions % 2 == 0)
                else:
                    return (inversions % 2 != 0)
        return False
    # В случае нечётного количества костяшек нужно, чтобы количество инверсий было чётно
    if inversions % 2 == 0:
        return True
    return False


# Класс состояния поля пятнашек
class BoardState:
    array = []  # Для хранения расположение костяшек
    n = 4  # Размерность поля
    m = 4
    pos0 = 0  # Для хранения позиции пустого места
    moves = []  # Для хранения необходимых перемещения для его достижения

    def __init__(self, array, n=4, m=4, pos0=15, moves=[]):
        self.array = array
        self.n = n
        self.m = m
        self.pos0 = pos0
        self.moves = moves

    # Переопределение сравнения по стоимости (законченности поля)
    def __lt__(self, other):
        return self.get_total_mdistance() < other.get_total_mdistance()

    def __le__(self, other):
        return self.get_total_mdistance() <= other.get_total_mdistance()

    # Для проверки равенства игровых полей, проверяем размерность и костяшки
    def equals(self, board):
        return (self.n == board.n and self.m == board.m and self.array == board.array)

    # Для подсчёта костяшек вне позиции
    def get_outofpos_count(self):
        counter = 0
        for i in range(0, len(self.array)):
            # Если проверяем не пустое место и не совпадает позиция
            if (self.array[i] != 0 and i + 1 != self.array[i]):
                counter += 1
        return counter

    # Manhattan Distance - это расстояние на которое нужно передвинуть
    # костяшку, чтобы она оказалась в позиции. В данном методе мы вычисляем
    # сумму всех расстояний всех костяшек поля.
    def get_total_mdistance(self):
        distance = 0
        for i in range(0, len(self.array)):
            # Если проверяем не пустое место вычисляем расстояние
            elem = self.array[i]
            if elem != 0:
                x = abs((elem - 1) % self.n - i % self.n)
                y = abs((elem - 1) // self.n - i // self.n)
                distance += x
                distance += y
                # print("DEBUG get_total_mdistance:", elem-1, i, x, y)
        return distance

    # Для возвращения нового состояния при передвижении костяшки
    def get_moved_state(self, direction):
        # Проверяем направление
        moved_index = None
        if direction == "up":
            moved_index = self.pos0 + self.n
        if direction == "down":
            moved_index = self.pos0 - self.n
        if direction == "left":
            moved_index = self.pos0 + 1
        if direction == "right":
            moved_index = self.pos0 - 1
            # Если указано правильное направление
        if moved_index != None:
            # Добавление нового хода
            new_moves = self.moves.copy()
            new_moves.append(self.array[moved_index])
            # Замена костяшки и пустого места
            new_array = self.array.copy()
            new_array[self.pos0] = new_array[moved_index]
            new_array[moved_index] = 0
            return BoardState(new_array, self.n, self.m, moved_index, new_moves)
        else:
            print("BoardState.get_moved_state(): Invalid direction, use up/down/left/right\n")
            return 0


def solve_astar(array, n=4, m=4, goal=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]):
    # Если нерешаемо, возвращаем пустой массив
    if not is_solvable(array):
        return 'Not solvable'
    else:
        # Создаём приоритетную очередь, для обработки состояний поля
        pq = queue.PriorityQueue()
        current_board = BoardState(array, n, m, array.index(0))
        # Добавляем в очередь изначальное положение игрового поля
        pq.put(current_board)
        # Два массива для доступа к ещё необработанным и уже обработанным состояниям
        open_boardstates = []
        closed_boardstates = []
        # Пока не найдём нужное поле
        while current_board.array != goal and not pq.empty():
            # print("DEBUG current_board:", current_board.array)
            closed_boardstates.append(current_board)
            # Добавляем в очередь все возможные состояния достижимые из данного
            if current_board.pos0 // n != m - 1:
                next_board = current_board.get_moved_state("up")
                # print("DEBUG next_board_up:", next_board.array)
                if not any(x.array == next_board.array for x in closed_boardstates):
                    pq.put(next_board)
            if current_board.pos0 // n != 0:
                next_board = current_board.get_moved_state("down")
                # print("DEBUG next_board_down:", next_board.array)
                if not any(x.array == next_board.array for x in closed_boardstates):
                    pq.put(next_board)
            if current_board.pos0 % n != n - 1:
                next_board = current_board.get_moved_state("left")
                # print("DEBUG next_board_left:", next_board.array)
                if not any(x.array == next_board.array for x in closed_boardstates):
                    pq.put(next_board)
            if current_board.pos0 % n != 0:
                next_board = current_board.get_moved_state("right")
                # print("DEBUG next_board_right:", next_board.array)
                if not any(x.array == next_board.array for x in closed_boardstates):
                    pq.put(next_board)
            current_board = pq.get()
        if pq.empty():
            print("Did not found")
        return current_board.moves;
