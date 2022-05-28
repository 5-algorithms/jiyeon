def solution(n, times):
    answer = 0
    d = [0]*2001
    d[2] = times[0]
    d[3] = 2*times[0]
    for i in range(4, n+1):
        temp = []
        for j in range(1, i//2+1):
            temp.append(d[i-j]+times[j-1])
        d[i] = min(temp)
    answer = d[n]
    return answer