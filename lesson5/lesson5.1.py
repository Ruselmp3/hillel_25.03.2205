import string
import keyword

name = input("Введіть імʼя: ")

if name[0].isdigit():
    print("False")

elif any(char.isupper() for char in name):
    print("False")

elif name in keyword.kwlist:
    print("False")

else:
    wrong_chars = string.punctuation.replace("_", "") + " "
    if any(char in wrong_chars for char in name):
        print("False")
    else:
        underscore_count = 0
        for char in name:
            if char == "_":
                underscore_count += 1
        if underscore_count > 1:
            print("False")
        else:
            print("True")
