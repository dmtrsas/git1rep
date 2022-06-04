#def printlist (somelist): #локальная переменная somelist
#    for element in somelist: # локальная переменная element
#        print(element)
#Здесь element и some_list – локальные переменные, которые видны только внутри функции, и которые не могут использоваться за ее пределами с теми значениями, которые были им присвоены внутри функции при ее работе.


#def printlist(somelist):
#    for el in somelist:
#        print(el)
#
#printlist([1,2,3,4])
#el = 'q'
#print(el)
#Здесь переменная element внутри функции и переменная с таким же именем вне ее – это две разные переменные, их значения не перекрещиваются и не взаимозаменяются.
# Они называются одинаково, но ссылаются на разные объекты в памяти.
#Более того, переменная с именем element внутри функции живет столько же, сколько выполняется функция и не больше.

#sudden_list = [0, 0, 0, 1] #глобальная переменная
#
#def printlist(somelist):
#   for element in sudden_list: #локальные переменные
#       print(element)
#printlist([1, 2, 3])

#candy = 5
#def getcandy():
#    global candy
#    candy += 1
#    print('У меня есть {} конфет'.format(candy)) #Метод format - форматирование строк 'Hello, {}!'.format('Vasya') >>> 'Hello, Vasya!'
#
#getcandy()
#getcandy()

def get_candy():
    candy = 5 #нелокальная переменная в области видимости

    def increment_candy():
        nonlocal candy  # локальная переменная в области видимости
        candy += 1
        return candy

    return increment_candy


result = get_candy()()
print('Всего {} конфет.'.format(result))