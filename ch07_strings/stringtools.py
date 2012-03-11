def reverse(s):
    """
        >>> reverse('happy')
        'yppah'
        >>> reverse('Python')
        'nohtyP'
        >>> reverse('')
        ''
        >>> reverse('P')
        'P'
    """
    new_s = ''
    index = -1
    s_length = len(s)
    while index >= -s_length:
        new_s += s[index]
        index -= 1
    return new_s

def mirror(s):
    """
        >>> mirror('good')
        'gooddoog'
        >>> mirror('yes')
        'yessey'
        >>> mirror('Python')
        'PythonnohtyP'
        >>> mirror('')
        ''
        >>> mirror('a')
        'aa'
    """
    new_s = s + reverse(s)
    return new_s

def remove_letter(letter, strng):
    """
        >>> remove_letter('a', 'apple')
        'pple'
        >>> remove_letter('a', 'banana')
        'bnn'
        >>> remove_letter('z', 'banana')
        'banana'
        >>> remove_letter('i', 'Mississippi')
        'Msssspp'
    """
    new_strng = ''
    for ch in strng:
        if ch != letter:
            new_strng += ch
    return new_strng

def is_palindrome(s):
    """
        >>> is_palindrome('abba')
        True
        >>> is_palindrome('abab')
        False
        >>> is_palindrome('tenet')
        True
        >>> is_palindrome('banana')
        False
        >>> is_palindrome('straw warts')
        True
    """
    length = len(s) / 2
    first_half = s[:length]
    second_half = reverse(s[-length:])
    return first_half == second_half

def count(sub, s):
    """
        >>> count('is', 'Mississippi')
        2
        >>> count('an', 'banana')
        2
        >>> count('ana', 'banana')
        2
        >>> count('nana', 'banana')
        1
        >>> count('nanan', 'banana')
        0
    """
    import string
    count = 0
    index = 0
    while index != -1:
        index = string.find(s, sub, index)
        if index != -1:
            count += 1
            index += 1
    return count
    
def remove(sub, s):
    """
        >>> remove('an', 'banana')
        'bana'
        >>> remove('cyc', 'bicycle')
        'bile'
        >>> remove('iss', 'Mississippi')
        'Missippi'
        >>> remove('egg', 'bicycle')
        'bicycle'
    """
    import string
    stop = string.find(s, sub)
    if stop != -1:
        new_s = ''
        start = stop + len(sub)
        index = 0
        while index < len(s):
            if index < stop or index >= start:
                new_s += s[index]
            index += 1
        return new_s
    else:
        return s

def remove_all(sub, s):
    """
        >>> remove_all('an', 'banana')
        'ba'
        >>> remove_all('cyc', 'bicycle')
        'bile'
        >>> remove_all('iss', 'Mississippi')
        'Mippi'
        >>> remove_all('eggs', 'bicycle')
        'bicycle'
    """
    number = 0
    total = count(sub, s)
    while number < total:
        s = remove(sub, s)
        number += 1
    return s


if __name__ == '__main__':
    import doctest
    doctest.testmod()
