def add_one(lst: list) -> list:
    added = int("".join(map(str, lst)))+1
    to_list = [int(d) for d in str(added)]
    return to_list

assert add_one([1,2,3,4]) == [1,2,3,5], 'Test1'
assert add_one([9,9,9]) == [1,0,0,0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1,0], 'Test4'
print("ОК")