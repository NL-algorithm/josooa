import collections
import sys

tc= int(input())
for i in range(tc):
    n, m = map(int, input().split())
    queue = collections.deque(list(map(int, sys.stdin.readline().split())))
    count = 0
    p=m
    while (queue):
        front = queue.popleft() 
        valuehigh = max(queue) 
        p-=1 
        if (valuehigh==front): 
            count+=1
            if (p<0): 
                print(count)
                break
        else:  
            queue.append(front) 
            if (p<0) :  
                p=len(queue) - 1