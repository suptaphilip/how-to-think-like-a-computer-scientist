def add_vectors(u, v):
    """
      >>> add_vectors([1, 0], [1, 1])
      [2, 1]
      >>> add_vectors([1, 2], [1, 4])
      [2, 6]
      >>> add_vectors([1, 2, 1], [1, 4, 3])
      [2, 6, 4]
      >>> add_vectors([11, 0, -4, 5], [2, -4, 17, 0])
      [13, -4, 13, 5]
    """
    vector_sum = []
    for index in range(len(u)):
        vector_sum += [u[index] + v[index]]
    return vector_sum

def scalar_mult(s, v):
    """
      >>> scalar_mult(5, [1, 2])
      [5, 10]
      >>> scalar_mult(3, [1, 0, -1])
      [3, 0, -3]
      >>> scalar_mult(7, [3, 0, 5, 11, 2])
      [21, 0, 35, 77, 14]
    """
    scalar_multiple = []
    for value in v:
        scalar_multiple += [s * value]
    return scalar_multiple

def dot_product(u, v):
    """
      >>> dot_product([1, 1], [1, 1])
      2
      >>> dot_product([1, 2], [1, 4])
      9
      >>> dot_product([1, 2, 1], [1, 4, 3])
      12
      >>> dot_product([2, 0, -1, 1], [1, 5, 2, 0])
      0
    """
    dot_prod = []
    for index in range(len(u)):
        dot_prod += [u[index] * v[index]]
    result = 0
    for value in dot_prod:
        result += value
    return result

def cross_product(u, v):
    """
      >>> cross_product([1, 2, 3], [4, 5, 6])
      [-3, 6, -3]
      >>> cross_product([3, 2, 1], [4, 5, 6])
      [7, -14, 7]
      >>> cross_product([1, 2, 3], [6, 5, 4])
      [-7, 14, -7]
      >>> cross_product([3, 2, 1], [6, 5, 4])
      [3, -6, 3]
    """
    product = []
    product += [u[1] * v[2] - u[2] * v[1]]
    product += [u[2] * v[0] - u[0] * v[2]]
    product += [u[0] * v[1] - u[1] * v[0]]
    return product


if __name__ == '__main__':
    import doctest
    doctest.testmod()
