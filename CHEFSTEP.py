# https://www.codechef.com/problems/CHEFSTEP

for T in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    for z in l:
        print("1",end="") if(z%k==0) else print("0",end="")
    print()