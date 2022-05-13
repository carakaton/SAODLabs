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
    lines_count = int(input())
    photo = list(map(int, input().split()))

    main_width = 1
    current_width = 1

    i = 1
    while i != lines_count:
        if photo[i-1] == photo[i]:
            main_width += 1
            i += 1
        else:
            break

    if main_width != lines_count:
        for i in range(main_width + 1, lines_count):
            if photo[i-1] == photo[i]:
                current_width += 1
            elif current_width != main_width:
                break
            else:
                current_width = 1
        else:
            if current_width == main_width:
                print("YES")
            else:
                print("NO")
    else:
        print("YES")


# Файловая система BerOS
def task_3():
    string = input()
    optimized = ""
    counter = 0

    for char in string:
        if char != "/":
            optimized += char
            counter = 0
        else:
            counter += 1
            if counter == 1:
                optimized += char
            else:
                pass

    print(optimized)
