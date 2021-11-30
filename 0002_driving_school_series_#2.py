import math


FIRST_HOUR_PRICE = 30
EVERY_OTHER_HALFHOUR_PRICE = 10


def cost(mins: int) -> int:
    if 0 < mins <= 65: return FIRST_HOUR_PRICE
    return FIRST_HOUR_PRICE + math.ceil((mins - 65)/30) * EVERY_OTHER_HALFHOUR_PRICE 


# Solution for https://www.codewars.com/kata/589b1c15081bcbfe6700017a