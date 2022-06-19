def solution(w,h):
    def gcd(a, b):
        while b>0:
            a, b = b, a%b
        return a
    
    if w==h:
        answer = w*h - w
    else:
        g = gcd(w, h)
        answer = w*h - int((w/g + h/g - 1)*g)
    return answer
