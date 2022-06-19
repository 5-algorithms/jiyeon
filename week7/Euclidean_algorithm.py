# Euclidean algorithm(유클리드 호제법): finding the greateds common divisor(최대공약수 찾기)
# (a, b) = (b, r) where r = a % b

def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a
