# https://www.codechef.com/problems/CHFMOT18

import math
for _ in range(int(input())):
    s,n=map(int,input().split())
    print(math.ceil((s-s%2)/n)+(s%2))