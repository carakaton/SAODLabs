#сортировка
def sort(nums, count):
    for i in range(count-1):
        for j in range(count-i-1):
            flag = False
            a = str(nums[j])
            al = len(a)
            b = str(nums[j+1])
            bl = len(b)
            
            if al == bl and int(a) < int(b):
                flag = True

            elif al > bl:
                c = 0
                while a[c] == b[c-1]:
                    c += 1
                    
                if a[c] < b[c-1]:
                    flag = True
                    
            elif al < bl:
                c = 0
                while a[c-1] == b[c]:
                    c += 1
                    
                if a[c-1] < b[c]:
                    flag = True
            
            if flag:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = False
    return nums

#вывод
def prt(nums):
    result = ""
    for num in nums:
        result += "."
        result += str(num)
    print(result)
    
variants = [[10, 2], [3, 30, 34, 5, 9], [1], [10], [7, 43, 999, 80, 82], [6512, 6558, 32, 9, 606, 60, 66]]
for variant in variants:
    variant = sort(variant, len(variant))
    prt(variant)