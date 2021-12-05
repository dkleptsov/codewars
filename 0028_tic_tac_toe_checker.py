def is_solved(board:list) -> int:
    rotated = [list(i)[::-1] for i in zip(*board)] 
    rows = [set(x) for x in board + rotated]
    rows.append({board[i][i] for i in range(3)})
    rows.append({rotated[i][i] for i in range(3)})

    unfinished = False
    for row in rows:
        if row == {2}: return 2
        elif row == {1}: return 1
        elif 0 in row: unfinished = True
    if unfinished: return -1
    return 0


# https://www.codewars.com/kata/525caa5c1bf619d28c000335