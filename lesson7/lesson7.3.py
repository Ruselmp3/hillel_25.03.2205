def second_index(text: str, some_str: str) -> int | None:
    _first = text.index(some_str)
    _second = text.find(some_str, _first+1)
    if _second != -1:
        return _second
    else:
        return None

assert second_index("sims","s") == 3, 'Test 1'
assert second_index("find the river", "e") == 12, 'Test 2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test 4'
print('OK')