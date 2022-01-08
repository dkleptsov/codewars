def high_and_low(numbers: str) -> str:
    numbers = [int(x) for x in numbers.split(" ")]
    return f"{max(numbers)} {min(numbers)}"


# https://www.codewars.com/kata/554b4ac871d6813a03000035/