import sys
#input
n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(m):
    tmp  = input().strip()
    tmparr = []
    for i in range(n):
        tmparr.append(tmp[i])
    arr.append(tmparr)

visited = [[0]*n for _ in range(m)]


def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = 1
    cnt = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visited[nx][ny] == 0 and arr[nx][ny] == arr[x][y]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1
    return cnt

resw = 0
resb = 0
for i in range(m):
    for j in range(n):
        if(visited[i][j] == 0 and arr[i][j] == 'W'):
            resw += bfs(i, j)**2
        elif(visited[i][j] == 0 and arr[i][j] == 'B'):
            resb += bfs(i, j)**2

print(resw, resb)