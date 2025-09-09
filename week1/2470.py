import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
left = 0
l=0
r=n-1
right = n-1
min_value = abs(arr[left] + arr[right])
while(left<right):
    current_value = arr[left] + arr[right]
    if abs(current_value) < abs(min_value):
        min_value = current_value
        l=left
        r=right
    if current_value < 0:
        left += 1
    else:
        right -= 1 

print(arr[l], arr[r])
