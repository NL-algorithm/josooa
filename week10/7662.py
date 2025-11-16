import heapq
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    min_heap = []
    max_heap = []
    entry_finder = {}
    REMOVED = '<removed>'
    count = 0

    for _ in range(k):
        command, num = sys.stdin.readline().split()
        num = int(num)

        if command == 'I':
            count += 1
            entry = [num, count]
            entry_finder[count] = entry
            heapq.heappush(min_heap, entry)
            heapq.heappush(max_heap, [-num, count])
        elif command == 'D':
            if num == 1:
                while max_heap:
                    value, idx = heapq.heappop(max_heap)
                    if idx in entry_finder:
                        del entry_finder[idx]
                        break
            elif num == -1:
                while min_heap:
                    value, idx = heapq.heappop(min_heap)
                    if idx in entry_finder:
                        del entry_finder[idx]
                        break

    while min_heap and min_heap[0][1] not in entry_finder:
        heapq.heappop(min_heap)
    while max_heap and max_heap[0][1] not in entry_finder:
        heapq.heappop(max_heap)

    if not entry_finder:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])