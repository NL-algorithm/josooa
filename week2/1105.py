import sys

l, r = list(map(str, sys.stdin.readline().split()))

if(len(l) < len(r)):
    l = '0' * (len(r) - len(l)) + l
elif(len(r) < len(l)):
    r = '0' * (len(l) - len(r)) + r
count = 0
flag = True
for i in range(len(l)):
    if l[i] != r[i]:
        flag = False
    if flag and l[i] == r[i] == '8':
        count += 1

print(count)