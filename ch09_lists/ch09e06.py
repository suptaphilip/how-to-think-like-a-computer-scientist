"""
  >>> 13 in junk
  True
  >>> del junk[4]
  >>> junk
  [3, 7, 9, 10, 17, 21, 24, 27]
  >>> del junk[a:b]
  >>> junk
  [3, 7, 27]
"""

"""
  >>> nlist[2][1]
  0
  >>> nlist[0][2]
  17
  >>> nlist[1][1]
  5
"""

"""
  >>> import string
  >>> string.split(message, '??')
  ['this', 'and', 'that']
"""

junk = [3, 7, 9, 10, 13, 17, 21, 24, 27]
a = 2
b = 7

nlist = []
for row in range(3):
    nlist += [[]]
for row in nlist:
    row += [0] * 3
nlist[2][1] = 0
nlist[0][2] = 17
nlist[1][1] = 5

message = "this??and??that"


if __name__ == '__main__':
    import doctest
    doctest.testmod()
