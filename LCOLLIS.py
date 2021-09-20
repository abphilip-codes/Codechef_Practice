# https://www.codechef.com/problems/LCOLLIS

import math
def ncr(n,r): return math.factorial(n)//math.factorial(r)//math.factorial(n-r) if(n>=r) else 0
for _ in range(int(input())):
    (n,m),ans,a = map(int,input().split()),0,[]
    for z in range(n): a.append(input())
    a = [[a[y][x] for y in range(len(a))] for x in range(len(a[0]))]
    for z in range(m): ans+=ncr(a[z].count('1'),2)
    print(ans)