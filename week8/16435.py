import sys
n , l = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))
h.sort()

for i in h:
    if l>=i:
        l+=1
    else:
        break

print(l)