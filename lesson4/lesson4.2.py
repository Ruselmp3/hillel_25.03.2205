lst = [0, 1, 2, 3, 4, 5, 6]

del_two = lst[::2]
summa = sum(del_two)

if len(lst) > 0:
    result = summa * lst[-1]
    print(result)
else:
    print(lst)