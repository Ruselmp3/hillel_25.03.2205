def common_elements() -> set:

    del_3 = {i for i in range(100) if i % 3 == 0}
    del_5 = {i for i in range(100) if i % 5 == 0}
    common = del_3 & del_5

    return common

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}