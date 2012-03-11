def compare(x, y):
    if x < y:
        print x, "is less than", y
    elif x > y:
        print x, "is greater than", y
    else:
        print x, "and", y, "are equal"

def truth_table(expression):
    heading = " p      q     %s " % expression
    length = len(heading)
    print heading
    print '=' * length
    
    for p in True, False:
        for q in True, False:
            print "%-7s %-7s %-7s" % (p, q, eval(expression))

