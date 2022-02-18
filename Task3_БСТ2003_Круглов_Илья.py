#ввод матрицы (пример: 1 2 3, 4 5 6, 7 8 9)
def enterMatrix():
    enter = list(input().split(","))
    matrix = list()
    for line in range(len(enter)):
        matrix.append(list(map(int, enter[line].split())))
    return matrix
#вывод матрицы  
def printMatrix(matrix):
    print()
    for line in matrix:
        for number in line:
            cell = str(number)
            print(cell + " "*(3-len(cell)), end=' ')
        print("\n")

#сортировка по-диагонали 
def diagonalSort(matrix):
    matrixHeight = len(matrix)
    matrixLenght = len(matrix[0])
    startY = matrixHeight
    startX = 0
    
    diagonalCount = matrixLenght + matrixHeight - 1
    for d in range(diagonalCount):
        diagonalLength = min(matrixHeight - startY, matrixLenght - startX)
        for i in range(diagonalLength-1):
            y = startY
            x = startX
            for j in range(diagonalLength-i-1):
                if matrix[y][x] > matrix[y+1][x+1]:
                    matrix[y][x], matrix[y+1][x+1] = matrix[y+1][x+1], matrix[y][x]
                y += 1
                x += 1
        
        if startY != 0: 
            startY -= 1
        else: 
            startX += 1

#пример 3.1 и 3.2
#matrix = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
#matrix = [[11, 25, 66, 1, 69, 7], [23, 55, 17, 45, 15, 52], [75, 31, 36, 44, 58, 8], [22, 27, 33, 25, 68, 4], [84, 28, 14, 11, 5, 50]]
#printMatrix(matrix)

matrix = enterMatrix()
diagonalSort(matrix)
printMatrix(matrix)