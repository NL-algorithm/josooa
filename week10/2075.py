import sys
import heapq
n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    for j in a:
        if len(heap) < n:
            heapq.heappush(heap, j)
        else:
            if heap[0] < j:
                heapq.heappop(heap)
                heapq.heappush(heap, j)
print(heap[0])
