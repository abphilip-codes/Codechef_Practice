# https://www.codechef.com/problems/UTMOPR

for T in range(int(input())):
    n,k=map(int,input().split())
    s=sum(list(map(int,input().split())))
    if(s%2==0):
        print("odd") if(k==1) else print("even")
    else: print("even")