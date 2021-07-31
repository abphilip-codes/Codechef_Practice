# https://www.codechef.com/problems/CHEFARRP

for T in range(int(input())):
    n,c=int(input()),0
    l=list(map(int,input().split()))
    for i in range(1,n):
        s,p=0,1
        for j in range(i,-1,-1):
            s,p=s+l[j],p*l[j]
            if(s==p): c+=1 
    print(c+1)