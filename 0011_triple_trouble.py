def triple_double(num1: str, num2: str) -> int:
    num1, num2 = str(num1), str(num2) 
    for char in set(num1):
        if num1.count(3*char) >= 1 and num2.count(2*char) >= 1:
            return 1
    return 0


# Solution for https://www.codewars.com/kata/55d5434f269c0c3f1b000058/