def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

def gcd2(a,b):
    while b > 0:
        c = b
        b = a%b
        a = c
    return a

import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    result = a * b // gcd2(a,b)
    print(result)