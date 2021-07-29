# https://www.codechef.com/problems/ICL1902

for T in range(int(input())):
    n,ans=int(input()),0
    k=n
    while(k>0):
        if(n**(1/2)==int(n**(1/2))): ans,k,n=ans+1,k-n,k-n
        else: n-=1
    print(ans)