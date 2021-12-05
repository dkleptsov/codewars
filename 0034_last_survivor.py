def last_survivor(letters: str, coords: list) -> str: 
    for coord in coords:
        letters = letters[:coord] + letters[coord+1:]
    return letters


# https://www.codewars.com/kata/609eee71109f860006c377d1/