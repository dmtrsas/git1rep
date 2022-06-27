# Tasks2022
# Libraries
import math
import calendar


# Task1
# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе


def is_year_leap():
    print('Enter the year:')
    year = int(input())
    if calendar.isleap(year) is True:
        return print('Year is leap')
    else:
        return print('Year is not leap')


is_year_leap()
print('Task 1 completed')
print('_________________________________________________________')


# Task 2
# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.


def square():
    print('Please enter the square side size (in cm):')
    side_size = int(input())
    perimeter = side_size * 4
    area = side_size * 2
    diagonal = math.sqrt((side_size ** 2) * 2)
    square_data = tuple([str(perimeter) + ' cm', str(area) + ' cm2', str(diagonal) + ' cm'])
    print(square_data)


square()
print('Task 2 completed')
print('_________________________________________________________')


# Task 3
# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).

def season(month):
    winter = set([1, 2, 12])
    spring = set([3, 4, 5])
    summer = set([6, 7, 8])
    fall = set([9, 10, 11])
    print('Month №' + str(month) + ' is ')
    if month in winter:
        return print('Winter')
    elif month in spring:
        return print('Spring')
    elif month in summer:
        return print('Summer')
    else:
        print('Fall')


season(5)
print('Task 3 completed')
print('_________________________________________________________')


# Task 4
# Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования,
# которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом.
# Написать также функцию XOR_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.


def xor(glkey):
    encrypted = ''
    decrypted = ''

    def xor_cipher(key):
        print('Enter the message to encrypt: ')
        decrypted = input()
        encrypted = ''
        for s in decrypted:
            encrypted += chr(ord(s) ^ key)

        print('Зашифрованное сообщение: ' + encrypted)

    xor_cipher(glkey)

    def xor_decipher(key):
        print('Enter the message to decrypt: ')
        decrypted = ''
        encrypted = input()
        for s in encrypted:
            decrypted += chr(ord(s) ^ key)

        print('Расшифрованное сообщение: ' + decrypted)

    xor_decipher(glkey)


xor(301295)
