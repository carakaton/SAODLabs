# WTF?
def task_1():
    tux = int(input())
    foo, bar, baz, quz = 0, 0, 0, 1

    for _ in range(tux):
        foo += int(input())
        bar += 1

        if foo * quz >= bar * baz:
            baz, quz = foo, bar

    print(baz / quz)


# Это зебра?
def task_2():
    columns_count = int(input())
    columns = list(map(int, input().split()))

    base_width, current_width = 1, 1
    miss = False

    for i in range(columns_count - 1):
        if columns[i] != columns[i + 1]:
            break
        base_width += 1

    for i in range(base_width, columns_count - 1):
        if columns[i] == columns[i + 1]:
            current_width += 1
        elif current_width != base_width:
            miss = True
            break
        else:
            current_width = 1

    if (not miss and current_width == base_width) or (base_width == columns_count):
        print('YES')
    else:
        print('NO')


# Файловая система BerOS
def task_3():
    original = input()
    optimized = '/'

    for char in original:
        if (char != '/') or (char == '/' and optimized[-1] != '/'):
            optimized += char

    if optimized[-1] == '/' and len(optimized) > 1:
        optimized = optimized[:-1]

    print(optimized)
