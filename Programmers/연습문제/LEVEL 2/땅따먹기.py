# LEVEL 2

def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] = max(land[i-1][j-1], land[i-1][j-2], land[i-1][j-3]) + land[i][j]
    return max(land[-1])