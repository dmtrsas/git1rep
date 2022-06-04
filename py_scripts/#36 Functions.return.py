# a = abs(-6)
# print(a)
# b = max(4, 5, abs(-90), 6, 7, 53, 7, min(100, 200), 5, 8)
# print(b)

# def sqr(x):
#    print(x**2)
#    return None - Всегда выводит None, если не указана

# def sqr(x):
#    return x ** 2
#
#
# a = sqr((sqr(6)))
# print(a)


# def example():
#    print(1)
#    print(2)
#    return 'Hello'  # работает как break в цикле - выходит из функции
#    print(3)
#    print(4)

# def even(x):
#    # return x%2 == 0 - более легкий вариант, возвращающий тру или фолс
#    if x % 2 == 0:
#        return 'Четное'
#    else:
#        return 'Нечётное'


# print(even(552342362))

# for i in range(11):
#    if i % 2 == 0:
#        print(i, 'Четное')
#    else:
#        print(i, 'Нечётное')

# import math
# def soch(n, k):
#    return (math.factorial(n) / (math.factorial(k) * (math.factorial(n - k))))

#def factor(x):
#    pr = 1
#    for x in range(2, x + 1):
#        pr = pr * x
#    return pr
#
#
#print(factor(4))
#
#for i in range(1, 8):
#    print(i, factor(i))
#
#
#def sochet(n, k):
#    return (factor(n) / (factor(k) * (factor(n - k))))
#print(sochet(5, 3))

def sqrandper(a,b):
    mas = []
    mas.append(a*b)
    mas.append((2*(a+b)))
    return mas

print(sqrandper(10,20))

sqr, perim = sqrandper(2, 5)
print(sqr, perim)
