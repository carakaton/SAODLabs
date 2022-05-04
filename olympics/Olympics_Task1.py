# поиск наибольшого периметра
def findMaxP(segments, count):
    # сортировка
    for i in range(count - 1):
        for j in range(count - i - 1):
            if segments[j] > segments[j + 1]:
                segments[j], segments[j + 1] = segments[j + 1], segments[j]

    # поиск маскимума
    maxP = 0
    for i in range(count - 2):
        a = segments[i]
        b = segments[i + 1]
        c = segments[i + 2]
        P = a + b + c

        if (a + b > c and a + c > b and b + c > a) and (P > maxP):
            maxP = P

    return maxP


# пример 1.1, 1.2, 1.3 и 1.4
# segments = [2, 1, 2]
# segments = [1, 2, 1]
# segments = [3, 2, 3, 4]
# segments = [3, 6, 2, 3]

segments = list(map(int, input().split()))
maxP = findMaxP(segments, len(segments))
print(maxP)