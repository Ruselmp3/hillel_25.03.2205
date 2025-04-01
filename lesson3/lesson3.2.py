
lst = [1, 2, 3, [3,4,5]]
if len(lst) >1:
    lst.insert(0, lst[-1])
    lst.pop()
    print(lst)
else:
    print(lst)


