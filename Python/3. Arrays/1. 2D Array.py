# Creation of two Dimensional Array
import numpy as np
twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)


# Insertion into 2D array
newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=1)      # 0-Row, 1-Column
print(newTwoDArray)

newTwoDArray = np.append(twoDArray, [[1, 2, 3, 4]], axis=0)      # 0-Row, 1-Column
print(newTwoDArray)


# Accessing an element of 2D Array
def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array):
        print("Incorrect Index")
    else:
        print(array[rowIndex][colIndex])

accessElements(twoDArray, 1, 2)


# Traversal of 2D array
def traversal2DArray(array, rowLen, colLen):
    for i in range(colLen):
        for j in range(rowLen):
            print(array[i][j], end=" ")
        print()

traversal2DArray(twoDArray, 4, 4)


# Searching an element in 2D array
def search2DArray(array, value):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] == value:
                return "Value is at index: " + str(i) + " " + str(j)
    return "Not Found."

print(search2DArray(twoDArray, 5))