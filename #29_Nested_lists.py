a = [[0,2,4,6],[1,5,9,13],[3,10,17,19]]
#print(len(a))
#print(a[2][2])
#b = ['hello','hi','privet','bonjur']
#print(b[2][3])

#for i in a:
#    for j in i:
#        print(j, end=' ')
#    print ()

#for i in range(3):
#    s = 0
#    for j in range(4):
#        s += a[i][j]
#       # print(a[i][j], end= ' ')
#    print(s)

#a = []

#for i in range (n):
#    a.append([0]*m)
#for i in a:
#    print(i)
#
#for i in range(n):
#    b = []
#    for i in range(m):
#        b.append(int(input()))
#    a.append(b)
#for i in a:
#    print(i)
a = []
n = int(input())
for i in range(n):
    a.append([0]*n)
for i in a:
    print(i)

for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 10
        elif i>j:
            a[i][j] = 3
        else:
            a[i][j] = 5
for i in a:
    print(i)

