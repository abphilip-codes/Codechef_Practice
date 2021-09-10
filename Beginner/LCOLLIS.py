# https://www.codechef.com/problems/LCOLLIS

import math
def ncr(n,r): return math.factorial(n)//math.factorial(r)//math.factorial(n-r) if(n>=r) else 0
for _ in range(int(input())):
    (n,m),ans = map(int,input().split()),0
    for z in range(n): ans+=ncr(input().count('1'),2)
    print(ans)