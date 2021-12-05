def ips_between(start:str, end:str) -> int:
    start = [int(x) for x in start.split('.')]
    end = [int(x) for x in end.split('.')]
    result = 0
    for i in range(4):
        result += (end[i]-start[i])*256**(3-i)
    return result


# https://www.codewars.com/kata/526989a41034285187000de4