# https://www.codechef.com/problems/DEVUGRAP

for T in range(int(input())):
    N,K=map(int,input().split())
    n,ans=list(map(int,input().split())),0
    for i in range(N):
        if(n[i]>=K): ans+=min(n[i]%K,K-n[i]%K)
        else: ans+=K-n[i]%K
    print(ans)