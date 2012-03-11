def replace(s, old, new):
    """
      >>> replace('Mississippi', 'i', 'I')
      'MIssIssIppI'
      >>> s = "I love spom! Spom is my favourite food. Spom, spom, spom, yum!"
      >>> replace(s, 'om', 'am')
      'I love spam! Spam is my favourite food. Spam, spam, spam, yum!'
      >>> replace(s, 'o', 'a')
      'I lave spam! Spam is my favaurite faad. Spam, spam, spam, yum!'
    """
    import string
    return string.join(string.split(s, old), new)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
