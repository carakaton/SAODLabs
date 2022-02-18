#создать максимальное число
def createBiggest(numbers, count):
    #сортировка
    for i in range(count-1):
        for j in range(count-i-1):
            
            a = str(numbers[j])
            b = str(numbers[j+1])
            
            lenA = len(a)
            lenB = len(b)
            
            modA = int(a + a[-1] * (lenB - lenA))
            modB = int(b + b[-1] * (lenA - lenB))

            if (modA < modB) or (modA == modB and lenA > lenB):
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    #вывод числа
    result = ""
    for number in numbers:
        result += str(number)
        result += "." #разделители для удобной проверки

    return result

#пример 2.1, 2.2, 2.3, 2.4 и свои 
#numbers = [10, 2]
#numbers = [3, 30, 34, 5, 9]
#numbers = [1]
#numbers = [10]
#
#numbers = [5, 43, 999, 90, 92]
#numbers = [6558, 6512, 606, 66, 60, 32, 9]
#numbers = [45, 455, 4455, 554, 45]
#numbers = [111, 11, 1, 110, 101, 100, 10, 111, 11, 1, 110, 101, 100, 10, 111, 11, 1, 110, 101, 100, 10]

numbers = list(map(int, input().split()))
result = createBiggest(numbers, len(numbers))
print(result)