# Функция: Пишем формулу
# Пишем формулу
def formula(test, count):
    res = []
    i = 0
    while count != 0:
        inter = test[i]
        if inter != 0:
            res.append(str(inter))
            res.append('x')
            if count != 1:
                res.append('^')
                res.append(str(count))
            res.append('+')
        count -= 1
        i += 1
    if test[i] != 0:
        res.append(str(test[i]))
    else:
        res[-1] = ""  # убираем плюс, если =0
    res.append('=0')
    return res