# 
#$N$개의 노드로 이루어진 트리가 주어지고 M개의 두 노드 쌍을 입력받을 때 두 노드 사이의 거리를 출력하라.
#
#입력
#첫째 줄에 노드의 개수 
#$N$과 거리를 알고 싶은 노드 쌍의 개수 
#$M$이 입력되고 다음 
#$N-1$개의 줄에 트리 상에 연결된 두 점과 거리를 입력받는다. 그 다음 줄에는 거리를 알고 싶은 
#$M$개의 노드 쌍이 한 줄에 한 쌍씩 입력된다.
#
#출력
# 
#$M$개의 줄에 차례대로 입력받은 두 노드 사이의 거리를 출력한다.

import sys
from collections import defaultdict
n, m = list(map(int, sys.stdin.readline().split()))
graph = defaultdict(list)
for i in range(n-1):
    u, v, w = list(map(int,sys.stdin.readline().split()))
    graph[u].append((v, w))
    graph[v].append((u, w))
for i in range(m):
    s, t = list(map(int, sys.stdin.readline().split()))
    