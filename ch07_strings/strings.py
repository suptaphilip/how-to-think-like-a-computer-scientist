def print_duck_names():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            print letter + 'u' + suffix
        else:
            print letter + suffix

def count_letters(strng, ch):
    """
        >>> count_letters('apple', 'p')
        2
        >>> count_letters('banana', 'a')
        3
        >>> count_letters('cherry', 'y')
        1
    """
    count = 0
    start = 0
    while start != -1:
        start = find(strng, ch, start)
        if start != -1:
            count += 1
            start += 1
    return count

def find(strng, ch, start=0):
    """
        >>> find('apple', 'p')
        1
        >>> find('banana', 'a', 2)
        3
        >>> find('cherry', 'd')
        -1
    """
    index = start
    while index < len(strng):
        if strng[index] == ch:
            return index
        index += 1
    return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
