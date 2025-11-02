import sys
n = int(sys.stdin.readline())
trees = list(map(int, sys.stdin.readline().split()))
trees.sort(reverse=True)
print(trees)
