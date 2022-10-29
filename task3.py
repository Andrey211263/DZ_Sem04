# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
from random import randint


number = int(input('Задайте длину списка = '))
## Формируем случайный массив
lst = []
for i in range(0, number):
    lst.append(randint(0, 10))
print(lst)
## Поиск в исходном массиве дублей(просто перебор)
res = []
length = len(lst)
j = 0
k = 0
while j < length:
    referens = lst[j]
    for i in range(0, length):
        if i!= j:
            if referens == lst[i]:
                k = 1
                break
        # print(f' i = {i}, j = {j}, referens = {referens}, k = {k}, lst[i] = {lst[i]}')
    if k != 1:
        res.append(referens)
    # print()
    j +=1
    k = 0
print('Сприсок не повторяющихся элементов',res) 

## Решение ребят
lst = list(map(int, input('введите послед чисел: ').split()))
res = [i for i in lst if lst.count(i) == 1]
## res = [i for i in set(lst) if lst.count(i) == 1]
print(res)

