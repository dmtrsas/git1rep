def season(m):
    if m in (12, 1, 2):
        return 'Winter'
    elif m in (3, 4, 5):
        return 'Spring'
    elif m in (6, 7, 8):
        return 'Summer'
    else:
        return 'Fall'


print(season(11))


def isprime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


print(isprime(101))

from math import sqrt
def sqr(l):
    p = l * 4
    s = l * l
    d = l * sqrt(2) #или sqrt((l**2)*2)
    a = (p, s, round(d, 3))
    return a
print(sqr(3))
print ('Okey-dokey')