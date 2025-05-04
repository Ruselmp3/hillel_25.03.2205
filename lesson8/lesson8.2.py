import string

def is_palindrome(text: str) -> bool:
    zaborona = string.punctuation + " "
    cleared_str = ''.join([char for char in text.lower() if char not in zaborona])
    if cleared_str == cleared_str[::-1]:
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")