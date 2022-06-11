def solution(s):
    answer = ''
    sorted_s = sorted(s, reverse=True)
    for c in sorted_s:
        answer += c
    return answer