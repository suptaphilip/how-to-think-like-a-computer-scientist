def only_evens(numbers):
    """
      >>> only_evens([1, 3, 4, 6, 7, 8])
      [4, 6, 8]
      >>> only_evens([2, 4, 6, 8, 10, 11, 0])
      [2, 4, 6, 8, 10, 0]
      >>> only_evens([1, 3, 5, 7, 9, 11])
      []
      >>> only_evens([4, 0, -1, 2, 6, 7, -4])
      [4, 0, 2, 6, -4]
      >>> nums = [1, 2, 3, 4]
      >>> only_evens(nums)
      [2, 4]
      >>> nums
      [1, 2, 3, 4]
    """
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers += [number]
    return even_numbers

def only_odds(numbers):
    """
      >>> only_odds([1, 3, 4, 6, 7, 8])
      [1, 3, 7]
      >>> only_odds([2, 4, 6, 8, 10, 11, 0])
      [11]
      >>> only_odds([1, 3, 5, 7, 9, 11])
      [1, 3, 5, 7, 9, 11]
      >>> only_odds([4, 0, -1, 2, 6, 7, -4])
      [-1, 7]
      >>> nums = [1, 2, 3, 4]
      >>> only_odds(nums)
      [1, 3]
      >>> nums
      [1, 2, 3, 4]
    """
    odd_numbers = []
    for number in numbers:
        if number % 2 != 0:
            odd_numbers += [number]
    return odd_numbers

def multiples_of(num, numlist):
    """
      >>> multiples_of(3, [1, 2, 3])
      [3]
      >>> multiples_of(4, [4, 8, 10])
      [4, 8]
      >>> multiples_of(5, [5, 10, 15])
      [5, 10, 15]
      >>> multiples_of(6, [1, 2, 3])
      []
      >>> num = 7
      >>> numlist = [7, 12, 17, 21, 28]
      >>> multiples_of(num, numlist)
      [7, 21, 28]
      >>> numlist
      [7, 12, 17, 21, 28]
    """
    multiples = []
    for number in numlist:
        if number % num == 0:
            multiples += [number]
    return multiples


if __name__ == '__main__':
    import doctest
    doctest.testmod()
