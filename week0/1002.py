import sys
import math

tc = int(input())
for _ in range(tc):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = math.dist((x1, y1), (x2, y2))  # 두 중심 사이 거리

    if x1 == x2 and y1 == y2 and r1 == r2:
        ans = -1
    elif d > r1 + r2 or d < abs(r1 - r2):
        ans = 0
    elif d == r1 + r2 or d == abs(r1 - r2):
        ans = 1
    else:
        ans = 2
    print(ans)
