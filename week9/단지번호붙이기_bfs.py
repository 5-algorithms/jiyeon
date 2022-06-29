from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y):
    dq = deque()
    dq.append((x,y))
    graph[x][y] = 0
    cnt = 1
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                dq.append((nx,ny))
                graph[nx][ny] = 0
                cnt += 1
    return cnt

num = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            num.append(bfs(i,j))

print(len(num))
num.sort()
for i in range(len(num)):
    print(num[i])