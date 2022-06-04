#a = [['moskva',495],['piter',812], ['penza',8412]]
#q = dict.fromkeys(['a','b','c'],100) #создание словаря со значение по умолчению
#print(q)

#d = {'moskva':495, 1:812, 'penza':'8f12'}
#v = dict{}
#b = {}

#print(d['penza'])

q = {
    1:'one',
    2:'two',
    3:'three'
}
print(q)
#del q[1] - удалить элемент
#print(q)
#print(len(q))
#print(1 in q, 5 in q)

#if 4 in q:
#    print(q[4])
#else:
#    q[4] = 'five'
#print (q)




# q.clear - очистить словать
#print(q.get(3,'No such key')) # получает значение по ключу

#print(q.setdefault(7,'seven'))
#print(q.pop(3))
#q.popitem() - удаляет случайную пару словаря
#print(q.keys()) - возвращает все ключи
#print(q.values()) - возвращает все значения
#for key in q:
#   print(key, q[key])






#print(q)
#q[4] = 'four'
#print(q)
#q[3] = 'Tri'
#print(q)

#person = {}
#s = 'Ivanov Ivan Samara SGU 5 4 5 5 4 3 5'
#s = s.split()
#print(s)
#person['lastname'] = s[0]
#person['firstname'] = s[1]
#person['city'] = s[2]
#person['university'] = s[3]
#person['marks'] = []
#for i in s[4:]:
#    person['marks'].append(int(i))
#
#print(person)