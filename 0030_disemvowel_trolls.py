def disemvowel(input: str) -> str:
    return "".join(x for x in input if x.lower() not in "aeiou")


# https://www.codewars.com/kata/52fba66badcd10859f00097e/