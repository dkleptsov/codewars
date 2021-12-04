def direction(facing:str, turn:int) -> str:
    dirs = ["N","NE","E","SE","S","SW","W","NW"]
    return dirs[(dirs.index(facing) + turn//45)%8]


# https://www.codewars.com/kata/61a8c3a9e5a7b9004a48ccc2/