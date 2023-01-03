# Silver 5 - 덩치

n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]
rank = [1] * n

for i in range(n):
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
             rank[i] += 1

print(*rank)