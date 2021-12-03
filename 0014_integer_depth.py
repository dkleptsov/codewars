def compute_depth(n: int) -> int:
    set10 = {str(digit) for digit in range(10)}
    current_set = set()
    counter = 1
    while True:
        current_set = current_set | {digit for digit in str(n*counter)}
        if current_set == set10:
            return counter
        counter += 1


# Solution for https://www.codewars.com/kata/59b401e24f98a813f9000026/