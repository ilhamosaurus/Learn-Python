import numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriks)

import sys

var_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(
    "Ukuran keseluruhan elemen list dalam bytes = ",
    sys.getsizeof(var_list) * len(var_list),
)
print(
    "Ukuran keseluruhan elemen NumPy dalam bytes = ",
    var_array.size * var_array.itemsize,
)

matriks2 = [[0 for j in range(4)] for i in range(3)]

print(matriks2)

var_mat = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

print(var_mat[2][1])


var_mat2 = numpy.array([[5, 0], [1, -2]])

result = var_mat2 * 2
print(result)
