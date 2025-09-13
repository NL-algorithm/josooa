import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
sorta = sorted(a,reverse=False)
p = []
for i in range(n):
    p.append(sorta.index(a[i]))
    sorta[sorta.index(a[i])] = -1

for i in range(n):
    print(str(p[i]),end=' ')