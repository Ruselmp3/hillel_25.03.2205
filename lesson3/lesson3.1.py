
x = int(input("Введіть перше число: "))
diya = input("Введіть дію з числом: ")
y = int(input("Введіть друге число: "))


if diya == "+":
    result = x + y
elif diya == "-":
    result = x - y
elif diya == "*":
    result = x * y
elif diya == "/":
    if y == 0:
        print("На 0 нічого не ділиться")
    else:
        result = x / y

print(result)






