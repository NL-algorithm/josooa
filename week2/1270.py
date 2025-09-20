import sys

n = int(sys.stdin.readline())
for _ in range(n):
    s = list(map(int, sys.stdin.readline().split()))
    t = s[0]
    s = s[1:]
    dict_s = {}
    for i in s:
        if i in dict_s:
            dict_s[i] += 1
        else:
            dict_s[i] = 1
    if max(dict_s.values()) > (t)//2:
        print(max(dict_s, key=dict_s.get))
    else:
        print("SYJKGW")