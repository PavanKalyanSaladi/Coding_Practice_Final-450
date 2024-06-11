# Creation of two Dimensional Array
import numpy as np
twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)


# Insertion into 2D array
newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=1)      # 0-Row, 1-Column
print(newTwoDArray)

newTwoDArray = np.append(twoDArray, [[1, 2, 3, 4]], axis=0)      # 0-Row, 1-Column
print(newTwoDArray)
