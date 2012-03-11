def cleanword(word):
    """
      >>> cleanword('what?')
      'what'
      >>> cleanword('"now!"')
      'now'
      >>> cleanword('?+="word!,@$()"')
      'word'
    """
    import string
    for char in word:
        if char in string.punctuation:
            word = ''.join(word.split(char))
    return word

def has_dashdash(s):
    """
      >>> has_dashdash('distance--but')
      True
      >>> has_dashdash('several')
      False
      >>> has_dashdash('critters')
      False
      >>> has_dashdash('spoke--fancy')
      True
      >>> has_dashdash('yo-yo')
      False
    """
    return bool(s.count('--'))

def extract_words(s):
    """
      >>> extract_words('Now is the time! "Now", is the time? Yes, now.')
      ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now']
      >>> extract_words('she tried to curtsey as she spoke--fancy')
      ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy']
    """
    if has_dashdash(s):
        s = s.replace('--', ' ')
    words = s.split()
    for index in range(len(words)):
        words[index] = cleanword(words[index])
        words[index] = words[index].lower()
    return words

def wordcount(word, wordlist):
    """
      >>> wordcount('now', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['now', 2]
      >>> wordcount('is', ['now', 'is', 'time', 'is', 'now', 'is', 'the', 'is'])
      ['is', 4]
      >>> wordcount('time', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['time', 1]
      >>> wordcount('frog', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['frog', 0]
    """
    return [word, wordlist.count(word)]

def wordset(wordlist):
    """
      >>> wordset(['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['is', 'now', 'time']
      >>> wordset(['I', 'a', 'a', 'is', 'a', 'is', 'I', 'am'])
      ['I', 'a', 'am', 'is']
      >>> wordset(['or', 'a', 'am', 'is', 'are', 'be', 'but', 'am'])
      ['a', 'am', 'are', 'be', 'but', 'is', 'or']
    """
    set = []
    for word in wordlist:
        if word not in set:
            set.append(word)
    set.sort()
    return set

def longestword(wordset):
    """
      >>> longestword(['a', 'apple', 'pear', 'grape'])
      5
      >>> longestword(['a', 'am', 'I', 'be'])
      2
      >>> longestword(['this', 'that', 'supercalifragilisticexpialidocious'])
      34
    """
    longest = 0
    for word in wordset:
        word_length = len(word)
        if word_length > longest:
            longest = word_length
    return longest


if __name__ == '__main__':
    import doctest
    doctest.testmod()

