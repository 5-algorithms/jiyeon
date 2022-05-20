def solution(answers):
    answer = []
    first = [1,2,3,4,5]*2000
    second = [2,1,2,3,2,4,2,5]*1250
    third = [3,3,1,1,2,2,4,4,5,5]*1000
    cnt = [0, 0, 0]
    
    for ans in answers:
        if first.pop(0) == ans:
            cnt[0] += 1
        if second.pop(0) == ans:
            cnt[1] += 1
        if third.pop(0) == ans:
            cnt[2] += 1
    
    for idx, score in enumerate(cnt):
        if score == max(cnt):
            answer.append(idx+1)
        
    return answer