def readposint(prompt='Please enter a positive integer: '):
    while True:
        num = raw_input(prompt)
        try:
            num = int(num)
            if num < 0:
                raise Exception
        except:
            print '%s is not a positive integer. Try again.' % num
            continue
        break
    return num

