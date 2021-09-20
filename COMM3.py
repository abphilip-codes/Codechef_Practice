# https://www.codechef.com/problems/COMM3

for T in range(int(input())):
    n,k,l=int(input()),0,[]
    for i in range(3):
        l.append(list(map(int,input().split())))
    if(((l[0][0]-l[1][0])**2+(l[0][1]-l[1][1])**2)<=n*n):k+=1
    if(((l[0][0]-l[2][0])**2+(l[0][1]-l[2][1])**2)<=n*n):k+=1
    if(((l[1][0]-l[2][0])**2+(l[1][1]-l[2][1])**2)<=n*n):k+=1
    print("yes") if(k>1) else print("no")