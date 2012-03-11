#
# seqtools.py
#

def encapsulate(val, seq):
    """
      >>> encapsulate('c', 'abde')
      'c'
      >>> encapsulate('c', ['a', 'b', 'd', 'e'])
      ['c']
      >>> encapsulate('c', ('a', 'b', 'd', 'e'))
      ('c',)
    """
    if type(seq) == type([]):
        return [val]
    if type(seq) == type(()):
        return (val,)
    return val

def insert_in_middle(val, seq):
    """
      >>> my_string = 'abde'
      >>> insert_in_middle('c', my_string)
      'abcde'
      >>> my_list = ['a', 'b', 'd', 'e']
      >>> insert_in_middle('c', my_list)
      ['a', 'b', 'c', 'd', 'e']
      >>> my_tuple = ('a', 'b', 'd', 'e')
      >>> insert_in_middle('c', my_tuple)
      ('a', 'b', 'c', 'd', 'e')
      >>> my_string
      'abde'
      >>> my_list
      ['a', 'b', 'd', 'e']
      >>> my_tuple
      ('a', 'b', 'd', 'e')
    """
    middle = len(seq) / 2
    return seq[:middle] + encapsulate(val, seq) + seq[middle:]

def make_empty(seq):
    """
      >>> make_empty([1, 2, 3, 4])
      []
      >>> make_empty(('a', 'b', 'c'))
      ()
      >>> make_empty("No, not me!")
      ''
    """
    if type(seq) == type([]):
        return []
    if type(seq) == type(()):
        return ()
    return ''

def insert_at_end(val, seq):
    """
      >>> insert_at_end(5, [1, 3, 4, 6])
      [1, 3, 4, 6, 5]
      >>> insert_at_end('x', 'abc')
      'abcx'
      >>> insert_at_end(5, (1, 3, 4, 6))
      (1, 3, 4, 6, 5)
    """
    if type(seq) == type(''):
        return seq + val
    if type(seq) == type(()):
        seq = list(seq)
        seq.append(val)
        return tuple(seq)
    seq.append(val)
    return seq

def insert_in_front(val, seq):
    """
      >>> insert_in_front(5, [1, 3, 4, 6])
      [5, 1, 3, 4, 6]
      >>> insert_in_front(5, (1, 3, 4, 6))
      (5, 1, 3, 4, 6)
      >>> insert_in_front('x', 'abc')
      'xabc'
    """
    if type(seq) == type(''):
        return val + seq
    if type(seq) == type([]):
        seq.insert(0, val)
        return seq
    seq = list(seq)
    seq.insert(0, val)
    return tuple(seq)

def index_of(val, seq, start=0):
    """
      >>> index_of(9, [1, 7, 11, 9, 10])
      3
      >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5))
      3
      >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5), 4)
      6
      >>> index_of('y', 'happy birthday')
      4
      >>> index_of('banana', ['apple', 'banana', 'cherry', 'date'])
      1
      >>> index_of(5, [2, 3, 4])
      -1
      >>> index_of('b', ['apple', 'banana', 'cherry', 'date'])
      -1
    """
    if type(seq) == type(''):
        return seq.find(val, start)
    try:
        return seq.index(val, start)
    except:
        return -1

def remove_at(index, seq):
    """
      >>> remove_at(3, [1, 7, 11, 9, 10])
      [1, 7, 11, 10]
      >>> remove_at(5, (1, 4, 6, 7, 0, 9, 3, 5))
      (1, 4, 6, 7, 0, 3, 5)
      >>> remove_at(2, "Yomrktown")
      'Yorktown'
    """
    if type(seq) == type(''):
        seq = list(seq)
        seq.pop(index)
        sequence = ''
        for char in seq:
            sequence += char
        return sequence
    if type(seq) == type(()):
        seq = list(seq)
        seq.pop(index)
        return tuple(seq)
    seq.pop(index)
    return seq

def remove_val(val, seq):
    """
      >>> remove_val(11, [1, 7, 11, 9, 10])
      [1, 7, 9, 10]
      >>> remove_val(15, (1, 15, 11, 4, 9))
      (1, 11, 4, 9)
      >>> remove_val('what', ('who', 'what', 'when', 'where', 'why', 'how'))
      ('who', 'when', 'where', 'why', 'how')
    """
    if type(seq) == type(''):
        head, sep, tail = seq.paritition(val)
        return head + tail
    if type(seq) == type(()):
        seq = list(seq)
        seq.remove(val)
        return tuple(seq)
    seq.remove(val)
    return seq

def remove_all(val, seq):
    """
      >>> remove_all(11, [1, 7, 11, 9, 11, 10, 2, 11])
      [1, 7, 9, 10, 2]
      >>> remove_all('i', 'Mississippi')
      'Msssspp'
    """
    if type(seq) == type(''):
        seq = list(seq)
        while seq.count(val):
            seq.remove(val)
        sequence = ''
        for char in seq:
            sequence += char
        return sequence
    if type(seq) == type(()):
        seq = list(seq)
        while seq.count(val):
            seq.remove(val)
        return tuple(seq)
    while seq.count(val):
        seq.remove(val)
    return seq

def count(val, seq):
    """
      >>> count(5, (1, 5, 3, 7, 5, 8, 5))
      3
      >>> count('s', 'Mississippi')
      4
      >>> count((1, 2), [1, 5, (1, 2), 7, (1, 2), 8, 5])
      2
    """
    if type(seq) != type([]):
        seq = list(seq)
    return seq.count(val)

def reverse(seq):
    """
      >>> reverse([1, 2, 3, 4, 5])
      [5, 4, 3, 2, 1]
      >>> reverse(('shoe', 'my', 'buckle', 2, 1))
      (1, 2, 'buckle', 'my', 'shoe')
      >>> reverse('Python')
      'nohtyP'
    """
    if type(seq) == type(''):
        seq = list(seq)
        seq.reverse()
        sequence = ''
        for char in seq:
            sequence += char
        return sequence
    if type(seq) == type(()):
        seq = list(seq)
        seq.reverse()
        return tuple(seq)
    seq.reverse()
    return seq

def sort_sequence(seq):
    """
      >>> sort_sequence([3, 4, 6, 7, 8, 2])
      [2, 3, 4, 6, 7, 8]
      >>> sort_sequence((3, 4, 6, 7, 8, 2))
      (2, 3, 4, 6, 7, 8)
      >>> sort_sequence("nothappy")
      'ahnoppty'
    """
    if type(seq) == type(''):
        seq = list(seq)
        seq.sort()
        sequence = ''
        for char in seq:
            sequence += char
        return sequence
    if type(seq) == type(()):
        seq = list(seq)
        seq.sort()
        return tuple(seq)
    seq.sort()
    return seq


if __name__ == '__main__':
    import doctest
    doctest.testmod()

