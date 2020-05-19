#!python3
from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)


@lru_cache(maxsize=None)
def fibo(n):
    if n == 0:
        answer = 0
    elif n == 1:
        answer = 1
    else:
        answer = fibo(n-1)+fibo(n-2)
    return answer


print(fibo(1000))
