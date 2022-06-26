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


#
#
# Task 2
# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.


def square():
    print('Please enter the square side size (in cm):')
    side_size = int(input())
    perimeter = side_size * 4
    area = side_size * 2
    diagonal = math.sqrt((side_size ** 2) * 2)
    square_data = tuple(str(perimeter) + ' cm', str(area) + ' cm2', str(diagonal) + ' cm')
    print(square_data)


square()

# Task 3