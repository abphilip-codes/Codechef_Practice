# https://www.codechef.com/problems/SUBINC

for T in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[0]*n
    for i in range(n):
        if(a[i-1]>a[i]): b[i]=1 
        else: b[i]=b[i-1]+1 
    print(sum(b))