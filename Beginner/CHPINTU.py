# https://www.codechef.com/problems/CHPINTU

for _ in range(int(input())):
    n,m=map(int,input().split())
    f,p,ans=list(map(int,input().split())), list(map(int,input().split())),999999999999
    for z in range(1,m+1):
        s=0
        for y in range(n):
            if(f[y]==z): s+=p[y]
        if(s!=0): ans=min(ans,s)
    print(ans)