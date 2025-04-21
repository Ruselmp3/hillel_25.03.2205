import string
import keyword

name = input("Введіть імʼя: ")

if name[0].isdigit():
    print("False")

elif any(char.isupper() for char in name):
    print("False")

elif name in keyword.kwlist:
    print("False")

elif any(char in string.punctuation and char != "_" for char in name):
    print("False")

elif name.startswith('__') or name.startswith('___'):
    print("False")

elif ' ' in name:
    print("False")

else:
    print("True")
