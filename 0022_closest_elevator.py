def elevator(left: int, right: int, call: int) -> str:
    return "right" if abs(right - call) <= abs(left - call) else "left"


# https://www.codewars.com/kata/5c374b346a5d0f77af500a5a/