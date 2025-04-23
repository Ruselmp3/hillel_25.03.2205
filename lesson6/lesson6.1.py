import string

user_input = str(input("Введіть діапазон (a-Z): "))
user_input = user_input.split('-')

all_ascii = string.ascii_letters
zxc = all_ascii[all_ascii.index(user_input[0]):(all_ascii.index(user_input[1])+1)]
print(zxc)