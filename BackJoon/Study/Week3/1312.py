# Silver 5 - 소수

import sys
input = sys.stdin.readline

a, b, n = map(int, input().split())

for i in range(n):
    a = (a % b) * 10
    ans = a // b

print(ans)