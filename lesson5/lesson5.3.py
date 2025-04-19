import string

string_input = input(str("Введіть рядок: "))

string_input = ''.join(char for char in string_input if char not in string.punctuation)
string_input = string_input.title()
new_string = string_input.replace(" ", "")

if len(new_string) > 139:
    new_string = new_string[:139]

hashtag= f"#{new_string}"

print(hashtag)
