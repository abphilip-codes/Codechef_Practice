# https://www.codechef.com/problems/KTTABLE

for T in range(int(input())):
    n,count=int(input()),0
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    for i in range(1,n): A[i]=A[i]-sum(A[:i])
    for i in range(n):
        if(A[i]>=B[i]): count+=1 
    print(count)