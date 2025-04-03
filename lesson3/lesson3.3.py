lst = [1, 2, 3, 4, [3,4,5], "Hello"]

x = len(lst)
my_list = x // 2

if not x:
    result = [lst, lst]
    print(result)
elif not x % 2:
    half_list1 = lst[:my_list]
    half_list2 = lst[my_list:]
    result = [half_list1, half_list2]
    print(result)
else:
    half_list1 = lst[:my_list + 1]
    half_list2 = lst[my_list + 1:]
    result = [half_list1, half_list2]
    print(result)





