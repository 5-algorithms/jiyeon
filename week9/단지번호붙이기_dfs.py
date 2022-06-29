n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        global cnt
        cnt += 1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

num_houses = []
cnt = 0
danji = 0
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            danji += 1
            num_houses.append(cnt)
            cnt = 0

print(danji)
num_houses.sort()
for i in range(len(num_houses)):
    print(num_houses[i])
