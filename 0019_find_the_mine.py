def mineLocation(field: list) -> list:
    for i, row in enumerate(field):
        if sum(row) > 0:
            return [i, row.index(1)]


# https://www.codewars.com/kata/528d9adf0e03778b9e00067e