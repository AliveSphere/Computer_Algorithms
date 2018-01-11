# Charles Buyas, cjb8qf, 10.31.17, drainage.py
# collaborators; Brady Zhang, bwz3kt


def matrixPath(matrix, row, col):
    curMaxVal = []

    if maxPath[row][col] == 0:
        if row-1 >= 0:
            if matrix[row-1][col] < matrix[row][col]:
                curMaxVal.append(1 + matrixPath(matrix, row-1, col))
        if row+1 < len(maxPath):
            if matrix[row+1][col] < matrix[row][col]:
                curMaxVal.append(1 + matrixPath(matrix, row+1, col))
        if col-1 >= 0:
            if matrix[row][col-1] < matrix[row][col]:
                curMaxVal.append(1 + matrixPath(matrix, row, col-1))
        if col+1 < len(maxPath[0]):
            if matrix[row][col+1] < matrix[row][col]:
                curMaxVal.append(1 + matrixPath(matrix, row, col+1))

        if len(curMaxVal) == 0:
            maxPath[row][col] = 1
        else:
            maxPath[row][col] = max(curMaxVal)

    return maxPath[row][col]


def initializeMatrix(matrix, row, col):
    mat = []
    mat = [[0]*col for i in range(row)]
    return mat


if __name__ == '__main__':
    pass

maxPath = []
f = open('map.txt', 'r') #opens a file named "myvalues.txt" as per instructions
numMatrices = f.readline()

for m in range(int(numMatrices)):
    sizeList = f.readline()
    numRows = int(list(sizeList.split())[1])
    numCols = int(list(sizeList.split())[2])

    matrixVals = []#instantiate a list to contain the values
    maxPath = initializeMatrix(maxPath, numRows, numCols)
    #print(maxPath)

    for j in range(numRows):
        nums = f.readline().split()
        matrixVals.append([int(j) for j in nums]) #parse each value in the file as an int, insert into the list

    #print(matrixVals)
    for i in range(numRows):
        for j in range(numCols):
            matrixPath(matrixVals, i, j)

    print(list(sizeList.split())[0] +": " + str(max(map(max, maxPath))))

