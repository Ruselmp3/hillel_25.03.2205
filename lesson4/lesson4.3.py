import random
x = random.randint(3, 10)
lst = list(random.randint(0, 10) for i in range(x))
print(lst)

new_lst = [lst[0],lst[2],lst[-2]]
print(new_lst)

