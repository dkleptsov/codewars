def title_case(title:str, minor_words:str='') -> str:
    result = []
    minor_words = minor_words.lower().split()
    for i, word in enumerate(title.split()):
        if i == 0 or word.lower() not in minor_words:
            result.append(word.title())
        else:
            result.append(word.lower())
    return ' '.join(result)


# Solution for https://www.codewars.com/kata/5202ef17a402dd033c000009