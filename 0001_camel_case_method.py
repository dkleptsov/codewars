def camel_case(string: str) -> str:
    return ''.join(word.title() for word in string.split())


# Solution for: https://www.codewars.com/kata/587731fda577b3d1b0001196