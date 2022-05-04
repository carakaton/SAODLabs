import random


# Вывод доски в консоль
def print_board(board):
    print("  |" + "———|" * 8)
    for y in range(8):
        print(f"{8 - y} |", end=" ")
        for value in board[y]:
            print(value + " |", end=" ")
        print("\n  |" + "———|" * 8)
    print("    a   b   c   d   e   f   g   h")


# Ферзь
class Queen:
    s = []
    offsets = [(1, 2), (1, -2), (-1, -2), (-1, 2), (2, -1), (2, 1), (-2, 1), (-2, -1)]

    # Добавление нового ферзя
    def __init__(self, y, x):
        self.y, self.x, self.d, self.b = y, x, y + x, y - x
        Queen.s.append(self)
        self.try_place_next()

    # Попытка установить следующего ферзя на возможных восьми позициях в случайном порядке
    def try_place_next(self):
        random.shuffle(Queen.offsets)
        for (offset_y, offset_x) in Queen.offsets:
            # Высчитывание данных нового ферзя
            new_y = abs((self.y + offset_y) % 8)
            new_x = abs((self.x + offset_x) % 8)
            new_d = new_y + new_x
            new_b = new_y - new_x

            # Сравнение данных с уже существующими ферзями
            for queen in Queen.s:
                if queen.y == new_y or queen.x == new_x or queen.d == new_d or queen.b == new_b: break
            else:
                queen = Queen(new_y, new_x)

    # Заполнение доски по координатам
    @staticmethod
    def place_on_board(board):
        board[Queen.s[0].y][Queen.s[0].x] = "Q"
        for queen in Queen.s[1:]:
            board[queen.y][queen.x] = "q"
