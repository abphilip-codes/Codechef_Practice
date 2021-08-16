# https://www.codechef.com/problems/AVG

for T in range(int(input())):
    n,k,v=map(int,input().split())
    a=list(map(int,input().split()))
    ans=v*(n+k)-sum(a)
    print(int(ans//k)) if(ans%k==0 and ans>=0) else print(-1)