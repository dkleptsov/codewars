def sort_me(courses: list) -> list:
    return sorted(courses, key = lambda x: (int(x.split("-")[1]), x.split("-")[0]))


# https://www.codewars.com/kata/51f42b1de8f176db5a0002ae