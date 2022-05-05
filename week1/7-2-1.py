n = int(input())
has_list = set(map(int, input().split()))
m = int(input())
want_list = list(map(int, input().split()))

for x in want_list:
    if x in has_list:
        print("yes", end=" ")
    else:
        print("no", end=" ")