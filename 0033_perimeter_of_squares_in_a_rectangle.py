def perimeter(n: int) -> int:
    output = [0, 1]
    for i in range(n):
        output.append(output[-1] + output[-2])
    return(sum(output) * 4)


# https://www.codewars.com/kata/559a28007caad2ac4e000083/