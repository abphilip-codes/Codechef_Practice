# https://www.codechef.com/problems/MSNSADM1

for T in range(int(input())):
    n,points=int(input()),0
    scores,fouls=list(map(int,input().split())),list(map(int,input().split()))
    for i in range(n):
        if((scores[i]*20-fouls[i]*10)>points): points=scores[i]*20-fouls[i]*10
    print(max(0,points))