# itertools로 조합 찾아서 다 만들기
# sorting 해서 n번째 원소 출력

import itertools

n = int(input())

numbers = [x for x in range(10)]
arr = []
for i in range(1, 11):
    comb = list(itertools.combinations(numbers, i))
    for c in comb:
        num = ''
        for j in sorted(c, reverse=True):
            num += str(j)
        arr.append(int(num))
    if i==3:
        arr.sort()
        print(f"arr: {arr}")
arr.sort()

if n < len(arr):
    print(arr[n])
else:
    print(-1)
