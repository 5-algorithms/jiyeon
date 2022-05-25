import math
def solution(brown, yellow):
    answer = []
    x = (brown/2+2+math.sqrt(brown**2/4-2*brown-4*yellow+4))/2
    y = brown/2+2-x
    answer.append(int(x))
    answer.append(int(y))
    return answer