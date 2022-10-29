# Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.

##Практически не работает при больших числах. Например 686786756568778
num = int(input('Ввведите натуральное число: '))
lst = []
n = num
for i in range(2, num + 1):
    while n % i == 0:
        lst.append(i)
        n /=i 
    # print('n = ', n, ' i = ', i)
print('Простые множители числа: ', lst)

## Решение ребят
# num = int(input('Ввведите натуральное число '))
# lst = []
# n = num
# i = 2
# while True:
#     if n % i == 0:
#         lst.append(i)
#         n /=i 
#         i = 2
#     elif n == 1:
#         break
#     else:
#         i += 1
# print('Число простое' if len(lst) == 1 else f'Простые множители:  {lst}')

## Решение Алевтина, работает быстрее всех
# num = int(input('Ввведите натуральное число '))
# lst = []
# n = num
# i = 2
# while i * i <= num:
#     while num % i == 0:
#         num //= i
#         lst.append(i)
#     i += 1
# if num > 1:
#     lst.append(num)
# print(f'Простые множители:  {lst}')
