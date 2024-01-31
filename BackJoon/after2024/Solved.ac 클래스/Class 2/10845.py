# Silver 4 - 큐

from collections import deque
import sys
input = sys.stdin.readline

q = deque()
for _ in range(int(input())):
    s = input().rstrip().split()

    if s[0] == 'push':
        q.append(s[1])
    elif s[0] == 'pop':
        print(q.popleft() if q else -1)
    elif s[0] == 'size':
        print(len(q))
    elif s[0] == 'empty':
        print(0 if q else 1)
    elif s[0] == 'front':
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)