from typing import List, Tuple


def locate_entrance(office: List[str]) -> Tuple[int, int]:
    for i, row in enumerate(office):
        if "." in row and any([i==0, i==len(office)-1]): return row.find("."), i
        for j, char in enumerate(row):
            if char == ".":
                if any([j==0, j==len(row)-1, j>=len(office[i-1]), j>=len(office[i+1])]):
                    return j, i
                elif any([office[i-1][j] == ' ', office[i+1][j] == ' ', row[j-1] == ' ', row[j+1] == ' ']):
                    return j, i

# https://www.codewars.com/kata/61390c407d15c3003fabbd35