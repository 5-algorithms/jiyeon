x=3
d_0 = [0]*41
d_1 = [0]*41
d_0[0] = 1
d_0[1] = 0
d_1[0] = 0
d_1[1] = 1

for i in range(2, x+1):
    d_0[i] = d_0[i-1] + d_0[i-2]
    d_1[i] = d_1[i-1] + d_1[i-2]
print(d_0[x], d_1[x])    
    