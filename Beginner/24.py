# https://www.codechef.com/problems/FLOW005

for T in range(int(input())):
    a,n,s = [100,50,10,5,2,1],int(input()),0
    for i in a: s,n = s+(n//i),n%i
    print(s)