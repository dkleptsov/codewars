def decipher_this(input_string:str) -> str:
    real_words = []

    for word in input_string.split():
        digits, letters = '', ''
        for char in word:
            if char.isdigit():
                digits += char
            else: 
                letters += char
        l1 = chr(int(digits))
        
        if not letters: real_words.append(l1)
        elif len(letters) == 1: real_words.append(l1 + letters)
        elif len(letters) == 2: real_words.append(l1 + letters[-1] + letters[0])
        else: real_words.append(l1 + letters[-1] + letters[1:-1] + letters[0])
        
    return ' '.join(real_words)


# Solution for https://www.codewars.com/kata/581e014b55f2c52bb00000f8