from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n

if __name__ == '__main__':
    for i in range(1, 11):
        print(fib(i))