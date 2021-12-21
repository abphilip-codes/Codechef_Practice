# https://www.codechef.com/problems/XXOORR

import math
for T in range(int(input())):
    n,k = map(int, input().split())
    a,b = list(map(int, input().split())), [0]*32
    for z in a:
        p=0
        while(z>0):
            if(z&1): b[p]+=1
            z=z>>1
            p+=1
    print(sum([math.ceil(z/k) for z in b]))