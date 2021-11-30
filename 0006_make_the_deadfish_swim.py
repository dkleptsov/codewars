def parse(data: str) -> list:
    current_value, output = 0, []
    for command in data:
        if command == 'i':
            current_value += 1
        elif command == 'd':
            current_value -= 1
        elif command == 's':
            current_value = current_value**2
        elif command == 'o':
            output.append(current_value)
    return output


# Solution for https://www.codewars.com/kata/51e0007c1f9378fa810002a9