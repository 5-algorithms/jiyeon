n = int(input())
triangle = []
for i in range(n):
    line = list(map(int, input().split()))
    if i != 0:
        line[0] += triangle[i-1][0]
        line[len(line)-1] += triangle[i-1][len(triangle[i-1])-1]
        for j in range(1, len(line)-1):
            line[j] += max(triangle[i-1][j], triangle[i-1][j-1])
    triangle.append(line)

print(max(triangle[n-1]))