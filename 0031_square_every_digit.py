def square_digits(num: int) -> int:
    return int("".join(f"{int(x)**2}" for x in str(num)))


# https://www.codewars.com/kata/546e2562b03326a88e000020