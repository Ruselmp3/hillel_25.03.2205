from typing import Generator

def prime_generator(end: int) -> Generator[int, None, None]:
    primes: list[int] = []
    for n in range(2, end + 1):
        prime1 = True
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                prime1 = False
                break
        if prime1:
            primes.append(n)
            yield n

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
