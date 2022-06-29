from sys import stdin

input = stdin.readline # 이거 꼭 하자! 안하면 시간초과난다

n, c = map(int, input().split())
house = []
for i in range(n):
    house.append(int(input()))
house.sort()

start = 1 # 최소거리
end = house[n-1] - house[0] # 최대거리
answer = 0

# binary search
while start <= end:
    mid = (start + end)//2
    current = house[0]
    cnt = 1
    for i in range(1, n):
        if house[i] >= current + mid:
            current = house[i]
            cnt += 1
    if cnt >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)