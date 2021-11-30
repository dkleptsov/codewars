def valid_solution(board:list) -> bool:
    set9 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for row in board:
        if set(row) != set9: return False
        if row.count(0) > 0: return False

    rotated = [list(i)[::-1] for i in zip(*board)]
    for row in rotated:
        if set(row) != set9: return False
    
    for i, j in [(x, y) for x in (0,3,6) for y in (0,3,6)]:
        block= [board[i+x][j+y] for x in (0,1,2) for y in (0,1,2)]
        if set(block) != set9: return False
    
    return True


# Solution for https://www.codewars.com/kata/529bf0e9bdf7657179000008