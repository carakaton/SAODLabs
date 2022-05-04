# Вывод доски в консоль
def print_desk(desk):
    print(".\n  |" + "———|" * 4)
    for y in range(8):
        print(f"{8 - y} |", end=" ")
        for value in desk[y]:
            print(value + " |", end=" ")
        print("\n  |" + "———|" * 4)
