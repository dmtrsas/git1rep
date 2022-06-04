import os

path = 'G:\Pics\Camera'


def obhodfile(path, level=1):
    print('Level = ', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print('Спускаемся', path + '\\' + i)
            obhodfile(path + '\\' + i, level + 1)
            print('Возвращаемся в', path)

obhodfile(path)
# print(i,type(i),path+'\\'+i,os.path.isdir(path+'\\'+i))
