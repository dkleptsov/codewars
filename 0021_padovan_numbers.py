from functools import lru_cache


@lru_cache
def padovan(n:int) -> int:
    if n in [0, 1, 2]:
        return 1
    return padovan(n-2) + padovan(n-3)


# https://www.codewars.com/kata/5803ee0ed5438edcc9000087/