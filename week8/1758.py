import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort(reverse=True)
tip = 0
for idx, val in enumerate(arr):
    real_tip = val - idx
    if real_tip > 0:
        tip += real_tip
print(tip)