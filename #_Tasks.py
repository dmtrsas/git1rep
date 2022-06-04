a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
# найти элементы меньше 5
for i in a:
    if i < 5:
        b.append(i)
# print(b)
# print([elem for elem in a if elem < 5]) - списковое включение - было в уроках!!!


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Вернуть список, состоящий их элементов, которые есть в обоих списках
# a = set(a)
# b = set(b)
# print(a&b)


# найти ключи с 3 самыми большими значениями
mydict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
max3 = sorted(mydict, key=mydict.get, reverse=False)[:3]
print(max3)


def ispalyndrom(string):
    low = string.lower()
    lowrep = low.replace(' ', '')
    #    if lowrep == lowrep[::-1]:
    #        return True
    #    else:
    #        return False
    return lowrep == lowrep[::-1]


print(ispalyndrom('Лёша на полке клопа нашёл'))

# def is_palindrome(string):
#    return string == ''.join(reversed(string))


# Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами
# seq = input('Введите числа через запятую: ')
# lseq = list(seq.split(','))
# tseq = tuple(seq.split(','))
# print(lseq)
# print(tseq)

# Выведите первый и последний элемент списка
# print(lseq[0])
# print(lseq[-1])

#Напишите программу, которая принимает имя файла и выводит его расширение. Если расширение у файла определить невозможно, выбросите исключение
#filename = input('Введите имя файла с расширением: ')
##sep_filename = filename.split('.')
#if '.' in filename:
#    sep_filename = filename.split('.')
#    print(sep_filename[-1])
#else:
#    print('No extension in file')


#Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 101, 167, 5555]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 34]
#a = set(a)
#b = set(b)
#print(a-b)


#Сложите цифры целого числа
def digits(num):
    num = list(str(num))
    sumnum = 0
    for i in num:
        sumnum += int(i)
    print(sumnum)
    #digits = [int(d) for d in str(num)]  другой способ решения
    #return sum(digits)
