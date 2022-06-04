def f(x, y): return (x + y) ** 2


lambda x, y: (x + y) ** 2

users = ['John 45', 'Dima 25', 'Evan 30','Mike 18']

users.sort(key = lambda x: x.split(' ')[-1])
print(users)

