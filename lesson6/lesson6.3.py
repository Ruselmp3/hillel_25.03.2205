user_input = int(input("Введіть число: "))

while user_input > 9:
    promejutok = 1
    for digit in str(user_input):
        promejutok *= int(digit)
    user_input = promejutok
print(user_input)