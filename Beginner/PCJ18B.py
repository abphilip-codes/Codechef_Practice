# https://www.codechef.com/problems/PCJ18B

for T in range(int(input())):
    n,s=int(input()),0
    for i in range(n,0,-2): s+=i**2
    print(s)