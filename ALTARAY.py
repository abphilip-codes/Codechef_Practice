# https://www.codechef.com/problems/ALTARAY

for T in range(int(input())):
    n,l=int(input()),list(map(int,input().split()))
    ans=[1]*n
    for i in range(n-2,-1,-1):
        if(l[i]^l[i+1]<0): ans[i]=ans[i+1]+1
        else: ans[i]=1
    print(*ans)