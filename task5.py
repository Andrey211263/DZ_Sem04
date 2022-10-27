# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.


# from pdb import line_prefix
import f_la
import re
#--------------------------
# функция обработки сроки, убираем +^
#--------------------------
def splt(file):         #
    f = []
    for line in data:
        print(line)
        f = re.split(r'[+^]', line)
    return f
#--------------------------
# функция обработки сроки в int, 
# 0-ой элемент степень многочлена
#--------------------------
def int_str(f):        
    res = []
    dl = len(f) # длина массива
    count = int(f[1])
    res.append(count) # 0-ой содержит степень многочлена
    i = 0
    while dl > 2:
        tmp = int(f[i+1])
        if count == tmp:
            a = re.split(r'[x]', f[i])
            res.append(a[0])
        else:
            res.append(0)
        count -= 1
        dl -= 2
        i += 2
    a = re.split(r'[x]', f[i])
    res.append(a[0])
    i += 1
    a = re.split(r'[=]', f[i])
    res.append(a[0])
    return res
#--------------------------
# сумируем строки
# условие вхождения a1 > a2
#--------------------------
def sum_str(str1, str2, a1, a2):
    
    result = []
    i = 1
    count = a1
    while a1 != a2:
        result.append(str1[i])
        i += 1
        a1 -=1
    j = 1
    while a1 != 0:
        result.append(int(str1[i]) + int(str2[j]))
        i += 1
        j += 1
        a1 -= 1
    result.append(int(str1[i]) + int(str2[j]))
    return result
#---------------------

f1 = []
f2 = []

path = 'file.txt' 
data = open(path, 'r')
f1 = splt(data) #функция обработки сроки, Убрали +^
data.close()

path = 'file1.txt'
data = open(path, 'r')
f2 = splt(data) #функция обработки сроки, Убрали +^
data.close()

f11 = int_str(f1) # функция обработки сроки в int, 0-й элемент степень
f21 = int_str(f2)
a1 = f11[0]
a2 = f21[0]
print(a1, a2)
if a1 >= a2:
    itof_str = sum_str(f11, f21, a1, a2)
    count = a1
else:
    itof_str = sum_str(f21, f11, a2, a1)
    count = a2

res = f_la.formula(itof_str, count)
print(*res)

# сохраняем в файл полученную формулу
length = len(res)
with open('file2.txt', 'w') as data:
    for i in range(0, length):
        data.writelines((res[i]))
