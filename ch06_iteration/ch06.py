def is_prime(n):
    """
        >>> is_prime(1)
        False
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(4)
        False
    """
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    i = 3
    m = int(round(n**0.5))
    while i <= m:
        if n % i == 0:
            return False
        i += 2
    return True

def num_digits(n):
    """
        >>> num_digits(12345)
        5
        >>> num_digits(0)
        1
        >>> num_digits(-12345)
        5
    """
    if n == 0:
        return 1
    elif n < 0:
        n = abs(n)
    digits = 0
    while n != 0:
        n /= 10
        digits += 1
    return digits

def num_even_digits(n):
    """
        >>> num_even_digits(123456)
        3
        >>> num_even_digits(2468)
        4
        >>> num_even_digits(1357)
        0
        >>> num_even_digits(2)
        1
        >>> num_even_digits(20)
        2
    """
    if n == 0:
        return 1
    elif n < 0:
        n = abs(n)
    digits = 0
    remainder = 0
    while n != 0:
        remainder = n % 10
        if remainder % 2 == 0:
            digits += 1
        n /= 10
    return digits

def print_digits(n):
    """
        >>> print_digits(13789)
        9 8 7 3 1
        >>> print_digits(39874613)
        3 1 6 4 7 8 9 3
        >>> print_digits(213141)
        1 4 1 3 1 2
    """
    if n == 0:
        return 0
    elif n < 0:
        n = abs(n)
    digit = 0
    while n != 0:
        digit = n % 10
        print digit,
        n /= 10

def sum_of_squares_of_digits(n):
    """
        >>> sum_of_squares_of_digits(1)
        1
        >>> sum_of_squares_of_digits(9)
        81
        >>> sum_of_squares_of_digits(11)
        2
        >>> sum_of_squares_of_digits(121)
        6
        >>> sum_of_squares_of_digits(987)
        194
    """
    if n == 0:
        return 0
    elif n < 0:
        n = abs(n)
    result = 0
    remainder = 0
    while n != 0:
        remainder = n % 10
        result += remainder**2
        n /= 10
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()

