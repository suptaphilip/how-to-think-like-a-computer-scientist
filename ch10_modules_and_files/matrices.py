def add_row(matrix):
    """
      >>> m = [[0, 0], [0, 0]]
      >>> add_row(m)
      [[0, 0], [0, 0], [0, 0]]
      >>> n = [[3, 2, 5], [1, 4, 7]]
      >>> add_row(n)
      [[3, 2, 5], [1, 4, 7], [0, 0, 0]]
      >>> n
      [[3, 2, 5], [1, 4, 7]]
    """
    import copy
    new_matrix = copy.deepcopy(matrix)
    new_matrix += [[]]
    last_row = len(new_matrix) - 1
    for element in new_matrix[0]:
        new_matrix[last_row] += [0]
    return new_matrix

def add_column(matrix):
    """
      >>> m = [[0, 0], [0, 0]]
      >>> add_column(m)
      [[0, 0, 0], [0, 0, 0]]
      >>> n = [[3, 2], [5, 1], [4, 7]]
      >>> add_column(n)
      [[3, 2, 0], [5, 1, 0], [4, 7, 0]]
      >>> n
      [[3, 2], [5, 1], [4, 7]]
    """
    import copy
    new_matrix = copy.deepcopy(matrix)
    for element in new_matrix:
        element += [0]
    return new_matrix

def add_matrices(m1, m2):
    """
      >>> a = [[1, 2], [3, 4]]
      >>> b = [[2, 2], [2, 2]]
      >>> add_matrices(a, b)
      [[3, 4], [5, 6]]
      >>> c = [[8, 2], [3, 4], [5, 7]]
      >>> d = [[3, 2], [9, 2], [10, 12]]
      >>> add_matrices(c, d)
      [[11, 4], [12, 6], [15, 19]]
      >>> c
      [[8, 2], [3, 4], [5, 7]]
      >>> d
      [[3, 2], [9, 2], [10, 12]]
    """
    matrix_sum = []
    for row in range(len(m1)):
        matrix_sum = add_row(matrix_sum)
    for column in range(len(m1[0])):
        matrix_sum = add_column(matrix_sum)
    for row in range(len(matrix_sum)):
        for column in range(len(matrix_sum[row])):
            matrix_sum[row][column] = m1[row][column] + m2[row][column]
    return matrix_sum

def scalar_mult(s, m):
    """
      >>> a = [[1, 2], [3, 4]]
      >>> scalar_mult(3, a)
      [[3, 6], [9, 12]]
      >>> b = [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
      >>> scalar_mult(10, b)
      [[30, 50, 70], [10, 10, 10], [0, 20, 0], [20, 20, 30]]
      >>>
      [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
    """
    matrix_product = []
    for row in range(len(m)):
        matrix_product = add_row(matrix_product)
    for column in range(len(m[0])):
        matrix_product = add_column(matrix_product)
    for row in range(len(matrix_product)):
        for column in range(len(matrix_product[row])):
            matrix_product[row][column] = s * m[row][column]
    return matrix_product

def row_times_column(m1, row, m2, column):
    """
      >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 0)
      19
      >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 1)
      22
      >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 0)
      43
      >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 1)
      50
    """
    product = 0
    for index in range(len(m2)):
        product += m1[row][index] * m2[index][column]
    return product

def matrix_mult(m1, m2):
    """
      >>> matrix_mult([[1, 2], [3, 4]], [[5, 6], [7, 8]])
      [[19, 22], [43, 50]]
      >>> matrix_mult([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 1], [2, 3]])
      [[31, 19], [85, 55]]
      >>> matrix_mult([[7, 8], [9, 1], [2, 3]], [[1, 2, 3], [4, 5, 6]])
      [[39, 54, 69], [13, 23, 33], [14, 19, 24]]
    """
    matrix_product = []
    for row in range(len(m1)):
        matrix_product = add_row(matrix_product)
    for column in range(len(m2[0])):
        matrix_product = add_column(matrix_product)
    for row in range(len(matrix_product)):
        for column in range(len(matrix_product[row])):
            matrix_product[row][column] = row_times_column(m1, row, m2, column)
    return matrix_product

def new_matrix_mult(m1, m2):
    """
      >>> new_matrix_mult([[1, 2], [3, 4]], [[5, 6], [7, 8]])
      [[19, 22], [43, 50]]
      >>> new_matrix_mult([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 1], [2, 3]])
      [[31, 19], [85, 55]]
      >>> new_matrix_mult([[7, 8], [9, 1], [2, 3]], [[1, 2, 3], [4, 5, 6]])
      [[39, 54, 69], [13, 23, 33], [14, 19, 24]]
    """
    matrix_product = []
    for row in range(len(m1)):
        matrix_product.append([])
    for row in range(len(matrix_product)):
        for column in range(len(m2[0])):
            matrix_product[row].extend([0])
    for row in range(len(matrix_product)):
        for column in range(len(matrix_product[row])):
            matrix_product[row][column] = row_times_column(m1, row, m2, column)
    return matrix_product


if __name__ == '__main__':
    import doctest
    doctest.testmod()
