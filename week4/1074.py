import sys
n, r, c = map(int, sys.stdin.readline().split())
result = 0
size = 2 ** n
while n > 0:
    n -= 1
    size //= 2
    if r < size and c < size:
        result += 0 * (size * size)
    elif r < size and c >= size:
        result += 1 * (size * size)
        c -= size
    elif r >= size and c < size:
        result += 2 * (size * size)
        r -= size
    else:
        result += 3 * (size * size)
        r -= size
        c -= size
print(result)