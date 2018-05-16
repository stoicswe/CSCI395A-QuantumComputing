import numpy

def createMatrix(size):
    d = numpy.zeros((size))
    d[0][0] = 1
    return d

def walk(matrix):
    for i in range(1, matrix[0].size):
        matrix[i][0] = matrix[i - 1][0] / 2
        matrix[i][i] = matrix[i][0]
        if (i > 1):
            for x in range(1, i + 1):
                matrix[i][x] = (matrix[i - 1][x - 1]) / 2 + matrix[i - 1][x] / 2
    return matrix

while True:

    sizeOfArrayX = input("Please enter a sizeX for the array: ")
    probabilityMatrix = createMatrix(int(sizeOfArrayX))
    probabilityMatrix = walk(probabilityMatrix)

    print(probabilityMatrix)