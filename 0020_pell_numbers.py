from functools import lru_cache


class Pell(object):
    @lru_cache
    def get(self, n:int) -> int:
        if n == 0: return 0
        elif n == 1: return 1
        else: return 2 * self.get(n-1) + self.get(n-2)


# https://www.codewars.com/kata/5818d00a559ff57a2f000082/