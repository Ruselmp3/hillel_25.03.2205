lst = [1,2,3,4,5,6]

x = len(lst)
my_list = x // 2

if x == 0:
    print("Лист порожній")
elif x % 2 == 0:
    half_list1 = lst[:my_list]
    half_list2 = lst[my_list:]
    print(half_list1)
    print(half_list2)
elif x % 2 != 0:
    half_list1 = lst[:my_list+1]
    half_list2 = lst[my_list+1:]
    print(half_list1)
    print(half_list2)





