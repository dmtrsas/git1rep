#a, *b, c = [True, 7, 'Hello', 9, 214, 21, '534']  # a - первое значение, с - последнее, b - остальные
# a, *b, c = 'hello world' - так же работает со строкой
#print(a, b, c)

#s = (4,10)
#print(list(range(*s))) # S распаковывается

#def f(a,b,c,d):
#    print(a,b,c,d)
#
#f(1,2,3,4)
#a = ('hello',True,78,[3,4,5])



#def f(*args):
#    s = 0
#    for i in args:
#        s += i
#    return s


def f(*args,**kwargs):
    print(args,kwargs)
def outprint(*args,sep='#',end='@'):
    print(args,sep,end)

outprint(1,14,5,5,36,121,53312,sep='90')
outprint(1,14,5,end=111)



##f(a=1,b=5,c=6)
#f(5,5,8,9,0,2,4,5, a=5,b=7,d='hello')
#print(1,3,5,5,35,43, sep=' ',end=' ')

a = [1,4,5,6,62]
print(*a)
