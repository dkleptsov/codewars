def compute_sum(n:int) -> int:
    return sum(int(digit) for digit in ''.join(str(number) for number in range(n+1)))


# Solution for https://www.codewars.com/kata/527e4141bb2ea5ea4f00072f