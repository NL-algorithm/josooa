import sys
n = int(sys.stdin.readline())
trees = list(map(int, sys.stdin.readline().split()))
trees.sort(reverse=True)
max_time = 0
for i in range(n):
    time_needed = trees[i] + i + 1
    if time_needed > max_time:
        max_time = time_needed
print(max_time + 1)
