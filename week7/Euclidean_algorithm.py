# Euclidean algorithm(유클리드 호제법)
# (a, b) = (b, r) where r = a % b

def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a
