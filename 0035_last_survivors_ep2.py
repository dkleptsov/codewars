def last_survivors(input: str) -> str:
    ALPHA = 'abcdefghijklmnopqrstuvwxyz'
    while len(set(input)) != len(input):
        for char in input:
            if input.count(char) >= 2:
                input = input.replace(char, "", 2) + ALPHA[(ALPHA.find(char)+1)%26]
    return input


# https://www.codewars.com/kata/60a1aac7d5a5fc0046c89651/