import itertools 


def permutations(string:str) -> list:
    result = []
    for word in itertools.permutations(string):
        result.append(''.join(word))
        
    return list(set(result))


# Solution for https://www.codewars.com/kata/5254ca2719453dcc0b00027d/