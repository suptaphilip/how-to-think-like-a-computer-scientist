def sqrt(n):
    approx = n / 2.0
    better = (approx + n / approx) / 2.0
    while better != approx:
        approx = better
        better = (approx + n / approx) / 2.0
        print better
    return approx

def print_triangular_numbers(n):
    result = 0
    index = 1
    while index <= n:
        result += index
        print '%-5d %-5d' % (index, result)
        index += 1

