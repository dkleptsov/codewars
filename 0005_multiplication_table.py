def multiplication_table(size: int) -> list:
    table = []
    for i in range(1, size+1):
        table.append([i*j for j in range(1, size+1)])
    return table


# Solution for https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08