# 1) Вычислить число c заданной точностью d
# Пример: при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)
import math


dis = input('Задайте точность = ').split('.')
i = len(dis[1])
num = float(input('Введите дробное число = '))
print(round((math.pi), i))
print('Вывод с заданной точностью: ',round(num, i))
