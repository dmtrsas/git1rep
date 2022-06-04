# a = [i%4 for i in range(1, 15)]
# print(a)


import random

# a = [random.randint(-10, 10) for i in range(10)]
# print(a)
##b = [abs(el)+1 for el in a]
##print(b)
# c = [el for el in a if el%2 == 0 and el%3 == 0]
# print(c)

# d = input().split()
# d = [int(i) for i in d]
# print(d)

n = 4
m = 4
a = [[1] * m for i in range(n)]
print(a)
a[1][3] = 100
for i in a:
    print(i)

a = [(i, j) for i in [2,3,4,5,6] for j in [1, 2, 3] if i*j > 10]
print(a)