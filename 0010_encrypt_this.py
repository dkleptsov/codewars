def encrypt_this(text: str) -> str:
    new_words = []
    for word in text.split():
        new_word = str(ord(word[0]))
        if len(word) == 1: pass
        elif len(word) == 2: new_word += word[-1]
        elif len(word) == 3: new_word += word[-1] + word[1]
        elif len(word) >= 4: new_word +=  word[-1] + word[2:-1] + word[1]   
        new_words.append(new_word)
    return ' '.join(new_words)


# Solution for https://www.codewars.com/kata/5848565e273af816fb000449/