lst = [3, 4, 0, 6 ,7]


x = 0
y = len(lst)
z = 0

while z < y:
    if lst[x] == 0:
        lst.append(lst.pop(x))
    else:
        x += 1
    z += 1
print(lst)
