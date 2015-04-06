"""
primelist - returns list with specified amount of prime numbers

"""


def primelist(n):
    # returns list with specified amount of prime numbers

    if n < 1:
        return []
    elif n == 1:
        return [1]

    lst = [2]
    i = 2
    while len(lst) < (n-1):
        i += 1
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j*j-1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return [1] + lst