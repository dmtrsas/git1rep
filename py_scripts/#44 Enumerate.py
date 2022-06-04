a = [10, 20, 30, 40, 50, 60, 70, 80]
s = 'hello world'
t = ('apple', 'banana', 'orange')
d = {'a': 1, 'b': 2, 'c': 3}
# print(list(enumerate(a)))

for index, value in enumerate(t, 1): #можно использовать range
    #    if value % 20 == 0:
    print(index, value)
