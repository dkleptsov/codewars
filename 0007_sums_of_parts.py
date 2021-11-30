def parts_sums(input_list:list) -> list:
    result = [0]
    for item in input_list[::-1]: 
        result.append(result[-1] + item)
    return result[::-1]


# Solution for https://www.codewars.com/kata/5ce399e0047a45001c853c2b/