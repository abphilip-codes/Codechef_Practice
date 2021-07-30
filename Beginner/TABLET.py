# https://www.codechef.com/problems/TABLET

for T in range(int(input())):
    n,k=map(int,input().split())
    m=0
    for i in range(n): 
        inp=list(map(int,input().split()))
        if(inp[2]<=k): 
            if(inp[0]*inp[1]>m): m=inp[0]*inp[1]
    print("no tablet") if(m==0) else print(m)