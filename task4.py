# 4) Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0
from random import randint
import f_la # импорт функции формирования формулы


k = int(input('Задайте степень К = '))
## Формируем случайный массив
lst = []
res = []
for i in range(0, k + 1):
    lst.append(randint(0, 100))
print('коэфициенты -> ',lst)

# Вызываем фуцию формирования формулы
result = f_la.formula(lst, k)
print(*result)   

# exit()
length = len(result)

with open('file.txt', 'w') as data:
    for i in range(0, length):
        data.writelines(result[i])