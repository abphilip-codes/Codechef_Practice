# https://www.codechef.com/problems/SIMDISH

for T in range(int(input())):
    n,m,s=list(input().split()),list(input().split()),0
    for i in range(len(m)):
        if(m[i] in n): s+=1
    print("similar") if(s>=len(m)/2) else print("dissimilar")