def recursive_min(nested_num_list):
    """
      >>> recursive_min([2, 9, [1, 13], 8, 6])
      1
      >>> recursive_min([2, [[100, 1], 90], [10, 13], 8, 6])
      1
      >>> recursive_min([2, [[13, -7], 90], [1, 100], 8, 6])
      -7
      >>> recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6])
      -13
    """
    minimum = nested_num_list[0]
    while type(minimum) == type([]):
        minimum = minimum[0]
    for element in nested_num_list:
        if type(element) == type([]):
            min_of_elem = recursive_min(element)
            if min_of_elem < minimum:
                minimum = min_of_elem
        else:
            if element < minimum:
                minimum = element
    return minimum


if __name__ == '__main__':
    import doctest
    doctest.testmod()

