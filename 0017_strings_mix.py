def mix(s1: str, s2: str) -> str:
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for char in set.union(set(s1), set(s2)):
        if char not in alpha:
            continue
        if 1 < s1.count(char) > s2.count(char):
            result.append(('1', char*s1.count(char)))
        elif 1 < s2.count(char) > s1.count(char):
            result.append(('2', char*s2.count(char)))
        elif 1 < s1.count(char) == s2.count(char):
            result.append(('=', char*s1.count(char)))
    
    return "/".join(f"{i}:{j}" for i,j in sorted(result, key=lambda x: (-len(x[1]), x[0], x[1][0])))


# https://www.codewars.com/kata/5629db57620258aa9d000014