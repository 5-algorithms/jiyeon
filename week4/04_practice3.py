# 개임 개발
# a: row, b: col, rotate, go, back, visited

n, m = map(int, input().split())
a, b, d = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))


def rotate():
    global d 
    d = (d+3)%4

mr = [-1, 0, 1, 0]
mc = [0, 1, 0, -1]
visited = [(a, b)]
def go():
    global a, b, d, mr, mc, board, visited, cnt_rot
    na = a + mr[d]
    nb = b + mc[d]
    if 0<na<n+1 and 0<nb<m+1 and board[na][nb]==0 and (na, nb) not in visited:
        a = na
        b = nb
        visited.append((a, b))
        cnt_rot = 0

def back():
    global a, b, d, mr, mc
    a -= mr[d]
    b -= mc[d]

cnt_rot = 0
while True:
    if cnt_rot<4:
        rotate()
        cnt_rot += 1
        go()
    else:
        back()
        if board[a][b] == 1:
            break
        else:
            cnt_rot = 0

print(len(visited))