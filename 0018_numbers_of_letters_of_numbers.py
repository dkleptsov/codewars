def numbers_of_letters(number: int) -> list:
    result = [num2str(number)]
    while result[-1] != "four":
        result.append(num2str(len(result[-1])))
    return result


def num2str(number: int) -> str:
    n_dict = {"1":"one","2":"two","3":"three","4":"four","5":"five",
              "6":"six","7":"seven","8":"eight","9":"nine", "0":"zero"}
    return "".join(n_dict.get(digit, "") for digit in str(number))


# https://www.codewars.com/kata/599febdc3f64cd21d8000117