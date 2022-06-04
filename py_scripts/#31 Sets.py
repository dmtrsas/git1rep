#a = [1,2,3,1,2,3,4,4,1,2,3,4,5,2]
#print(a)
#print (type(a))
#c = set('sdqssqfqwfq')
#print(c)
#e = set(range(5))
#print(e)
#f = set()
#print(type(f))
#g = set([[1,2],[2,3],[1,2],[2,6]])
#print (g)
#a = list(set(a))
#print(a)

a = {54,45,6,786,89}
#a.add(9) - добавить число (одно)
##a.update('hello') - добавить строку или несколько чисел
#a.update(range(5,10)) - добавить рейндж
#print(a)
#a.discard(4) - удалить элемент
#a.remove(6) - удалить элемент
#a.clear() - очистить сет
#print(a)
#print(len(a)) - длина сета
#print(4 in a, 6 not in a)
a = {4,3,2,1}
b = {3,4,5,6,7}
#print(a&b) #& - Нахождение пересечений в множествах
c = {10,11,12}
#print (a&c)
#a&=c
#print(a,c)
#print(a.intersection(c))

#print (a|b) # Объединение сетов
#print(a.union(b)) #Объединение сетов

#print(a-b) #Вычитание сетов (вычитание всех пересекающихся)
#print (a^b) #Симметричная разность (вычитаются только пересечения

text = input()
a = set()
while text != '':
    slova = text.split()
    a.update(slova)
    text = input()
print(len(a))