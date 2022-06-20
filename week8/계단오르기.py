n = int(input())

s = [0]*301
for i in range(n):
    s[i+1] = int(input())

f = [0]*301
f[1] = s[1]
f[2] = s[1]+s[2]  
for i in range(3, n+1):
    f[i] = max(f[i-3]+s[i-1]+s[i], f[i-2]+s[i])

print(f[n])